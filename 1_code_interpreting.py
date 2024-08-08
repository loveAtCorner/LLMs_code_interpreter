import os
import re
import requests
import yaml
import json
import concurrent.futures
from typing import List, Tuple

# 清空 output 文件夹
def clear_output_directory(output_dir: str):
    for root, dirs, files in os.walk(output_dir, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

# 读取文件内容并移除注释
def read_file_content_without_comments(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        # 移除单行注释
        content = re.sub(r'#.*', '', content)
        # 移除多行注释
        content = re.sub(r'\'\'\'(.*?)\'\'\'', '', content, flags=re.DOTALL)
        content = re.sub(r'\"\"\"(.*?)\"\"\"', '', content, flags=re.DOTALL)
    return content.strip()

# 裁剪用户提示词
def trim_user_prompt(system_prompt: str, user_prompt: str, max_length: int) -> str:
    total_length = len(system_prompt) + len(user_prompt)
    if total_length > max_length:
        excess_length = total_length - max_length
        user_prompt = user_prompt[:-excess_length]
    return user_prompt

# 准备请求数据
def prepare_data(model: str, system_prompt: str, user_prompt: str) -> dict:
    return {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        "temperature": 0
    }

# 发送请求
def send_request(url: str, headers: dict, data: dict) -> Tuple[int, dict, dict]:
    response = requests.post(url, headers=headers, json=data)
    return response.status_code, response.json(), data

# 处理请求和响应
def process_request_and_response(request_data: dict, response_json: dict, response_dir: str) -> bool:
    try:
        # 写入 request.json 文件
        request_path = os.path.join(response_dir, 'request.json')
        with open(request_path, 'w', encoding='utf-8') as json_file:
            json.dump(request_data, json_file, ensure_ascii=False, indent=4)

        # 写入 response.json 文件
        response_path = os.path.join(response_dir, 'response.json')
        with open(response_path, 'w', encoding='utf-8') as json_file:
            json.dump(response_json, json_file, ensure_ascii=False, indent=4)

        # 提取并写入 response_content.md 文件
        content_list = []
        for choice in response_json.get('choices', []):
            content = choice.get('message', {}).get('content', '')
            content_list.append(content)

        content_path = os.path.join(response_dir, 'response_content.md')
        with open(content_path, 'w', encoding='utf-8') as content_file:
            for content in content_list:
                content_file.write(content + "\n")

        print(f"请求和响应结果已写入 {response_dir} 文件夹")
        return True

    except Exception as e:
        print(f"处理请求和响应时发生错误: {e}")
        return False

# 主函数
def main(config: dict):
    directory = config['directory']
    system_prompt_file = config['system_prompt_file']
    user_prompt_file = config['user_prompt_file']
    output_dir = config['output_dir']
    url = config['url']
    headers = config['headers']
    concurrency = config['concurrency']
    model = config['model']
    input_max_length = config['input_max_length']
    file_extension = config['file_extension']

    # 清空输出文件夹
    clear_output_directory(output_dir)

    # 读取系统提示词
    system_prompt = read_file_content_without_comments(system_prompt_file)
    # 读取用户提示词模板
    user_prompt_template = read_file_content_without_comments(user_prompt_file)

    # 创建镜像文件夹
    os.makedirs(output_dir, exist_ok=True)

    # 遍历目录中的所有文件，包括子目录
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith(file_extension):  # 只处理指定后缀的文件
                files.append(os.path.join(root, filename))

    received_reply_count = 0
    no_reply_count = 0
    successfully_parsed_count = 0
    failed_to_parse_count = 0

    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {}
        for file_path in files:
            file_content = read_file_content_without_comments(file_path)
            relative_path = os.path.relpath(file_path, directory)
            response_dir = os.path.join(output_dir, os.path.dirname(relative_path), os.path.splitext(os.path.basename(file_path))[0])
            os.makedirs(response_dir, exist_ok=True)

            # 模板一
            user_prompt_1 = user_prompt_template.format(file_content=file_content)
            user_prompt_1 = trim_user_prompt(system_prompt, user_prompt_1, input_max_length)
            data_1 = prepare_data(model, system_prompt, user_prompt_1)
            futures[executor.submit(send_request, url, headers, data_1)] = response_dir

        for future in concurrent.futures.as_completed(futures):
            response_dir = futures[future]
            try:
                status_code, response_json, request_data = future.result()
                if status_code == 200:
                    received_reply_count += 1
                    if process_request_and_response(request_data, response_json, response_dir):
                        successfully_parsed_count += 1
                    else:
                        failed_to_parse_count += 1
                else:
                    no_reply_count += 1
                    print(f"请求失败，状态码: {status_code}")
                    print(f"请求数据: {json.dumps(request_data, ensure_ascii=False, indent=4)}")
                    print(f"响应数据: {json.dumps(response_json, ensure_ascii=False, indent=4)}")
            except Exception as e:
                no_reply_count += 1
                print(f"请求处理时发生错误: {e}")

    # 打印统计结果
    print(f"Received replies: {received_reply_count}")
    print(f"No replies: {no_reply_count}")
    print(f"Successfully parsed replies: {successfully_parsed_count}")
    print(f"Failed to parse replies: {failed_to_parse_count}")

if __name__ == "__main__":
    with open('config.yaml', 'r', encoding='utf-8') as config_file:
        config = yaml.safe_load(config_file)
    main(config)

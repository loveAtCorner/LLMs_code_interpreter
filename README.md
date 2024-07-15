# 源码解析工具

## 工具介绍

**核心功能——源代码翻译**

- 脚本级别的功能概括
- 函数/类级别的功能枚举


## 使用方法

前置条件
- vllms框架启动的 qwen1.5-32b大模型的服务接口（openai格式）
- 运行 test.py 测试脚本，判断大模型接口是否能够被正常调用

把源码放在src文件夹目录下
修改配置文件 config.yaml 后，运行 main.py 脚本

```yaml
# 源代码路径
directory: "./src"
# 翻译内容路径
# output_dir: "./output/src_summary"
output_dir: "./output/src_function_list"
# 大模型的接口调用地址
url: "***"
# 大模型的接口的请求头参数信息
headers:
  Authorization: "Bearer sk-***"
  User-Agent: "Apifox/1.0.0 (https://apifox.com)"
  Content-Type: "application/json"
# 大模型请求的并发数
concurrency: 5
# 大模型的系统提示词
system_prompt_file: "./prompt/system_prompt.txt"
# 大模型的用户提示词
# user_prompt_template: "请概括下面这个脚本的核心功能，然后该功能是否和大语言模型的指令精调任务有关```python\n{file_content}\n```"
user_prompt_template: "返回下面这个脚本当中所有函数或者类的名称，及其对应的功能\n返回内容的格式需要遵循markdown表格的形式\n\n```python\n{file_content}\n```"
```


**输出格式**

代码解析文件夹和源码文件夹保持相同的目录结构
- src_summary - 对应脚本的功能概括
- src_function_list - 对应脚本的函数功能清单


## 例子

**用户提示词**
```txt
返回下面这个脚本当中出现的
函数或者类的名称，及其对应的功能
返回内容的格式需要遵循markdown表格的形式
```

**返回内容**
| 函数/类名称 | 功能 |
| --- | --- |
| `ChatModel` | 用于处理聊天相关逻辑的模型类 |
| `create_app` | 从给定的`ChatModel`创建API应用 |
| `main` | 程序主入口，初始化`ChatModel`，创建应用并使用`uvicorn`运行服务器 |



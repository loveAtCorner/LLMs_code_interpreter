# 源码解析工具

## 使用方法

#### 一、测试 API 是否正常运行

默认用户已经使用 vllms 框架启动的 qwen1.5-32b大模型的服务接口（openai格式）

运行 0_source_api_test.py 测试脚本，判断大模型接口是否能够被正常调用
```python
python 0_source_api_test.py
```

#### 二、运行工具脚本

把源码放在src文件夹目录下

```yaml
directory: "./src" # 源代码目录
# output_dir: "./output/src_summary" # 输出目录（已注释）
output_dir: "./output/src_function_list" # 函数列表输出目录
url: "http://20.20.136.251:8001/v1/chat/completions" # API 请求的 URL
headers: # HTTP 请求头
  User-Agent: "Apifox/1.0.0 (https://apifox.com)" # 用户代理
  Content-Type: "application/json" # 内容类型
concurrency: 5 # 并发数
system_prompt_file: "./prompt/system_prompt.txt" # 系统提示文件
# user_prompt_file: "./prompt/user_prompt1.txt" # 用户提示文件（已注释）
user_prompt_file: "./prompt/user_prompt2.txt" # 当前用户提示文件
model: "qwen1.5-32b-chat-int4" # 使用的模型
input_max_length: 4096 # 输入的最大长度
file_extension: ".py" # 处理的文件扩展名
```

修改配置文件 config.yaml 后，运行 1_code_interpreting.py 脚本
```python
python 1_code_interpreting.py
```

## 工具介绍

#### 核心功能——源代码翻译

- 脚本级别的功能概括
- 函数/类级别的功能枚举


**输出格式**

代码解析文件夹 output/src_summary 或者 output/src_function_list 和源码文件夹保持相同的目录结构
- src_summary - 对应脚本的功能概括
- src_function_list - 对应脚本的函数功能清单


#### 案例

**核心功能概括**

```md
这个脚本的核心功能是与一个远程语言模型服务（LLM）进行交互，发送系统提示（system_prompt）和用户输入（user_prompt）作为消息，并获取模型的响应。脚本具有以下主要特性：

1. **配置管理**：使用`Config`类从配置文件中获取服务超时时间（service_time_out）、测试模式标志（is_test_mode）、LLM服务的URL、授权令牌（authorization）和模型名称（model_name）。

2. **发送消息**：根据测试模式（is_test_mode）的不同，脚本会使用不同的请求方法与LLM服务通信。在测试模式下，它会发送一个POST请求，包含模型名称、消息列表（包含系统提示和用户输入）以及温度参数（temperature，这里设置为0，可能用于控制生成响应的随机性）。在非测试模式下，它会发送一个带流式传输（stream=True）的POST请求，以便处理可能的长响应。

3. **处理响应**：成功时，脚本会解析服务返回的JSON响应，并从中提取第一个选择（choices[0]）的message内容作为最终的响应。如果在请求过程中发生超时或异常，脚本会捕获错误并记录日志，同时返回一个空字符串。

4. **日志记录**：脚本在关键步骤中记录日志，包括请求是否成功、LLM的响应内容、以及整个请求过程的执行时间。

5. **错误处理**：对于超时和未知异常，脚本会记录相应的错误日志，并返回一个空字符串作为响应。

这个脚本可以作为一个简单的接口，用于与任何支持类似API的远程语言模型服务进行交互。
```

**函数功能枚举**

```md
| 函数/类名 | 功能 |
| --- | --- |
| `sent_message_to_llm` | 发送消息到LLM（Language Learning Model）服务，获取回复并处理可能的异常 |
```

以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能。这些信息已按照Markdown表格的形式呈现：

| 类/函数名称 | 功能 |
| --- | --- |
| `lifespan` | 一个异步上下文管理器，用于在FastAPI应用的生命周期结束时调用`torch_gc()`。 |
| `create_app` | 创建一个FastAPI应用，包含模型列表、聊天完成和评分评估的端点，并设置跨域资源共享（CORS）和API密钥验证。 |
| `verify_api_key` | 验证请求中的API密钥是否有效。 |
| `list_models` | 返回一个包含模型信息的列表。 |
| `create_chat_completion` | 处理聊天完成请求，根据请求是否为流式生成响应或普通响应。 |
| `create_score_evaluation` | 处理评分评估请求，确保模型不支持生成。 |
| `run_api` | 创建并运行FastAPI应用，监听指定的主机和端口。 |

请注意，此脚本中没有定义类，只有函数。

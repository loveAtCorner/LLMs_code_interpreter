以下是提供的Python脚本中所有函数和类的名称，以及它们的功能。这些信息已按照Markdown表格的形式呈现：

| 类/函数名称 | 功能 |
| --- | --- |
| `Role` | 定义枚举类，表示用户、助手、系统、功能和工具等角色 |
| `Finish` | 定义枚举类，表示停止、长度限制或工具调用结束 |
| `ModelCard` | 定义一个基础模型类，包含模型ID、类型（固定为"model"）、创建时间以及所有者 |
| `ModelList` | 定义一个包含多个`ModelCard`的列表类 |
| `Function` | 定义一个表示函数的类，包含函数名称和参数 |
| `FunctionDefinition` | 定义一个表示函数定义的类，包含名称、描述和参数 |
| `FunctionAvailable` | 定义一个表示可用函数或代码解释器的类，包含类型和函数定义 |
| `FunctionCall` | 定义一个表示函数调用的类，包含ID、类型和函数 |
| `ImageURL` | 定义一个表示图像URL的类，包含URL |
| `MultimodalInputItem` | 定义一个表示多模态输入项的类，包含类型（文本或图像URL）、文本和图像URL |
| `ChatMessage` | 定义一个表示聊天消息的类，包含角色、内容（文本或多模态输入项列表）和工具调用 |
| `ChatCompletionMessage` | 定义一个表示聊天完成消息的类，包含角色、内容和工具调用 |
| `ChatCompletionRequest` | 定义一个表示聊天完成请求的类，包含模型、消息列表、工具列表、采样选项等 |
| `ChatCompletionResponseChoice` | 定义一个表示聊天完成响应选项的类，包含索引、消息和结束原因 |
| `ChatCompletionStreamResponseChoice` | 定义一个表示聊天完成流响应选项的类，包含索引、消息变化和可选的结束原因 |
| `ChatCompletionResponseUsage` | 定义一个表示聊天完成响应使用情况的类，包含提示令牌数、完成令牌数和总令牌数 |
| `ChatCompletionResponse` | 定义一个表示聊天完成响应的类，包含ID、对象类型、创建时间、模型、选项列表和使用情况 |
| `ChatCompletionStreamResponse` | 定义一个表示聊天完成流响应的类，包含ID、对象类型、创建时间、模型和选项列表 |
| `ScoreEvaluationRequest` | 定义一个表示评分评估请求的类，包含模型、消息列表和最大长度 |
| `ScoreEvaluationResponse` | 定义一个表示评分评估响应的类，包含ID、对象类型、模型和评分列表 |

这些类主要用于定义不同类型的模型、消息、请求和响应，用于构建一个聊天机器人系统，支持多模态输入、工具调用、聊天完成和评分评估等功能。

以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 类/函数名 | 功能描述 |
| --- | --- |
| `WebChatModel` | 一个基于`ChatModel`的类，用于管理聊天模型的加载、卸载和交互。 |
| `__init__` | 初始化方法，设置`Manager`实例，`demo_mode`和`engine`，并根据`lazy_init`参数决定是否立即加载模型。 |
| `loaded` | 属性，返回`engine`是否已加载的布尔值。 |
| `load_model` | 生成器函数，加载模型并显示加载进度和错误消息。 |
| `unload_model` | 生成器函数，卸载模型并显示卸载进度和错误消息。 |
| `append` | 函数，将新的查询添加到聊天历史中，并返回更新后的聊天历史和消息列表。 |
| `stream` | 生成器函数，处理连续的聊天交互，返回更新后的聊天历史和消息列表。 |
| `WebChatModel.stream_chat` | 内部方法，处理聊天交互的流式生成。 |

请注意，`WebChatModel`类依赖于其他类和模块，如`ChatModel`、`Manager`、`Role`、`PEFT_METHODS`等，这些依赖未在表格中详细描述。此外，`WebChatModel`类使用了一些外部库，如`json`、`os`、`numpy`、`typing`等，以及可能的`gradio`库，这取决于`is_gradio_available()`的结果。

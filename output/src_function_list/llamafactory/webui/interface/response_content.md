以下是给定Python脚本中函数和类的名称及其功能的Markdown表格形式：

| 功能 | 函数/类名称 |
| --- | --- |
| 初始化引擎，设置演示模式和纯文本聊天选项 | `Engine(demo_mode, pure_chat)` |
| 创建用户界面，包括顶部、训练、评估预测、聊天和（非演示模式下）导出选项 | `create_ui(demo_mode)` |
| 返回一个Gradio Blocks实例，用于演示模式下的Web应用 | `create_web_demo()` |
| 启动用户界面，根据环境变量设置是否分享和服务器名称 | `run_web_ui()` |
| 启动演示模式下的Web应用，功能与`run_web_ui()`类似 | `run_web_demo()` |

请注意，这里没有单独的类，只有函数。`Engine`是一个类的实例，用于管理UI元素和逻辑。`gr.Blocks`和`gr.Dropdown`是Gradio库中的类，用于创建用户界面元素。

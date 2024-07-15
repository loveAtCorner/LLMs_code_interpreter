以下是您提供的Python脚本中函数和类的名称，以及它们的功能。我将以Markdown表格的形式呈现这些信息：

| 类/函数名称 | 功能 |
| --- | --- |
| `create_chat_box` | 创建聊天窗口的函数，传入`engine`参数并返回聊天窗口、消息和相关元素的元组。 |
| `create_infer_tab` | 创建推理选项卡的函数，传入`engine`参数并返回一个包含各种组件的字典。 |
| `gradio.components.Component` | Gradio库中的组件类，用于创建用户界面元素。 |
| `gradio.engine.Engine` | Gradio库中的引擎类，用于处理用户输入和模型推理。 |
| `gr.Row` | Gradio库中的行组件，用于在用户界面中水平排列元素。 |
| `gr.Dropdown` | Gradio库中的下拉菜单组件，用户可以选择其中的选项。 |
| `gr.Button` | Gradio库中的按钮组件，用户可以点击触发事件。 |
| `gr.Textbox` | Gradio库中的文本框组件，用户可以输入文本。 |
| `gr.Column` | Gradio库中的列组件，用于在用户界面中垂直排列元素。 |

请注意，`gradio.components.Component`和`gradio.engine.Engine`是类，而其他名称是函数或类的方法。这个脚本主要使用Gradio库来构建一个用户界面，用户可以在这个界面上选择模型推理的后端和数据类型，加载和卸载模型，以及与聊天机器人进行交互。

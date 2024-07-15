| 类/函数名 | 功能 |
| --- | --- |
| `ToolUtils` | 抽象基类，定义了工具实用工具类的接口，包括获取函数插槽、格式化工具和提取工具的方法 |
| `DefaultToolUtils` | `ToolUtils` 的子类，实现默认的工具提示和工具提取逻辑 |
| `get_function_slots` | 返回默认的函数插槽模板 |
| `tool_formatter` | 根据给定的工具列表生成工具提示文本 |
| `tool_extractor` | 从用户输入中提取工具名称和参数 |
| `GLM4ToolUtils` | `ToolUtils` 的子类，实现针对 ChatGLM 的工具提示和工具提取逻辑 |
| `get_function_slots` | 返回 GLM4 特定的函数插槽模板 |
| `tool_formatter` | 根据给定的工具列表生成 GLM4 特定的工具提示文本 |
| `tool_extractor` | 从用户输入中提取工具名称和参数，针对 GLM4 的格式要求 |

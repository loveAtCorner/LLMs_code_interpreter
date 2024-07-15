| 函数/类名 | 功能 |
| --- | --- |
| `EvalTemplate` | 一个数据类，用于存储评估模板的系统、选项和答案。包含一个私有方法 `_parse_example` 用于处理示例数据，以及一个公共方法 `format_example` 用于格式化目标数据。 |
| `_parse_example` | 私有方法，接收一个字典作为参数，根据 `CHOICES` 中的选项格式化输入数据，并返回格式化后的提示和响应。 |
| `format_example` | 公共方法，接收目标数据、支持集、主题名称作为参数，生成包含角色和内容的对话消息列表。 |
| `eval_templates` | 字典，存储不同名称的 `EvalTemplate` 实例。 |
| `_register_eval_template` | 私有方法，用于注册新的评估模板到 `eval_templates` 字典中。 |
| `get_eval_template` | 公共方法，根据名称从 `eval_templates` 中获取 `EvalTemplate` 实例，如果不存在则抛出异常。 |
| `_register_eval_template("en")` | 注册英文评估模板。 |
| `_register_eval_template("zh")` | 注册中文评估模板。 |

以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述。这些信息以Markdown表格的形式呈现：

| 类/函数名称 | 功能描述 |
| --- | --- |
| `_gradient_checkpointing_enable` | 为`PreTrainedModel`启用梯度检查点。检查模型是否支持梯度检查点，然后设置相关功能。 |
| `_fp32_forward_post_hook` | 模块后处理钩子，将模型输出转换为float32。 |
| `prepare_model_for_training` | 为模型训练做准备，包括处理层归一化、启用梯度检查点和处理语言模型头输出。 |

请注意，这个脚本中没有定义类，只有三个函数。`PreTrainedModel`和`ModelArguments`是函数参数中的类型注解，它们代表了在实际应用中可能使用的类。

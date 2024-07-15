以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 功能 | 函数/类名 |
| --- | --- |
| 获取日志记录器 | `get_logger(__name__)` |
| 配置注意力实现 | `configure_attn_implementation(config: "PretrainedConfig", model_args: "ModelArguments", is_trainable: bool) -> None` |
| 根据配置设置注意力实现，针对Gemma-2和InternLM2模型 |
| 检查torch和FlashAttention-2的可用性 |
| 打印注意力实现 | `print_attn_implementation(config: "PretrainedConfig") -> None` |
| 显示当前配置使用的注意力实现类型 |

函数`configure_attn_implementation`的主要功能是根据模型类型（Gemma-2或InternLM2）和用户提供的模型参数（model_args）来配置注意力实现。它会检查torch和FlashAttention-2库的可用性，并根据配置设置相应的注意力实现。

函数`print_attn_implementation`用于打印配置中使用的注意力实现类型，这有助于用户了解模型在训练和推理过程中使用的注意力机制。

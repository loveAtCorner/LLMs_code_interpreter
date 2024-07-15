以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能描述。这些信息以Markdown表格的形式呈现：

| 类/函数名称 | 功能描述 |
| --- | --- |
| `patch_tokenizer` | 修复tokenizer的_pad方法，使其与`PreTrainedTokenizerBase`兼容。 |
| `patch_config` | 配置模型配置，包括计算类型、注意力实现、ROPE、LongLORA、量化、Moe、视觉模型、打包和缓存设置。 |
| `patch_model` | 修复模型的generate方法，添加值头，调整嵌入层大小，配置视觉输入，为训练做准备，添加Z3叶模块，以及打印注意力实现。 |
| `patch_valuehead_model` | 为`AutoModelForCausalLMWithValueHead`添加方法，如tie_weights、get_input_embeddings、get_output_embeddings和create_or_update_model_card。 |

请注意，这个脚本中没有定义任何类，只有四个函数。这些函数主要用于在加载预训练模型后对其进行一些自定义配置和修复。

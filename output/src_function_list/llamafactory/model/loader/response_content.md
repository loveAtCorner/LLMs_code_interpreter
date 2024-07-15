以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能描述。这些信息以Markdown表格的形式呈现：

| 类/函数名称 | 功能描述 |
| --- | --- |
| `TokenizerModule` | 一个字典类型，包含`tokenizer`（一个`PreTrainedTokenizer`实例）和`processor`（一个可选的`ProcessorMixin`实例） |
| `_get_init_kwargs` | 返回一个字典，包含初始化模型、分词器等所需的关键字参数 |
| `load_tokenizer` | 加载分词器，并根据模型参数进行一些处理，如添加特殊令牌和处理视觉输入 |
| `load_config` | 加载模型配置 |
| `load_model` | 根据给定参数加载和初始化模型，包括处理模型混合深度、视觉输入、训练从头开始、添加价值头等功能 |

请注意，这个脚本中没有定义任何类，只有函数。此外，`load_model`函数中涉及的类（如`AutoTokenizer`、`AutoConfig`、`AutoModelForCausalLM`等）是Hugging Face Transformers库中的类，它们的功能不在这个脚本的范围内。

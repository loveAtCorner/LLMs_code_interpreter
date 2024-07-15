以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 功能 | 函数/类名 |
| --- | --- |
| 获取Unsloth模型的配置参数 | `_get_unsloth_kwargs` |
| 加载Unsloth预训练模型 | `load_unsloth_pretrained_model` |
| 获取Unsloth模型的PEFT版本 | `get_unsloth_peft_model` |
| 加载Unsloth预训练的PEFT模型 | `load_unsloth_peft_model` |

接下来是每个函数的详细描述：

1. **`_get_unsloth_kwargs(config: "PretrainedConfig", model_name_or_path: str, model_args: "ModelArguments") -> Dict[str, Any]`:**
   - 该函数用于获取Unsloth模型的配置参数，这些参数将用于加载预训练模型或PEFT模型。
   - 输入参数：
     - `config`: 预训练模型的配置对象。
     - `model_name_or_path`: 预训练模型的名称或路径。
     - `model_args`: 包含模型参数的ModelArguments对象。
   - 返回值：包含Unsloth模型配置的字典。

2. **`load_unsloth_pretrained_model(config: "PretrainedConfig", model_args: "ModelArguments") -> Optional["PreTrainedModel"]`:**
   - 该函数用于加载Unsloth预训练模型。
   - 输入参数：
     - `config`: 预训练模型的配置对象。
     - `model_args`: 包含模型参数的ModelArguments对象。
   - 返回值：加载成功的Unsloth模型实例，如果模型类型不被Unsloth支持，则返回`None`。

3. **`get_unsloth_peft_model(model: "PreTrainedModel", model_args: "ModelArguments", peft_kwargs: Dict[str, Any]) -> "PreTrainedModel"`:**
   - 该函数用于获取给定模型的PEFT（部分前向传播）版本。
   - 输入参数：
     - `model`: 预训练的Transformer模型实例。
     - `model_args`: 包含模型参数的ModelArguments对象。
     - `peft_kwargs`: PEFT模型的配置参数字典。
   - 返回值：PEFT版本的模型实例。

4. **`load_unsloth_peft_model(config: "PretrainedConfig", model_args: "ModelArguments", is_trainable: bool) -> "PreTrainedModel"`:**
   - 该函数用于加载Unsloth预训练的PEFT模型。
   - 输入参数：
     - `config`: 预训练模型的配置对象。
     - `model_args`: 包含模型参数的ModelArguments对象。
     - `is_trainable`: 表示模型是否可训练的布尔值。
   - 返回值：加载成功的Unsloth PEFT模型实例，如果模型类型不被Unsloth支持，将抛出ValueError异常。如果模型不可训练，将转换为推理模式。

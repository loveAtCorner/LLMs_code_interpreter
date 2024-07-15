|函数/类名称| 功能|
|---|---|
|`load_mod_pretrained_model`| 加载预训练的MoD模型。接受关键字参数并返回一个`PreTrainedModel`实例。|
|`convert_pretrained_model_to_mod`| 将预训练模型转换为MoD模型。接受一个`PreTrainedModel`实例、一个`PretrainedConfig`实例和一个`ModelArguments`实例作为参数，然后应用MoD技术，将模型转换为MoD模型，并根据`ModelArguments`中的`compute_dtype`设置数据类型，最后返回转换后的`PreTrainedModel`实例。|

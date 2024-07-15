|函数/类名称| 功能|
|---|---|
|`DummyOptimizer`| 一个简单的优化器类，用于模拟优化器的行为，但不执行任何真正的梯度更新。|
|`create_modelcard_and_push`| 创建模型卡片并将其推送到Hugging Face Hub。|
|`create_ref_model`| 创建参考模型，根据`finetuning_args`中的参数从预训练模型或自定义模型加载。|
|`create_reward_model`| 创建奖励模型，根据`finetuning_args`中的参数从预训练模型或API加载。|
|`_get_decay_parameter_names`| 获取模型中所有需要衰减的参数名称，不包括所有层标准化层的偏置。|
|`_create_galore_optimizer`| 创建使用Galore优化器的优化器，支持不同类型的Galore优化器（如AdamW、Adafactor等）。|
|`_create_loraplus_optimizer`| 创建使用LoRA+优化器的优化器，支持LORA+的特定学习率配置。|
|`_create_badam_optimizer`| 创建使用BAdam优化器的优化器，支持不同模式的BAdam（如基于层的更新和基于比例的更新）。|
|`create_custom_optimzer`| 创建自定义优化器，根据`finetuning_args`中的参数选择Galore、LoRA+或BAdam。|
|`create_custom_scheduler`| 创建自定义学习率调度器，根据`training_args`中的参数配置。|
|`get_batch_logps`| 计算给定logits和labels的对数概率，用于计算损失。|

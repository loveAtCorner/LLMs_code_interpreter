|函数/类名| 功能|
|---|---|
|CustomPPOTrainer| 继承自PPOTrainer和Trainer的类，用于训练带有PPO算法的模型|
|| `__init__`| 初始化方法，设置模型参数、训练参数、回调、模型、奖励模型、参考模型、分词器、处理器、数据集、数据集处理器|
|| `ppo_train`| 训练方法，执行PPO训练过程|
|| `create_optimizer`| 创建优化器的方法|
|| `create_scheduler`| 创建学习率调度器的方法|
|| `get_inputs`| 获取输入序列的方法，用于生成响应|
|| `get_rewards`| 计算奖励的方法，根据输入和响应计算模型的奖励|
|| `batched_forward_pass`| 批量前向传播方法，用于计算对数概率和价值|
|| `save_model`| 保存模型的方法，将模型保存到指定目录|
|PPOConfig| PPO配置类，包含PPO训练的超参数|
|PPODecorators| 包含空设备缓存装饰器的类|
|AverageMeter| 平均值计数器类，用于计算平均损失和奖励|
|get_logger| 获取日志记录器的函数|
|count_parameters| 计算模型参数数量的函数|
|get_current_device| 获取当前设备的函数|
|get_logits_processor| 获取logits处理器的函数|
|unwrap_model_for_generation| 用于解包模型以进行生成的函数|
|dump_layernorm| 备份模型中LayerNorm层参数的函数|
|restore_layernorm| 恢复模型中LayerNorm层参数的函数|
|FixValueHeadModelCallback| 固定值头模型回调，用于PPO训练|
|SaveProcessorCallback| 保存处理器回调，用于保存处理器到检查点|
|remove_dummy_checkpoint| 移除占位符检查点的函数|
|logprobs_from_logits| 从logits计算对数概率的函数|
|replace_model| 用于替换模型组件的函数|
|get_rewards_from_server| 从服务器获取奖励的函数|

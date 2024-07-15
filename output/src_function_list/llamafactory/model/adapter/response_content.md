|函数/类名称| 功能|
|---|---|
|get_logger| 获取日志记录器|
|_setup_full_tuning| 设置全量微调，将模型参数分为可训练和不可训练，可训练参数根据配置转换为float32|
|_setup_freeze_tuning| 设置冻结微调，根据配置冻结部分模型层，可训练参数根据配置转换为float32|
|_setup_lora_tuning| 设置LoRA微调，加载或创建LoRA适配器，根据配置设置LoRA参数，可能包括DoRA模式|
|init_adapter| 初始化微调，根据微调类型调用相应的微调设置函数，处理量化和半精度训练选项|

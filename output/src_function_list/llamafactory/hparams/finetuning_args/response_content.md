|函数/类名| 功能|
|---|---|
|FreezeArguments| 定义了用于冻结部分参数微调的参数，如可训练层的数量和模块名称。|
|LoraArguments| 定义了LoRA微调相关的参数，如LoRA层的α因子、丢弃率、内在维度、目标模块等。|
|RLHFArguments| 定义了RLHF（基于偏好学习的强化学习）训练相关的参数，如偏好损失、DPO损失类型、PPO优化参数等。|
|GaloreArguments| 定义了GaLore（梯度低秩投影）训练相关的参数，如应用的模块、秩、更新间隔等。|
|BAdamArgument| 定义了BAdam优化器的参数，如使用模式、更新策略、更新比例等。|
|FinetuningArguments| 继承了上述所有类，定义了整个微调过程的参数，包括微调类型、训练阶段、是否使用BF16等，并进行了一些参数的初始化和有效性检查。|

|函数/类名| 功能|
|---|---|
|CustomDPOTrainer| 继承自DPOTrainer的自定义训练器，用于偏好学习任务，支持多种损失函数和优化器。|
|__init__| 初始化方法，设置模型、参考模型、参数和超参数，处理模型的dropout，初始化Trainer并设置一些默认属性。|
|create_optimizer| 创建自定义优化器。|
|create_scheduler| 创建自定义学习率调度器。|
|odds_ratio_loss| 计算Odds Ratio Loss。|
|simpo_loss| 计算SIMPO Loss。|
|compute_preference_loss| 计算偏好损失，根据损失类型选择Odds Ratio Loss或SIMPO Loss。|
|concatenated_forward| 对输入批次进行前向传播，返回选择和拒绝的logits和logps。|
|compute_reference_log_probs| 计算参考模型的logits和logps。|
|get_batch_loss_metrics| 计算批次损失和相关指标，包括奖励、logps和logits的平均值，以及准确率和奖励差距。|
注意：这里没有列出所有Python内置类型和模块，如`torch`、`torch.nn.functional`等，它们是PyTorch库的一部分，用于处理张量和神经网络操作。

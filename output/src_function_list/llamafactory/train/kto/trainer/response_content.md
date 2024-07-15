以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能。这些信息已按照Markdown表格的形式呈现：

| 类/函数名 | 功能 |
| --- | --- |
| `CustomKTOTrainer` | 继承自`KTOTrainer`的自定义训练器，用于KTO（Knowledge Transfer Optimization）训练，包含自定义的优化器、学习率调度器和损失函数。 |
| `__init__` | 初始化方法，设置模型、参考模型、参数和回调。 |
| `create_optimizer` | 创建自定义优化器。 |
| `create_scheduler` | 创建自定义学习率调度器。 |
| `_get_train_sampler` | 获取训练数据采样器。 |
| `forward` | 前向传播，计算模型的对数概率。 |
| `concatenated_forward` | 计算模型的联合前向传播，用于KTO损失计算。 |
| `compute_reference_log_probs` | 计算参考模型的对数概率。 |
| `get_batch_loss_metrics` | 计算单个批次的损失和指标。 |
| `kto_loss` | 计算KTO损失，包括选择奖励、拒绝奖励和KL散度。 |
| `disable_dropout_in_model` | 禁用模型中的dropout层。 |
| `create_custom_optimzer` | 创建自定义优化器。 |
| `create_custom_scheduler` | 创建自定义学习率调度器。 |
| `get_batch_logps` | 计算对数概率和有效长度。 |
| `SaveProcessorCallback` | 保存处理器的回调。 |
| `BAdamCallback` | BAdam优化器回调。 |
| `clip_grad_norm_old_version` | 旧版的梯度裁剪函数。 |

请注意，这个表格仅包含主要的类和方法，以及它们的主要功能。对于更详细的实现细节，您需要查看每个函数或方法的源代码。

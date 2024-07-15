以下是您提供的Python脚本中函数和类的名称及其功能的Markdown表格形式：

| 类/函数名称 | 功能 |
| --- | --- |
| `run_ppo` | 主要入口函数，用于运行PPO训练过程，包括加载模型、数据集，创建Trainer并进行训练。 |
| `load_tokenizer` | 加载预训练模型的Tokenizer。 |
| `get_dataset` | 根据参数获取数据集。 |
| `load_model` | 加载模型，根据参数决定是否添加价值网络（value head）。 |
| `DataCollatorWithPadding` | 用于数据填充的类，来自Hugging Face的Transformers库。 |
| `create_ref_model` | 创建参考模型，用于PPO算法中的策略评估。 |
| `create_reward_model` | 创建奖励模型，用于计算策略的奖励。 |
| `CustomPPOTrainer` | 自定义的PPOTrainer类，继承自Hugging Face的Trainer。 |
| `ppo_train` | CustomPPOTrainer中的方法，执行PPO训练。 |
| `save_model` | CustomPPOTrainer中的方法，保存训练好的模型。 |
| `save_state` | CustomPPOTrainer中的方法，保存训练状态。 |
| `fix_valuehead_checkpoint` | 修复价值网络的检查点，确保其与模型其他部分同步。 |
| `plot_loss` | 可选地绘制训练过程中的损失和奖励曲线。 |

请注意，这个表格中的内容是基于代码的上下文和函数/类的名称来推断的，实际功能可能需要根据具体实现和文档进行详细理解。

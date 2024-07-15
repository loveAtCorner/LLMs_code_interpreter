以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能描述。这些内容已按照Markdown表格的形式呈现：

| 类/函数名 | 功能描述 |
| --- | --- |
| `CustomSeq2SeqTrainer` | 继承自`Seq2SeqTrainer`的自定义训练器，用于 finetuning 和预测任务。 |
| `__init__` | 初始化方法，设置 finetuning 参数、处理器和回调。 |
| `create_optimizer` | 创建自定义优化器。 |
| `create_scheduler` | 创建自定义学习率调度器。 |
| `prediction_step` | 在预测步骤中处理输入和生成的令牌。 |
| `_pad_tensors_to_target_len` | 将源张量填充到目标张量的长度。 |
| `save_predictions` | 保存预测结果到文件。 |

这个脚本定义了一个名为`CustomSeq2SeqTrainer`的类，它扩展了`Seq2SeqTrainer`，并添加了一些自定义功能，如使用自定义优化器、学习率调度器，以及在预测步骤中处理生成的令牌。此外，它还包含一些辅助方法，如填充张量和保存预测结果。

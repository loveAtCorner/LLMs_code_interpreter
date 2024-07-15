以下是您提供的Python脚本中函数和类的名称及其功能的Markdown表格形式：

| 类/函数 | 功能 |
| --- | --- |
| `compute_accuracy` | 计算预测结果的准确性。 |
| `eval_logit_processor` | 处理logits，返回每个样本预测的类别索引。 |
| `ComputeMetrics` | 一个数据类，用于计算评估指标（如ROUGE和BLEU）。 |
| `ComputeMetrics.__call__` | 实例化`ComputeMetrics`后，用于计算给定评估预测的指标。 |

这个脚本主要用于处理自然语言处理任务的评估指标计算，包括准确率、ROUGE和BLEU分数。它首先导入了必要的库，然后定义了一些条件导入，以确保在需要时使用特定的外部库。接下来，定义了计算准确率的函数`compute_accuracy`，以及处理logits的函数`eval_logit_processor`。

`ComputeMetrics`是一个数据类，它包含一个tokenizer属性。它的`__call__`方法用于计算给定评估预测的指标。这个方法首先将预测和标签转换为文本，然后使用jieba进行分词。接着，它计算ROUGE和BLEU分数，并将结果存储在一个字典中。最后，返回包含平均指标分数的字典。

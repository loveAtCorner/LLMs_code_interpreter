以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述。这些信息以Markdown表格的形式呈现：

| 功能名称 | 类型 | 描述 |
| --- | --- | --- |
| `run_dpo` | 函数 | 主要入口函数，用于运行DPO（Data Programming Optimization）训练过程，包括加载模型、数据处理、训练和评估。 |
| `PairwiseDataCollatorWithPadding` | 类 | 用于对序列对数据进行填充和编码的自定义数据处理器。 |
| `load_tokenizer` | 函数 | 加载预训练模型的分词器。 |
| `get_dataset` | 函数 | 根据给定参数加载数据集。 |
| `load_model` | 函数 | 加载预训练模型。 |
| `create_ref_model` | 函数 | 创建参考模型，用于DPO训练。 |
| `CustomDPOTrainer` | 类 | 自定义的Trainer类，用于执行DPO训练和评估。 |
| `plot_loss` | 函数 | 绘制训练过程中的损失曲线。 |
| `create_modelcard_and_push` | 函数 | 创建模型卡片并将其推送到指定位置。 |

请注意，这个脚本中没有直接定义类，但包含了一些类的实例（如`CustomDPOTrainer`）。此外，`run_dpo`函数是主要的入口点，它调用了其他辅助函数和类来执行整个训练流程。

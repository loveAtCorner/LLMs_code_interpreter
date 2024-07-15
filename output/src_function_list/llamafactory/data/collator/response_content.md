以下是您提供的Python脚本中函数和类的名称及其功能的Markdown表格形式：

| 类/函数 | 功能 |
| --- | --- |
| `prepare_4d_attention_mask` | 将2D注意力掩码转换为4D注意力掩码，用于自注意力计算。 |
| `SFTDataCollatorWith4DAttentionMask` | 数据收集器，用于在序列到序列任务中使用4D注意力掩码。 |
| `PairwiseDataCollatorWithPadding` | 数据收集器，用于处理成对输入（如选择和拒绝）的序列到序列任务。 |
| `KTODataCollatorWithPadding` | 数据收集器，用于处理KTO任务，其中包含目标序列和K-Loss序列。 |

类的详细功能如下：

1. `SFTDataCollatorWith4DAttentionMask`:
   - 继承自`DataCollatorForSeq2Seq`，用于处理序列到序列任务。
   - `block_diag_attn`：一个布尔值，决定是否使用块对角注意力。
   - `attn_implementation`：一个枚举值，指定注意力实现方式。
   - `compute_dtype`：一个`torch.dtype`，用于计算的类型。
   - `__call__`方法：根据输入的特征，处理注意力掩码并返回处理后的特征。

2. `PairwiseDataCollatorWithPadding`:
   - 用于处理成对输入（如选择和拒绝）的序列到序列任务的数据收集器。
   - `__call__`方法：将输入的特征按对合并，然后调用父类的`__call__`方法进行处理。

3. `KTODataCollatorWithPadding`:
   - 用于处理KTO任务（知识转移学习）的数据收集器，其中包含目标序列和K-Loss序列。
   - `__call__`方法：将目标序列和K-Loss序列分开处理，然后合并结果，添加额外的标签信息（如`kto_tags`）并返回处理后的特征。

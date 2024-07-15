|函数/类名| 功能|
|---|---|
|`run_sft`| 主要入口函数，用于运行序列到序列的 finetuning 过程|
|`SFTDataCollatorWith4DAttentionMask`| 数据集 collator，用于处理 4D 注意力掩码|
|`CustomSeq2SeqTrainer`| 自定义的 Seq2Seq 训练器，用于训练、评估和预测|
|`ComputeMetrics`| 计算指标类，用于评估和预测阶段|
|`compute_accuracy`| 计算准确率的辅助函数|
|`eval_logit_processor`| 评估阶段的 logits 处理函数|
|`get_logits_processor`| 获取 logits 处理器的函数|
|`get_dataset`| 获取数据集的函数|
|`split_dataset`| 划分数据集的函数|
|`load_model`| 加载模型的函数|
|`load_tokenizer`| 加载 tokenizer 的函数|
|`create_modelcard_and_push`| 创建并推送 modelcard 的函数|
|`plot_loss`| 绘制损失曲线的函数|

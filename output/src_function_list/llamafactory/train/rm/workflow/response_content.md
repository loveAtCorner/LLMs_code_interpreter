|函数/类名称| 功能|
|---|---|
|`run_rm`| 主要入口函数，用于运行模型的训练、评估和预测过程|
|`PairwiseDataCollatorWithPadding`| 数据处理类，用于对数据进行填充和对齐|
|`get_dataset`| 获取数据集|
|`load_model`| 加载模型|
|`load_tokenizer`| 加载分词器|
|`compute_accuracy`| 计算准确率的评估指标|
|`PairwiseTrainer`| 训练器类，负责模型的训练、评估和预测|
|`fix_valuehead_checkpoint`| 保存模型时修复值头的回调函数|
|`plot_loss`| 绘制训练和评估损失的函数|
|`create_modelcard_and_push`| 创建模型卡片并推送到仓库的函数|

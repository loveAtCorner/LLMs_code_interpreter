|函数/类名称| 功能|
|---|---|
|`run_pt`| 主要入口函数，用于运行预训练任务|
|`load_tokenizer`| 加载预训练模型的tokenizer|
|`get_dataset`| 根据参数获取数据集|
|`load_model`| 加载预训练模型并根据参数进行微调|
|`DataCollatorForLanguageModeling`| 由Hugging Face的Transformers库提供，用于数据预处理|
|`CustomTrainer`| 自定义的Trainer类，继承自Hugging Face的Trainer，用于训练和评估模型|
|`plot_loss`| 可选的绘图函数，用于绘制训练和验证损失|
|`create_modelcard_and_push`| 生成模型卡片并将其推送到指定位置|

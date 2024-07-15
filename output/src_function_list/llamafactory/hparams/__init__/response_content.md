|函数/类名称| 功能|
|---|---|
|DataArguments| 数据相关的参数类，用于处理数据路径、数据预处理等选项。|
|EvaluationArguments| 评估相关的参数类，用于设置评估任务的参数，如评估数据路径、评估指标等。|
|FinetuningArguments| 微调相关的参数类，用于设置模型微调时的参数，如微调数据路径、微调策略等。|
|GeneratingArguments| 生成相关的参数类，用于设置文本生成任务的参数，如生成长度、温度等。|
|ModelArguments| 模型相关的参数类，用于设置模型的选择、加载、保存等选项。|
|get_eval_args| 获取评估参数的函数，从命令行参数中解析并返回 EvaluationArguments 对象。|
|get_infer_args| 获取推理参数的函数，从命令行参数中解析并返回相关参数对象（具体类型未在代码中明确，但可能是 ModelArguments 或 GeneratingArguments）。|
|get_train_args| 获取训练参数的函数，从命令行参数中解析并返回 TrainArguments 对象（未在代码中定义，但根据函数名推测应是训练相关的参数类）。|

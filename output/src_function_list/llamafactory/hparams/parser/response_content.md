|函数/类名称| 功能|
|---|---|
|`get_logger`| 获取日志记录器|
|`check_dependencies`| 检查依赖项是否安装|
|`_set_transformers_logging`| 设置Transformers库的日志级别和默认处理器|
|`_verify_model_args`| 验证模型参数是否与训练方法兼容|
|`_check_extra_dependencies`| 检查额外的库依赖是否安装|
|`_parse_args`| 解析命令行参数|
|`_parse_train_args`| 解析用于训练的参数|
|`_parse_infer_args`| 解析用于推理的参数|
|`_parse_eval_args`| 解析用于评估的参数|
|`get_train_args`| 获取训练所需的参数并进行验证|
|`get_infer_args`| 获取推理所需的参数并进行验证|
|`get_eval_args`| 获取评估所需的参数并进行验证|
|`logging`| Python标准库中的日志模块|
|`os`| Python标准库中的操作系统接口模块|
|`sys`| Python标准库中的系统信息模块|
|`torch`| PyTorch深度学习库|
|`transformers`| Hugging Face的Transformers库|
|`HfArgumentParser`| Hugging Face的命令行参数解析器|
|`Seq2SeqTrainingArguments`| Hugging Face的序列到序列训练参数类|
|`ParallelMode`| Hugging Face的训练并行模式枚举|
|`require_version`| Hugging Face的库版本检查函数|
|`get_last_checkpoint`| 获取训练目录中最后一个检查点文件的路径|
|`is_deepspeed_zero3_enabled`| 检查是否使用了DeepSpeed ZeRO-3|
|`is_torch_bf16_gpu_available`| 检查GPU是否支持bfloat16数据类型|
|`ModelArguments`| 模型参数类|
|`DataArguments`| 数据参数类|
|`EvaluationArguments`| 评估参数类|
|`FinetuningArguments`| 微调参数类|
|`GeneratingArguments`| 生成参数类|
|`_TRAIN_ARGS`| 训练参数类的列表|
|`_TRAIN_CLS`| 训练参数类的元组类型|
|`_INFER_ARGS`| 推理参数类的列表|
|`_INFER_CLS`| 推理参数类的元组类型|
|`_EVAL_ARGS`| 评估参数类的列表|
|`_EVAL_CLS`| 评估参数类的元组类型|

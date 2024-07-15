|函数/类名| 功能|
|---|---|
|ModelArguments| 一个数据类，用于存储模型相关的参数，如模型名称、适配器路径、缓存目录等。|
|__post_init__| 初始化方法，设置一些默认属性并进行一些验证，如检查`split_special_tokens`和`use_fast_tokenizer`的兼容性，以及`visual_inputs`和`use_unsloth`的兼容性。|
|to_dict| 将数据类实例转换为字典。|
|copyfrom| 创建一个新的`ModelArguments`实例，基于旧的实例并更新给定的参数。|

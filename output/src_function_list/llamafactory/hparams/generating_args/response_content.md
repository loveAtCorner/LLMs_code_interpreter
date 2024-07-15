|函数/类| 功能|
|---|---|
|`GeneratingArguments`| 一个数据类，用于存储生成文本时的参数，如采样方式、温度、top-p等。|
|`to_dict`| 将`GeneratingArguments`对象转换为字典，根据`max_new_tokens`的值决定保留`max_length`还是`max_new_tokens`字段。|

以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 功能| 函数/类名|
|---|---|
|获取日志记录器| `get_logger(__name__)`|
|对一对示例进行编码，生成输入ID和标签| `_encode_pairwise_example(prompt, response, system, tools, template, tokenizer, processor, data_args)`|
|检查prompt和response的长度，根据数据参数进行截断|
|根据模板对消息进行编码|
|处理图像相关的输入，如图像序列长度和token type IDs|
|生成源序列长度和目标序列长度|
|组合输入ID和标签|
|对一对数据集进行预处理，生成模型输入| `preprocess_pairwise_dataset(examples, template, tokenizer, processor, data_args)`|
|遍历示例，调用 `_encode_pairwise_example` 函数处理每个示例|
|根据处理器处理图像相关的输入|
|返回包含模型输入的字典|
|打印一对数据集的示例| `print_pairwise_dataset_example(example, tokenizer)`|
|从输入ID中过滤出有效的标签（非忽略索引）|
|打印输入ID、输入文本、标签ID和标签文本|

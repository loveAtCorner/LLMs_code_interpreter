以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

|名称| 类型| 功能|
|---|---|---|
|AverageMeter| 类| 用于计算平均值的工具类，支持累加和平均值的更新|
|check_dependencies| 函数| 检查依赖版本，确保满足最低要求|
|count_parameters| 函数| 计算模型参数的总数和可训练参数的总数|
|get_current_device| 函数| 获取当前使用的设备（CPU、GPU、NPU或XPU）|
|get_device_count| 函数| 获取可用的设备数量（GPU、NPU或XPU）|
|get_logits_processor| 函数| 创建一个处理无穷大和NaN值的LogitsProcessorList对象|
|has_tokenized_data| 函数| 检查给定路径是否包含分词数据|
|infer_optim_dtype| 函数| 根据模型数据类型推断优化器数据类型|
|is_gpu_or_npu_available| 函数| 检查是否有GPU或NPU可用|
|skip_check_imports| 函数| 禁用或恢复检查导入的动态模块功能|
|torch_gc| 函数| 执行垃圾回收并清空缓存（GPU、NPU、XPU或MPS）|
|try_download_model_from_ms| 函数| 尝试从ModelScope下载模型，如果未找到或禁用，则返回给定的模型路径|
|use_modelscope| 函数| 检查是否使用ModelScope hub来下载模型|

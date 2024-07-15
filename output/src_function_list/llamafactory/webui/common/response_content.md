|函数/类名| 功能|
|---|---|
|`get_save_dir`| 根据给定的路径创建保存目录，处理路径中的空格和警告复杂的路径可能导致某些功能不可用。|
|`get_config_path`| 返回默认缓存目录下用户配置文件的路径。|
|`load_config`| 从用户配置文件中加载配置信息。|
|`save_config`| 保存配置信息到用户配置文件，包括语言、最后使用的模型和模型路径。|
|`get_model_path`| 根据模型名称获取模型的路径，优先使用用户配置中的路径，然后是默认路径，如果使用ModelScope且有ModelScope路径，则使用ModelScope路径。|
|`get_prefix`| 返回模型名称中的前缀。|
|`get_model_info`| 获取模型的路径、模板和是否为视觉模型。|
|`get_template`| 根据模型名称返回模型的默认模板。|
|`get_visual`| 判断模型是否为视觉模型。|
|`list_checkpoints`| 列出给定模型和微调类型的检查点，支持多选或单选。|
|`load_dataset_info`| 从给定目录加载数据集信息，如果目录为"ONLINE"，则返回空字典。|
|`list_datasets`| 列出数据集，根据训练阶段筛选是否使用配对数据。|

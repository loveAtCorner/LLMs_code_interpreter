|函数/类名| 功能|
|---|---|
|`DatasetAttr`| 数据集属性类，包含数据集加载方式、名称、格式化方式等属性，并提供设置属性的方法。|
|`__init__`| DatasetAttr类的初始化方法，设置默认属性值。|
|`__repr__`| 返回DatasetAttr对象的字符串表示，即其dataset_name属性。|
|`set_attr`| 根据键和提供的字典设置DatasetAttr对象的属性，如果字典中没有该键，则使用默认值。|
|`get_dataset_list`| 根据DataArguments对象获取数据集列表。从命令行参数或配置文件中读取数据集名称，根据数据集信息设置DatasetAttr对象的属性，并将它们添加到列表中。|

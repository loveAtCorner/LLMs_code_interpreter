|函数/类名称| 功能|
|---|---|
|`find_all_linear_modules`| 找到模型中所有非禁用的线性模块（不包括嵌入层）的名称，根据`freeze_vision_tower`决定是否排除视觉塔模块。返回这些模块的名称列表。|
|`find_expanded_modules`| 根据目标模块列表和可训练层数，找到模型中应应用特定策略（如LORA）的模块。返回这些模块的名称列表。|
|`register_autoclass`| 注册配置、模型和分词器类为自动类，以便在`Auto`系列中使用。|

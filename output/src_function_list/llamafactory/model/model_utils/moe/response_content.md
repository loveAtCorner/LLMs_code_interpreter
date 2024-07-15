以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 功能名称 | 类型 | 描述 |
| --- | --- | --- |
| `_set_z3_leaf_modules` | 函数 | 设置DeepSpeed Zero3的叶子模块，用于模型的零阶段优化。 |
| `add_z3_leaf_module` | 函数 | 根据模型类型添加DeepSpeed Zero3的叶子模块。 |
| `configure_moe` | 函数 | 配置模型的多专家（Moe）参数，如辅助损失系数和输出路由器日志几率。 |

这个脚本主要处理与DeepSpeed Zero3集成相关的功能，特别是针对某些特定模型（如dbrx、jamba、jetmoe、mixtral和qwen2_moe）的设置。它还包含了配置多专家（Moe）模型的参数，这些参数可能影响模型的训练和性能。

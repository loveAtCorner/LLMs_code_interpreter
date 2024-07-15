|函数/类名| 功能|
|---|---|
|LlamaAttention| 一个自定义的注意力模块，实现自旋位置编码和基于查询、键值的注意力机制。|
|LlamaFlashAttention2| 一个自定义的快速注意力模块，基于LlamaAttention，可能用于加速计算。|
|LlamaSdpaAttention| 一个自定义的SDPA注意力模块，可能用于优化计算效率，不支持输出注意力权重。|
|llama_attention_forward| LlamaAttention类的前向传播方法，计算注意力分数并应用注意力权重到值向量上。|
|llama_flash_attention_2_forward| LlamaFlashAttention2类的前向传播方法，类似于LlamaAttention，但可能使用了不同的注意力计算方法。|
|llama_sdpa_attention_forward| LlamaSdpaAttention类的前向传播方法，计算注意力分数并应用注意力权重到值向量上，不支持输出注意力权重。|
|_apply_llama_patch| 应用补丁，将LlamaAttention、LlamaFlashAttention2和LlamaSdpaAttention的forward方法替换为自定义实现。|
|configure_longlora| 配置LongLora模型，根据模型参数决定是否启用shift短注意力并设置相关配置。|

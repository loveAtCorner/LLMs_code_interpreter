|函数/类名| 功能|
|---|---|
|`LlavaMultiModalProjectorForYiVL`| 一个用于多模态投影的PyTorch模块，专为YiVL模型设计。包含线性层、层归一化和激活函数，用于将视觉特征转换为文本隐藏状态。|
|`LlavaMultiModalProjectorForYiVLForVLLM`| 一个子类，用于VLLM模型的多模态投影器。与`LlavaMultiModalProjectorForYiVL`类似，但允许自定义视觉和文本隐藏大小以及投影隐藏层的激活函数。|
|`autocast_projector_dtype`| 一个函数，用于在模型前向传播后自动将多模态投影器的输出转换为指定的计算数据类型。|
|`configure_visual_model`| 一个配置函数，用于设置LLava模型的隐藏大小，并在检测到Yi-VL模型时，将多模态投影器类替换为`LlavaMultiModalProjectorForYiVL`。|

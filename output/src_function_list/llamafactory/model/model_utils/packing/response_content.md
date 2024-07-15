以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 功能| 函数/类名|
|---|---|
|获取注意力掩码中序列长度| `get_seqlens_in_batch`|
|从注意力掩码中获取未填充数据| `get_unpad_data`|
|为特定模型类型应用块对角注意力补丁| `patch_for_block_diag_attn`|
|配置序列打包参数| `configure_packing`|

接下来是每个函数的详细描述：

1. **`get_seqlens_in_batch`**:
   - 功能：计算输入注意力掩码中每个样本的序列长度。
   - 参数：
     - `attention_mask`: 形状为 `(batch_size, sequence_length)` 的张量，表示输入序列的注意力掩码。
   - 返回值：形状为 `(batch_size)` 的张量，表示每个样本的序列长度。

2. **`get_unpad_data`**:
   - 功能：从注意力掩码中提取未填充数据，包括索引、累积序列长度和最大序列长度。
   - 参数：
     - `attention_mask`: 形状为 `(batch_size, sequence_length)` 的张量，表示输入序列的注意力掩码。
   - 返回值：一个元组，包含：
     - 索引张量：形状为 `(total_tokens)`，表示未填充数据的索引。
     - 累积序列长度张量：形状为 `(batch_size + 1)`，表示累积的序列长度。
     - 最大序列长度：整数，表示输入序列中的最大序列长度。

3. **`patch_for_block_diag_attn`**:
   - 功能：根据给定的模型类型，将`get_unpad_data`函数应用于特定的模型类，以实现块对角注意力。
   - 参数：
     - `model_type`: 字符串，表示要应用补丁的模型类型（如 "cohere"、"falcon" 等）。

4. **`configure_packing`**:
   - 功能：根据模型参数配置序列打包，包括是否启用块对角注意力。
   - 参数：
     - `config`: `PretrainedConfig` 类型，表示预训练模型的配置。
     - `model_args`: `ModelArguments` 类型，表示模型的命令行参数。
     - `is_trainable`: 布尔值，表示模型是否可训练。
   - 功能：
     - 如果模型支持块对角注意力且训练时启用，调用 `patch_for_block_diag_attn` 函数并输出日志。
     - 否则，如果模型不支持块对角注意力或训练不可用，抛出错误。

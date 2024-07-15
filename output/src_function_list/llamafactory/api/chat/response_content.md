|函数/类名| 功能|
|---|---|
|`get_logger`| 获取日志记录器|
|`ROLE_MAPPING`| 角色映射字典|
|`_process_request`| 处理请求，将输入消息转换为字典格式，检查请求的正确性，并提取必要的信息|
|`_create_stream_chat_completion_chunk`| 创建聊天完成流响应块，包含指定的完成ID、模型、增量和可能的结束原因|
|`create_chat_completion_response`| 创建完整的聊天完成响应，处理请求，调用模型并返回完整的响应|
|`create_stream_chat_completion_response`| 创建流式聊天完成响应，处理请求，调用模型并生成响应块|
|`create_score_evaluation_response`| 创建评分评估响应，处理请求，调用模型并返回评分结果|

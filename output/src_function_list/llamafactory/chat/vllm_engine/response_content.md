|函数/类名| 功能|
|---|---|
|`VllmEngine`| VLLM引擎，基于BaseEngine的子类，用于与VLLM模型交互，支持文本生成和聊天功能。|
|| **构造函数**  
|| - `__init__`：初始化VllmEngine，加载配置、模型、tokenizer和处理器，设置参数。|
|| **方法**  
|| - `_generate`：生成文本的内部方法，处理输入消息、系统和工具，编码提示，生成文本。|
|| - `chat`：基于 `_generate` 的聊天方法，返回生成的响应列表。|
|| - `stream_chat`：基于 `_generate` 的流式聊天方法，返回生成文本的增量。|
|| - `get_scores`：未实现的方法，提示VLLM引擎不支持获取分数。|
  
  
|变量| 功能|
|---|---|
|`uuid`| 用于生成唯一请求ID的Python标准库。|
|`typing`| Python类型提示库，定义各种类型变量。|
|`logger`| 日志记录器，用于记录模块的调试和错误信息。|
|`BaseEngine`| 基础引擎类，VllmEngine的父类，提供通用的聊天引擎功能。|
|`Response`| 用于封装生成的响应，包含响应文本、长度、提示长度和结束原因。|
|`AsyncEngineArgs`| VLLM库中的异步引擎参数类。|
|`AsyncLLMEngine`| VLLM库中的异步LLM引擎类。|
|`RequestOutput`| VLLM库中的请求输出类，包含生成的文本和其他元数据。|
|`SamplingParams`| VLLM库中的采样参数类，用于定义生成文本时的参数。|
|`LoRARequest`| VLLM库中的LoRA请求类，用于与LoRA模型交互。|
|`ImagePixelData`| VLLM库中的图像像素数据类，用于处理图像输入。|
|`MultiModalData`| VLLM库中的多模态数据类，用于处理多模态输入。|
  
  
|常量| 功能|
|---|---|
|`QuantizationMethod`| 定义量化方法的枚举类。|

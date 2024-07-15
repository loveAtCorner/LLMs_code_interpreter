|函数/类名| 功能|
|---|---|
|HuggingfaceEngine| 一个基于Transformer模型的对话引擎，支持生成和评估模式。|
|| **构造函数**<br>`__init__`<br>初始化引擎，加载模型、tokenizer和配置。|
|| **方法**<br>`can_generate`<br>检查模型是否支持生成对话。|
|| **方法**<br>`_process_args`<br>处理输入参数，准备模型生成所需的输入。|
|| **方法**<br>`_chat`<br>在非流式模式下生成对话响应。|
|| **方法**<br>`_stream_chat`<br>在流式模式下生成对话响应。|
|| **方法**<br>`_get_scores`<br>评估给定输入的分数，适用于非自回归模型。|
|| **方法**<br>`chat`<br>异步执行非流式对话生成。|
|| **方法**<br>`stream_chat`<br>异步执行流式对话生成。|
|| **方法**<br>`get_scores`<br>异步执行评估，适用于非自回归模型。|

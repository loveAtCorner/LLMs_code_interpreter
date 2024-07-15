以下是您提供的Python脚本中函数和类的名称，以及它们的功能描述，按照Markdown表格的形式呈现：

| 功能 | 函数/类名 |
| --- | --- |
| 获取日志记录器 | `get_logger(__name__)` |
| 从给定路径加载价值头部参数 | `load_valuehead_params(path_or_repo_id: str, model_args: "ModelArguments") -> Dict[str, torch.Tensor]` |
| 从安全的文件中加载价值头部参数 | `safe_open(vhead_file, framework="pt", device="cpu")` |
| 准备价值头部模型，根据模型类型设置LM头和忽略保存的键 | `prepare_valuehead_model(model: "PreTrainedModel") -> None` |

请注意，`safe_open` 函数实际上是一个外部调用，不是直接在提供的代码中定义的。这个函数可能在`safetensors`模块中定义，用于安全地打开和处理文件。

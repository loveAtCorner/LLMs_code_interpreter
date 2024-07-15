以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能。这些信息已按照Markdown表格的形式呈现：

| 功能 | 函数/类名称 |
| --- | --- |
| 获取日志记录器 | `get_logger(__name__)` |
| 运行实验 | `run_exp(args: Optional[Dict[str, Any]] = None, callbacks: List["TrainerCallback"] = []) -> None` |
| 获取训练参数 | `get_train_args(args)` |
| 运行PT（基础微调） | `run_pt(model_args, data_args, training_args, finetuning_args, callbacks)` |
| 运行SFT（序列标签） | `run_sft(model_args, data_args, training_args, finetuning_args, generating_args, callbacks)` |
| 运行RM（检索增强） | `run_rm(model_args, data_args, training_args, finetuning_args, callbacks)` |
| 运行ppo（策略梯度） | `run_ppo(model_args, data_args, training_args, finetuning_args, generating_args, callbacks)` |
| 运行dpo（多样性优化） | `run_dpo(model_args, data_args, training_args, finetuning_args, callbacks)` |
| 运行kto（知识检索） | `run_kto(model_args, data_args, training_args, finetuning_args, callbacks)` |
| 导出模型 | `export_model(args: Optional[Dict[str, Any]] = None) -> None` |
| 获取推理参数 | `get_infer_args(args)` |
| 加载分词器 | `load_tokenizer(model_args)` |
| 加载模型 | `load_model(tokenizer, model_args, finetuning_args)` |
| 保存模型到预训练目录 | `model.save_pretrained()` |
| 将模型推送到Hugging Face Hub | `model.push_to_hub()` |
| 保存分词器 | `tokenizer.save_pretrained()` |
| 将分词器推送到Hugging Face Hub | `tokenizer.push_to_hub()` |
| 保存图像处理器 | `getattr(processor, "image_processor").save_pretrained()` |
| 将图像处理器推送到Hugging Face Hub | `getattr(processor, "image_processor").push_to_hub()` |

请注意，这个脚本主要涉及一个实验运行器（`run_exp`），一个模型导出器（`export_model`），以及一些用于不同微调任务的运行函数（如`run_pt`、`run_sft`等）。脚本还包含了加载模型、分词器和图像处理器，以及将它们保存到预训练目录或推送到Hugging Face Hub的方法。

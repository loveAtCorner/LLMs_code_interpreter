以下是您提供的Python脚本中所有函数和类的名称，以及它们的功能。这些信息以Markdown表格的形式呈现：

| 功能 | 函数/类名称 |
| --- | --- |
| 获取日志记录器 | `get_logger(__name__)` |
| 加载单个数据集 | `load_single_dataset(dataset_attr, model_args, data_args, training_args)` |
| 检查数据集是否已分词 | `has_tokenized_data(data_path)` |
| 从磁盘加载分词数据集 | `load_from_disk(data_path)` |
| 获取数据集列表 | `get_dataset_list(data_args)` |
| 从多个数据集中合并数据 | `merge_dataset(all_datasets, data_args, training_args)` |
| 获取预处理函数和打印函数 | `get_preprocess_and_print_func(data_args, training_args, stage, template, tokenizer, processor)` |
| 对数据集进行预处理 | `dataset.map(preprocess_func, batched=True, remove_columns=column_names, **kwargs)` |
| 获取模板和修复分词器 | `get_template_and_fix_tokenizer(tokenizer, data_args.template, data_args.tool_format)` |
| 获取整个数据集 | `get_dataset(model_args, data_args, training_args, stage, tokenizer, processor)` |

这个脚本主要涉及数据集的加载、合并、预处理和分词。它包含用于处理不同数据源（如本地文件、Hugging Face Hub、ModelScope Hub）的逻辑，以及处理不同训练阶段（如预训练、微调等）的数据集。此外，它还包含了预处理函数和模板处理，以确保数据集与模型的输入格式兼容。

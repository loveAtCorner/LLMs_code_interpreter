|函数/类名| 功能|
|---|---|
|abort_process| 终止进程及其子进程|
|can_quantize| 根据finetuning_type返回可选择的量化选项|
|can_quantize_to| 根据量化方法返回可选择的量化位宽|
|change_stage| 根据提供的训练阶段返回空列表和布尔值，布尔值表示是否为PyTorch阶段|
|check_json_schema| 验证JSON格式的工具列表|
|clean_cmd| 清理命令行参数，移除空值或False值|
|gen_cmd| 生成命令行字符串|
|save_cmd| 将命令行参数保存到文件|
|get_eval_results| 从结果文件中读取并格式化JSON数据|
|get_time| 获取当前时间戳|
|get_trainer_info| 从训练日志中获取运行信息，如进度和损失图|
|load_args| 从配置文件中加载参数|
|save_args| 将参数保存到配置文件|
|list_config_paths| 列出可用的配置文件选项|
|list_output_dirs| 列出包含训练结果的输出目录选项|
|create_ds_config| 创建预设的分布式训练配置文件|

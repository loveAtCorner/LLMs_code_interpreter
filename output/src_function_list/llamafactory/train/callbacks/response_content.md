|函数/类名| 功能|
|---|---|
|fix_valuehead_checkpoint| 修复带有值头的模型的检查点，将值头和解码器部分分别保存。|
|FixValueHeadModelCallback| 当训练器保存模型时，调用`fix_valuehead_checkpoint`来修复值头的保存。|
|SaveProcessorCallback| 训练结束后，保存处理器（如图像处理器）到输出目录。|
|PissaConvertCallback| 在训练开始和结束时，处理PiSSA适配器的初始化和转换。|
|LogCallback| 监控训练进度，记录日志并更新训练状态。|
|on_init_end| 检查并删除可能存在的旧的训练日志文件。|
|on_train_begin| 开始训练时，初始化计时器，创建线程池并设置日志记录。|
|on_train_end| 训练结束后，关闭线程池。|
|on_substep_end| 当子步骤结束时，检查是否需要停止训练（通过`self.aborted`标志）。|
|on_step_end| 当步骤结束时，检查是否需要停止训练（通过`self.aborted`标志）。|
|on_evaluate| 在评估阶段，关闭日志记录。|
|on_predict| 在预测阶段，关闭日志记录。|
|on_log| 记录和更新训练日志，包括损失、学习率等信息。|
|on_prediction_step| 在预测阶段，记录和更新预测进度。|

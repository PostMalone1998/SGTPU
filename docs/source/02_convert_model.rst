模型转换
============

从已有网络模型快速开始
------------------

从 https://github.com/sophgo/SGTPU-ModelZoo 获取SGTPU-ModelZoo源码，并按照主页介绍下载源模型，执行模型导航中的模型转换脚本来获取bmodel。


需要保留这一步产生包含compilation.bmodel的文件夹。


手动转换网络模型为bmodel
------------------

参考pytorch或onnx导出教程，从神经网络框架中导出静态网络模型(.pt或.onnx格式)。

从 https://github.com/sophgo/tpu-mlir/tree/sgtpuv8 获取TPU-MLIR源码，注意使用sgtpuv8分支，并按照主页介绍完成model_transform、run_calibration、model_deploy步骤，实现单步从神经网络模型到bmodel的转换。

需要保留这一步产生包含compilation.bmodel的文件夹。
SGTPU软件简介
============

提供算能开源芯片SGTPU配套软件程序，包括:

    1.神经网络模型编译器TPU-MLIR

    2.神经网络模型编译示例SGTPU-ModelZoo

    3.模型运行时库libsophon

    4.神经网络算子库SGTPU-KernelModule

    5.芯片仿真库SGTPU-Cmodel

目前支持SGTPUV8。

使用以上程序可实现将不同框架神经网络模型(pytorch、ONNX等)转换为在SGTPU上高效运行的二进制文件-bmodel，并使用模型运行时库调用SGTPU来执行bmodel，以实现SGTPU对神经网络模型的加速。


其中TPU-MLIR提供了一套完整的工具链用于转换不同框架神经网络模型，SGTPU-ModelZoo提供了一些预训练好的开源模型和执行TPU-MLIR的编译脚本示例，libsophon提供bmodel运行时库、驱动以及bmodel测试运行程序。


SGTPU-KernelModule提供基于SGTPU指令编写的神经网络算子动态库，SGTPU-Cmodel提供在x86机器上模拟SGTPU指令行为的芯片仿真动态库。神经网络算子动态库与芯片仿真动态库作为TPU-MLIR和libsophon的依赖库使用。

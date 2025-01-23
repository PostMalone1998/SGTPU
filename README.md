# SGTPU

## 介绍

提供算能开源芯片SGTPU配套软件程序，包括:
    1.神经网络模型编译器TPU-MLIR
    2.神经网络模型编译示例SGTPU-ModelZoo
    3.模型运行时库libsophon
    4.神经网络算子库SGTPU-KernelModule
    5.芯片仿真库SGTPU-Cmodel

目前支持SGTPUV8。

## 子模块链接

| 链接 | 功能说明 |
|:-----|:--------|
|[TPU-MLIR](https://github.com/sophgo/tpu-mlir/tree/sgtpuv8)|用于将开源神经网络框架模型(pytorch、ONNX等)转换为SGTPU可运行的格式:bmodel|
|[SGTPU-ModelZoo](https://github.com/sophgo/SGTPU-ModelZoo)|提供预训练好的开源框架模型和对应使用TPU-MLIR的编译脚本示例|
|[libsophon](https://github.com/sophgo/libsophon/tree/SGTPUV8)|bmodel的驱动和运行时库|
|[SGTPU-KernelModule](https://github.com/sophgo/tpu-mlir/blob/sgtpuv8/third_party/nntoolchain/lib/libsgtpuv8_kernel_module.so)|基于SGTPU指令编写的神经算子动态库|
|[SGTPU-Cmodel](https://github.com/sophgo/tpu-mlir/blob/sgtpuv8/third_party/nntoolchain/lib/libcmodel_sgtpuv8.so)|在x86机器上模拟SGTPU指令行为的芯片仿真动态库|

## 文档指南

[SGTPU软件指南.pdf](docs/build/SGTPU软件指南.pdf)
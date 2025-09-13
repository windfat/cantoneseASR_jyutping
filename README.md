# cantoneseASR_jyutping
Cantonese Automatic Speech Recognition using Jyutping

This training is based on the facebook's fairseq open source code, https://github.com/facebookresearch/fairseq/blob/main/examples/wav2vec/README.md, the training will be run on a Ubuntu 20.04 PC with the RTX3080 GPU card. 

The OS and hardware environment:

OS: Ubuntu 20.04

GPU: NVIDIA GeForce RTX 3080

Nvidia Driver Version: 560.28.03

nvcc: NVIDIA (R) Cuda compiler driver
Copyright (c) 2005-2022 NVIDIA Corporation
Built on Wed_Sep_21_10:33:58_PDT_2022
Cuda compilation tools, release 11.8, V11.8.89
Build cuda_11.8.r11.8/compiler.31833905_0

libcudnn version is 8.6.0

To start training or test, we need to setup the python environment first. Please refer to setup.txt

After setup, if you want to try the model without doing training, please jump to test section

=============================================================

Before training the model, we need to prepare training data:
=============================================================

To try training based on Librispeech dataset, please visit training_on_Librispeech.txt



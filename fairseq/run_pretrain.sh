export HYDRA_FULL_ERROR=1
fairseq-hydra-train \
task.data=$PWD/manifest \
distributed_training.distributed_world_size=1 \
--config-dir ./examples/wav2vec/config/pretraining \
--config-name wav2vec2_base_librispeech \


#checkpoint.restore_file=./outputs/2025-04-24/23-45-14/checkpoints/checkpoint_last.pt \

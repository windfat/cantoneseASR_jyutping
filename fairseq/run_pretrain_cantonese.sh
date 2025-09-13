export HYDRA_FULL_ERROR=1
fairseq-hydra-train \
task.data=$PWD/manifest_cantonese \
checkpoint.restore_file=$PWD/reference_checkpoint/checkpoint_best.pt \
distributed_training.distributed_world_size=1 \
--config-dir ./examples/wav2vec/config/pretraining \
--config-name wav2vec2_base_librispeech \


#checkpoint.restore_file=$PWD/outputs/2025-07-01/23-14-42/checkpoints/checkpoint_best.pt \

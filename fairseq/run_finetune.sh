fairseq-hydra-train \
distributed_training.distributed_world_size=1 \
task.data=$PWD/manifest \
model.w2v_path=$PWD/outputs/2025-06-18/22-12-37/checkpoints/checkpoint_best.pt \
--config-dir $PWD/examples/wav2vec/config/finetuning \
--config-name base_100h

#checkpoint.restore_file=./outputs/2025-04-24/23-45-14/checkpoints/checkpoint_last.pt \

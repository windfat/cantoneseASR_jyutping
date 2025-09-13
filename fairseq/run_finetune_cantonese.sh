export HYDRA_FULL_ERROR=1
export PORT=1

fairseq-hydra-train \
    distributed_training.distributed_world_size=1 \
    task.data=$PWD/manifest_cantonese \
    checkpoint.restore_file=/media/home/mango/test_fairseq/fairseq/outputs/2025-07-07/23-21-17/checkpoints/checkpoint_last.pt \
    model.w2v_path=$PWD/outputs/2025-07-01/23-14-42/checkpoints/checkpoint_best.pt \
    --config-dir $PWD/examples/wav2vec/config/finetuning \
    --config-name base_100h

#    checkpoint.restore_file=/media/home/apple/projects/fairseq/outputs/finetune_cantonese/2025-05-22/23-27-13/checkpoints/checkpoint_last.pt  \

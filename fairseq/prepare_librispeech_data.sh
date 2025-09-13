export ext=flac
export valid=0.01
python examples/wav2vec/wav2vec_manifest.py ../dataset/LibriSpeech/train-clean-100 --dest ./manifest --ext $ext --valid-percent $valid

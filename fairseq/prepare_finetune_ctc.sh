export split=train
python libri_labels.py ./manifest/train.tsv --output-dir ./manifest --output-name $split

export split=valid
python libri_labels.py ./manifest/valid.tsv --output-dir ./manifest --output-name $split

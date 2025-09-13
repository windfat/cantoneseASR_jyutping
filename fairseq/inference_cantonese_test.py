
import torch
import torchaudio
from omegaconf import DictConfig
from fairseq import tasks, checkpoint_utils
from fairseq.data.audio.audio_utils import convert_waveform


def build_generator(args):
        
        print(args)
        w2l_decoder = getattr(args, "w2l_decoder", None)
        if w2l_decoder == "viterbi":
            print("using viterbi")
            from examples.speech_recognition.w2l_decoder import W2lViterbiDecoder
            return W2lViterbiDecoder(args, task.target_dictionary)
            
        elif w2l_decoder == "kenlm":
            from examples.speech_recognition.w2l_decoder import W2lKenLMDecoder

            return W2lKenLMDecoder(args, task.target_dictionary)
        elif w2l_decoder == "fairseqlm":
            from examples.speech_recognition.w2l_decoder import W2lFairseqLMDecoder

            return W2lFairseqLMDecoder(args, task.target_dictionary)
        else:
            print(
                "only flashlight decoders with (viterbi, kenlm, fairseqlm) options are supported at the moment"
            )



def load_model_and_task(model_path, data_dir):
    # Configure task for audio finetuning
    cfg = DictConfig({
        'task': 'audio_finetuning',
        'data': data_dir,
        'labels': "ltr"        
    })
    
    # Setup task and load model
    task = tasks.setup_task(cfg)
    
    print(task)
    models, _ = checkpoint_utils.load_model_ensemble([model_path], task=task)
    model = models[0].eval()
    return model, task

def transcribe(models, task, audio_path):
    # Load audio and convert to 16kHz mono
    waveform, sample_rate = torchaudio.load(audio_path, format="flac")
    waveform = torchaudio.functional.resample(waveform, sample_rate, 16000)
    waveform = waveform.mean(dim=0, keepdim=True)  # Convert to mono

    # Add batch dimension and normalize
    print("Waveform shape:", waveform.shape)  # Should be [1, 37280]

    # Generator config for CTC
    generator_cfg = {
        "beam": 5,
        "criterion": "ctc",
        "w2l_decoder": "viterbi",
        "max_len_a": 0,
        "max_len_b": 200,
        "labels": "ltr",
    }

    generator = build_generator(DictConfig(generator_cfg))

    # Inference
    sample = {"net_input": {"source": waveform, "padding_mask": None}}
    hypo = task.inference_step(generator, [models], sample)
    return task.target_dictionary.string(hypo[0][0]["tokens"], "letter", "ignore")



# Usage
models, task = load_model_and_task(  
    model_path = "./reference_checkpoint/cantonese/fine-tuned/checkpoint_best.pt",
    data_dir = "./manifest_cantonese"  # Should contain dict.ltr.txt   
)


print(transcribe(models, task, "./test_samples/common_voice_zh-HK_24020802.flac"))









from os.path import splitext
from pydub import AudioSegment

def wav_to_flac(wav_path):
    flac_path = "%s.flac" % splitext(wav_path)[0]
    song = AudioSegment.from_wav(wav_path)
    song.export(flac_path, format = "flac")

def mp3_to_flac(mp3_path):
    flac_path = "%s.flac" % splitext(mp3_path)[0]
    song = AudioSegment.from_mp3(mp3_path)
    song = song.set_frame_rate(16000)
    song.export(flac_path, format = "flac")
    #print(flac_path)

#mp3_to_flac("test_split3.mp3")

src_dir = '<folder path to the dataset mp3 files>'
input_file = '<folder to the dataset>/metadata_full.csv'
dest_dir = './output'

with open(input_file, 'r') as file:
    for line in file:
       line = file.readline()
       src_file = src_dir + line.split("|")[0]
       print(src_file)
       mp3_to_flac(src_file)




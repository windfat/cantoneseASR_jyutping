
import argparse
import os
import soundfile
from os.path import splitext
from pydub import AudioSegment
import pycantonese as pc

#output name can be train of valid
output_name = 'valid'


data_dir = '../dataset/cv-corpus-21.0-2025-03-14-zh-HK/cv-corpus-21.0-2025-03-14/zh-HK/clips'

dataset_dir = '../dataset/cv-corpus-21.0-2025-03-14-zh-HK/cv-corpus-21.0-2025-03-14/zh-HK'

#the input file must be the in the format of <audio file path and name>  <labels>
input_file = dataset_dir + "/" + "other.tsv"

out_tsv_file = "./" + output_name + ".tsv"
out_ltr_file = "./" + output_name + ".ltr"
out_wrd_file = "./" + output_name + ".wrd"
output_dir = './'
original_format = "mp3"
target_format = "flac"


def wav_to_flac(wav_path):
    flac_path = "%s.flac" % splitext(wav_path)[0]
    song = AudioSegment.from_wav(wav_path)
    song.export(flac_path, format = "flac")

def mp3_to_flac(mp3_path):
    flac_path = "%s.flac" % splitext(mp3_path)[0]
    song = AudioSegment.from_mp3(mp3_path)
    song = song.set_frame_rate(16000)
    song.export(flac_path, format = "flac")
    
def chineseCharToJyutping(tmpStr):   
    outStr = "";
    for jj in range(len(tmpStr)):
       cchar = tmpStr[jj];
       #print(cchar)
       result = pc.characters_to_jyutping(cchar);
       #print(result[0][1])
       #print(type(result[0][1]))
       if ( type(result[0][1]) != type(None) ):
          outStr = outStr + result[0][1] + " ";
    return  outStr     



with open(input_file, 'r') as file, open(
        os.path.join(output_dir, output_name + ".ltr"), "w"
    ) as ltr_out, open(
        os.path.join(output_dir, output_name + ".wrd"), "w"
    ) as wrd_out, open(
        os.path.join(output_dir, output_name + ".tsv"), "w"
    ) as tsv_out:
      print(data_dir, file=tsv_out)
      next(file)
      for line in file:
       #line = file.readline()  
       org_src_file = line.split()[1] + '.' + original_format 
       org_src_file = org_src_file.split('.')[0] + '.' + original_format
       src_file =  org_src_file.split('.')[0] + '.' + target_format
       fname_tmp = data_dir + "/" + org_src_file
       mp3_to_flac(fname_tmp)  
       #src_file = line.split()[1] + '.' + target_format
       #fname = data_dir + "/" + src_file
       fname = data_dir + "/" + src_file
       #print(fname)
       frames = soundfile.info(fname).frames
       #print(frames)
       print(src_file + "	" + str(frames), file=tsv_out)
       label_line = line.split()[3]    #tsv files contains the label of speech at 4 th parameters
       out_labels = chineseCharToJyutping(label_line)
       count = len(out_labels.split())
       testline = ""
       ltr = ""
       for x in range(0, count):
          #print(line.split()[x].upper())
          testline = testline + out_labels.split()[x].upper() + ' '
          word_len = len(out_labels.split()[x])
          word = out_labels.split()[x].upper()
          for y in range(0, word_len):             
             ltr = ltr + word[y] + ' '
          ltr = ltr + "| "   
          #ltr = ltr + line.split()[x].upper() + "|"
       print(testline, file=wrd_out)  
       #print(ltr)
       print(ltr, file=ltr_out) 
       #mp3_to_flac(src_file)




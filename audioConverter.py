import os
import sys
from pydub import AudioSegment


def convert_ogg_to_wav(orig_song):
    song = AudioSegment.from_ogg(orig_song)
    song.export(orig_song.replace('.ogg', '.wav'), format="wav")


if __name__ == '__main__':
    convert_ogg_to_wav()

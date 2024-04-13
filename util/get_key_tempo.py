import librosa
import numpy as np


def get_bpm(song_path):
    y, sr = librosa.load(song_path)

    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    return '\nTEMPO (estimation): {:.2f}'.format(tempo)


def get_key_signature(song_path):
    note_names = ['A', 'A#', 'B', 'C', 'C#', 'D', 'E', 'F', 'F#', 'G', 'G#', 'A']

    key_list = []

    if song_path.endswith('.mp3'):
        y, sr = librosa.load(song_path, sr=None)

        chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
        chroma_vals = np.sum(chroma, axis=1)
        most_common_pc = np.argmax(chroma_vals)
        key = note_names[most_common_pc]

        return '\nKey (estimate): ' + key

    return "\nerror"

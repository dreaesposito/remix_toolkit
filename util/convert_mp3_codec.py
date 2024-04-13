from pydub import AudioSegment


def convert_file(path_to_file, output_path):

    output_path = 'C:/Users/dreat/OneDrive/Desktop/mp3Files'

    AudioSegment.converter = 'C:/Users/dreat/OneDrive/Desktop/ffmpeg-6.0'

    print("songfile :  " + path_to_file)
    print("output path:  " + output_path)
    sound = AudioSegment.from_wav(path_to_file)
    #sound.export('sound.mp3', format='mp3')

    print("sound" + sound)

    return

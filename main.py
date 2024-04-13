import PySimpleGUI as simG

from util import get_mp3

simG.theme('DarkBlue 3')
main_font = ("Arial", 8)
PROGRAM_NAME = 'Vocal Extractor v1.0'
DOWNLOAD = 'Download Songs'
EXTRACT = 'Extract Vocals'
GREY = 'grey31'
OLIVE = 'OliveDrab4'

log_window = simG.Multiline(size=(70, 10), write_only=True, reroute_cprint=True, key='-OUT-',
                            expand_x=True, expand_y=True)
LOG = [simG.Text('Console log'), log_window]


# ---------Vocal extractor window
sub_button2 = simG.Button('Submit', key='-sub2-', button_color=OLIVE)

layout_2 = [[simG.Text('Choose a song', size=(15, 1)), simG.InputText(), simG.FileBrowse()],
            [simG.Text('Output destination', size=(15, 1)), simG.InputText(), simG.FolderBrowse()],
            [sub_button2, simG.Button(DOWNLOAD, key='-key2-', font=main_font, button_color=GREY)]]

# --------- Yt download window
sub_button1 = simG.Button('Submit', key='-sub1-', button_color=OLIVE)

layout_1 = [[simG.Text('Destination folder', size=(15, 1)), simG.InputText(), simG.FolderBrowse()],
            [simG.Text('Enter the video link', size=(15, 1)), simG.InputText()],
            [sub_button1, simG.Button(EXTRACT, key='-key1-', font=main_font, button_color=GREY)],
            [simG.Checkbox('Get key and BPM', default=True, key="-IN-", enable_events=True)]]

# Create the Window
layout_list = [[simG.Column(layout_1, key='-COL1-'),
               simG.Column(layout_2, key='-COL2-', visible=False)], LOG,
               [simG.Button('Close', size=(10, 1), button_color='IndianRed4')]]

window = simG.Window(PROGRAM_NAME, layout_list, finalize=True)
path = simG.FolderBrowse().InitialFolder


layout = 1  # current visible layout
# Event Loop 
while True:
    event, values = window.read()

    if event == simG.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
        break

    # check for submit button
    if event == '-sub1-':  # download video option
        folder_path = values[0]
        ytLink = values[1]
        try:
            simG.cprint(get_mp3.create(values[1], values[0], values['-IN-']))

        except Exception as e:
            simG.cprint(e)
    elif event == '-sub2-':  # extract option
        simG.cprint('button sub 2 for vocal extractor')

    # window cycle
    if event == '-key1-':
        window[f'-COL{layout}-'].update(visible=False)
        layout += 1
        window[f'-COL{layout}-'].update(visible=True)

    elif event == '-key2-':
        window[f'-COL{layout}-'].update(visible=False)
        layout -= 1
        window[f'-COL{layout}-'].update(visible=True)

window.Close()

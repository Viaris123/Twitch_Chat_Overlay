import PySimpleGUI as sg
import keyboard
from twitch import TwitchChatStream

sg.theme('DarkBlack')


def do_nothing():
    """ This function doing nothing)))"""
    pass


def start_stream_chat():
    """ Start stream chat in separated window. """

    layout = [[sg.Multiline(size=(150, 150), key='-IN-',
                            auto_refresh=True, font=('Cooper Black', 16))]]

    window = sg.Window('', layout, size=(300, 300), alpha_channel=0.5, no_titlebar=True,
                       keep_on_top=True, force_toplevel=True, finalize=True, modal=True)

    keyboard.add_hotkey('ctrl+o', do_nothing)

    with TwitchChatStream(username='viaris123',
                          oauth='oauth:wmuzovp81n3hepr096qmvwybx80lxb',
                          verbose=True) as chatstream:
        chatstream.send_chat_message("First message!")
        while True:
            rcv = chatstream.twitch_receive_messages()  # receiving here
            if rcv:
                window['-IN-'].print(rcv)
            event, value = window.read(timeout=100)

            if event == sg.WINDOW_CLOSED or keyboard.is_pressed('ctrl+o'):
                break
        window.close()


def main():
    layout = [[sg.Button('Start'), sg.Button('Exit')],
              [sg.Text('Press Ctrl+o to close second window.')]]

    window = sg.Window('First window', layout, size=(100, 100), finalize=True)
    while True:
        event, value = window.read(timeout=100)
        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            break
        if event == 'Start':
            start_stream_chat()
    window.close()


if __name__ == '__main__':
    main()

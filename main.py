"""PySimpleGui and keyboard modules are necessary!"""
import PySimpleGUI as sg
import keyboard
from twitch import TwitchChatStream


sg.theme('DarkBlack')


def do_nothing():
    """ This function doing nothing))) """
    pass


def start_stream_chat():
    """ Start stream chat in separated window. """

    layout = [[sg.Multiline(size=(500, 500), key='-IN-',
                            auto_refresh=True, font=('Cooper Black', 12))]]

    window = sg.Window('', layout, size=(300, 300), alpha_channel=0.5, no_titlebar=True,
                       keep_on_top=True, force_toplevel=True, finalize=True, modal=True)

    keyboard.add_hotkey('ctrl+o', do_nothing)

    # Connecting to stream with user credentials. Warning! Translation must be started!
    with TwitchChatStream(username='viaris123',
                          oauth='oauth:wmuzovp81n3hepr096qmvwybx80lxb',
                          verbose=True) as chatstream:
        chatstream.send_chat_message("Let's Go!")
        while True:
            rcv = chatstream.twitch_receive_messages()  # receiving here
            if rcv:
                window['-IN-'].print(f"{rcv[0]['username']} : {rcv[0]['message']}")
            event, value = window.read(timeout=100)

            if event == sg.WINDOW_CLOSED or keyboard.is_pressed('ctrl+o'):
                break
        window.close()


def main():
    layout = [[sg.Text('Press Ctrl+o to close second window.')],
              [sg.Text('Warning! Translation must be started!')],
              [sg.Button('Start'), sg.Button('Exit')]]

    window = sg.Window('Twitch Overlay Chat', layout, size=(250, 250), finalize=True)
    while True:
        event, value = window.read(timeout=100)
        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            break
        if event == 'Start':
            start_stream_chat()
    window.close()


if __name__ == '__main__':
    main()

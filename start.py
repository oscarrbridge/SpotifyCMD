from spotify import *
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def setup():
    user_input = 0
    current_vol = 0
    current_device = sp.devices()
    options = {1: "Show devices",
               2: "Turn volume up",
               3: "Turn volume down",
               4: "Skip track",
               5: "Previous track",
               6: "Pause / play",
               7: "Shuffle"}
    try:
        current_vol = current_device["devices"][0]["volume_percent"]

    except:
        print("There are no devices currently active! ")

    while True:
        try:
            while user_input not in options:

                for option in options:
                    print("{}: {}".format(option, options[option]))

                user_input = int(input("What option would you like to choose?"))

                print()

                current_device = sp.devices()

                if current_device["devices"][0]["is_active"] is True:

                    if user_input == 1:
                        show_devices(current_device)
                    if user_input == 2:
                        current_vol = current_device["devices"][0]["volume_percent"]
                        current_vol = turn_vol_up(current_vol, current_device)
                    if user_input == 3:
                        current_vol = current_device["devices"][0]["volume_percent"]
                        current_vol = turn_vol_down(current_vol, current_device)
                    if user_input == 4:
                        skip_track()
                    if user_input == 5:
                        previous_track()
                    if user_input == 6:
                        play_track()
                    if user_input == 7:
                        shuffle_songs()

                    user_input = 0
                    sp.volume(current_vol)

                else:
                    print("There is no currently active device!")

        except ValueError:
            print("That is not a valid option! ")

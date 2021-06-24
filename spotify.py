from re import L
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state,user-modify-playback-state,user-read-playback-position"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope=scope))

VOL_INCREASE = 25
VOL_DECREASE = 25


def show_devices(current_device):
    print("Current device name: {}".format(current_device["devices"][0]["name"]))
    print("Current song: {}".format(sp.currently_playing()['item']['name']))


def turn_vol_up(volume, current_device):
    if current_device["devices"][0]["volume_percent"] - VOL_DECREASE >= 100:
        print("Volume is already max!")
        return 0

    else:
        volume = volume + VOL_DECREASE
        print("The volume is at {}%".format(volume))
        return volume


def turn_vol_down(volume, current_device):
    if current_device["devices"][0]["volume_percent"] - VOL_DECREASE <= 0:
        print("Volume is already min!")
        return 0

    else:
        volume = volume - VOL_DECREASE
        print("The volume is at {}%".format(volume))
        return volume


def skip_track():
    sp.next_track()
    currently_playing = sp.currently_playing()['item']['name']
    print(currently_playing)


def previous_track():
    sp.previous_track()
    currently_playing = sp.currently_playing()['item']['name']
    print(currently_playing)


def play_track():
    playing_state = sp.currently_playing()['is_playing']

    if playing_state is False:
        sp.start_playback()

    else:
        sp.pause_playback()


def shuffle_songs():
    sp.shuffle()


def setup():
    user_input = 0
    current_device = sp.devices()
    try:
        current_vol = current_device["devices"][0]["volume_percent"]

    except:
        print("There are no devices currently active! ")

    while True:
        try:
            while user_input not in [1, 2, 3, 4, 5, 6, 7, 8]:
                user_input = int(input("What option would you like to choose?"))

                print(sp.currently_playing()['item'])

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


if __name__ == "__main__":
    setup()

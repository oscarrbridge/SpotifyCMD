from re import L
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_SECRET_ID",
                                               redirect_uri="http://localhost:8888/callback",
                                               scope=scope))

VOL_INCREASE = 25
VOL_DECREASE = 25


def show_devices(current_device):
    print("Current device name: {}".format(current_device["devices"][0]["name"]))


def turn_vol_up(volume, current_device):
    if current_device["devices"][0]["volume_percent"] - VOL_DECREASE <= 0:
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


def previous_track():
    sp.previous_track()


def play_track():
    try:
        sp.start_playback()

    except:
        sp.pause_playback()


def setup():
    user_input = 0
    current_device = sp.devices()
    current_vol = current_device["devices"][0]["volume_percent"]

    while user_input not in [1, 2, 3, 4, 5, 6, 7]:
        user_input = int(input("What option would you like to choose?"))

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

            user_input = 0
            sp.volume(current_vol)

        else:
            print("There is no currently active device!")


if __name__ == "__main__":
    setup()

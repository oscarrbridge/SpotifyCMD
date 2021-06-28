import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from secret import *

scope = "user-read-playback-state,user-modify-playback-state,user-read-playback-position"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://localhost:8888/callback",
                                               scope=scope))

VOL_INCREASE = 25
VOL_DECREASE = 25

SLEEP_TIME = 0.75


def show_devices(current_device):
    print("Current device name: {}".format(current_device["devices"][0]["name"]))
    print("Current song: {}".format(sp.currently_playing()['item']['name']))
    input("Enter anything to go back ")


def turn_vol_up(volume, current_device):
    if current_device["devices"][0]["volume_percent"] - VOL_DECREASE >= 100:
        print("Volume is already max!")
        time.sleep(SLEEP_TIME)
        return 0

    else:
        volume = volume + VOL_DECREASE
        print("The volume is at {}%".format(volume))
        time.sleep(SLEEP_TIME)
        return volume


def turn_vol_down(volume, current_device):
    if current_device["devices"][0]["volume_percent"] - VOL_DECREASE <= 0:
        print("Volume is already min!")
        time.sleep(SLEEP_TIME)
        return 0

    else:
        volume = volume - VOL_DECREASE
        print("The volume is at {}%".format(volume))
        time.sleep(SLEEP_TIME)
        return volume


def skip_track():
    sp.next_track()
    currently_playing = sp.currently_playing()['item']['name']
    current_artist = sp.currently_playing()['item']['album']['artists'][0]['name']
    print("The current song is: {} by {}".format(currently_playing, current_artist))
    option = input("Click 1 to go forward another song. ")
    if option == "1":
        skip_track()


def previous_track():
    sp.previous_track()
    currently_playing = sp.currently_playing()['item']['name']
    current_artist = sp.currently_playing()['item']['album']['artists'][0]['name']
    print("The current song is: {} by {}".format(currently_playing, current_artist))
    option = input("Click 1 to go back another song. ")
    if option == "1":
        previous_track()


def play_track():
    playing_state = sp.currently_playing()['is_playing']

    if playing_state is False:
        sp.start_playback()

    else:
        sp.pause_playback()


def shuffle_songs():
    sp.shuffle(False)

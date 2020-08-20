import time
from TikTokApi import TikTokApi
from playsound import *

api = TikTokApi()

USERNAME = "tiktok"


def get_follow():
    test = api.getUser(USERNAME)["userInfo"]["stats"]["followerCount"]
    return int(test)

def after():
    SOUNDDURATION = 0.2
    mp3File = ("heysisters.mp3")
    playsound(mp3File)
    time.sleep(SOUNDDURATION)
    print("New Follower")



followcopy = get_follow()
print("Followcopy :", followcopy)

while True:
    get_follows = get_follow()
    if get_follows > followcopy:
        loop = get_follows - followcopy
        for loops in range(loop):
            after()
        followcopy = get_follow()

    elif get_follows < followcopy:
        followcopy -= 1
        print("Lost a follower")
    time.sleep(1)

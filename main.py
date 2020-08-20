import time
from TikTokApi import TikTokApi

api = TikTokApi()

USERNAME = "tiktok"


def get_follow():
    test = api.getUser(USERNAME)["userInfo"]["stats"]["followerCount"]
    return int(test)

def after():
    # Place the code to run after a new follower comes here
    #For examples see the examples DIR
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

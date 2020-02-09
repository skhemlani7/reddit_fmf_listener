#TODO: Notifications
#   https://towardsdatascience.com/how-to-make-windows-10-toast-notifications-with-python-fb3c27ae45b9
#TODO: Run on startup
#   https://www.quora.com/How-do-I-run-a-Python-script-on-a-startup-on-Windows
#TODO: Use datetime to have script run once every hour after startup

#TODO: Move sample json to README
#Sample json file 
#{
#     'brands' : ['H&M', 'Uniqlo', 'Patagonia'],
#     'clothing_type' : ['oxford shirt', 'chino']
# }

import json
import praw

def main():
    with open("config.json") as json_file:
        with open("auth.json") as auth_file:
            config = json.load(json_file)
            auth = json.load(auth_file)
            # print(config["client_id"])

            reddit = praw.Reddit(client_id=config["client_id"], client_secret=config["client_secret"],
                            password=config["password"], user_agent=config["user_agent"],
                            username=config["username"])

            for submission in reddit.front.hot(limit=256):
                print(submission.score)
            # print(auth["access_token"])

if __name__ == "__main__":
    main()

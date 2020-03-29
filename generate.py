import json
import praw

def parse_reddit():
    with open("config.json") as json_file:
        config = json.load(json_file)
        result = []

        reddit = praw.Reddit(client_id=config["client_id"], client_secret=config["client_secret"],
                        password=config["password"], user_agent=config["user_agent"],
                        username=config["username"])
        subreddit = reddit.subreddit('frugalmalefashion')

        for submission in subreddit.hot(limit=50):
            if submission.stickied:
                continue
            for key in config['keys']:
                if key in submission.title.lower() and submission.title not in result:
                    result.append(submission.title)
        return result

if __name__ == "__main__":
    print(parse_reddit())

# Reddit_fmf_listener
Scrapes r/frugalmalefashion for deals filtered by user input. 
The script runs every time you turn on your computer and again once every hour after startup. 
Will only work for windows. If run on mac, the project will simply output to terminal. 

# Dependencies
- PRAW (pip install praw)
- win10toast (pip install win10toast)
- urllib3
- json
- requests
- time

# OAuth 2 and connecting to Reddit API 
- Create a reddit account.
- Go to https://www.reddit.com/prefs/apps and click "are you a developer? Create an app...".
- Add in a name of your choosing, leave description and about url blank. Select script.
    - Add your selected name to config.json with the key "app_name".
- Type in http://www.google.com for redirect uri. Don't judge me.
    - Add secret to config.json with key "client_secret".
    - Add the id under the application's name to config.json with key "client_id".
- Add your Reddit username and password to config.json. Make sure to use keys "username" and "password".
- To verify that everything works as expected, 
    - Create the config file shown below 
    - Run authenticate.py. You should see an access token as output. This access token will be saved to auth.json. 

- Helpful links for this step: 
    - https://github.com/reddit-archive/reddit/wiki/API
    - https://github.com/reddit-archive/reddit/wiki/OAuth2
    - https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
    - https://www.youtube.com/watch?v=CPbvxxslDTU

# Config
- Create config.json with the following template:
```
{
    "app_name" : "The name you chose for your app",
    "user_agent" : "Python:app_name:v1.0.0 (by u/your_account_name)",
    "client_id" : "From Reddit OAuth",
    "client_secret" : "From Reddit OAuth",
    "username" : "Your Reddit username",
    "password" : "Your Reddit account password",
    "keys" : ["uniqlo", "patagonia", "oxford shirt", "chinos", "anything you're interested in"],
}
```
- No need to worry about caps or plurals when adding to keys.

# Running on startup
COMING SOON
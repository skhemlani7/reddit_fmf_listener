# Reddit_fmf_listener
Scrapes r/frugalmalefashion for deals within the past week filtered by item type and brand. 
The script runs every time you turn on your computer and again once every hour after startup. 

# OAuth 2 and connecting to Reddit API 
- Create a reddit account.
- Go to https://www.reddit.com/prefs/apps and click "are you a developer? Create an app...".
- Add in a name of your choosing, leave description and about url blank. Select script.
- Type in http://www.google.com for redirect uri. Don't judge me.
    - Add secret to config.json with key "client_secret".
    - Add the id under the application's name to config.json with key "client_id".
- Add your Reddit username and password to config.json. Make sure to use keys "username" and "password".
- Run authenticate.py to verify that everything works as expected. You should see an access token as output. 

- Helpful links for this step: 
    - https://github.com/reddit-archive/reddit/wiki/API
    - https://github.com/reddit-archive/reddit/wiki/OAuth2
    - https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example
    - https://www.youtube.com/watch?v=CPbvxxslDTU

# Running on startup

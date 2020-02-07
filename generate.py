#TODO: Notifications
#   https://towardsdatascience.com/how-to-make-windows-10-toast-notifications-with-python-fb3c27ae45b9
#TODO: Run on startup
#   https://www.quora.com/How-do-I-run-a-Python-script-on-a-startup-on-Windows
#TODO: Use datetime to have script run once every hour after startup

#Sample json file 
#{
#     'brands' : ['H&M', 'Uniqlo', 'Patagonia'],
#     'clothing_type' : ['oxford shirt', 'chino']
# }

import json

def main():
    with open("auth.json") as json_file:
        config = json.load(json_file)
    print(config)

if __name__ == "__main__":
    main()

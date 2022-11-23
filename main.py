import os
os.system("pip install -r requirements.txt")
import object3
#import helper functions for errors
import json
#import helper functions for magiceden
import magiceden
#import helper functions for monkeylabs
import monkelabs





def getConfig():
        configFile = open("config.json", 'r')
        return list(json.load(configFile).values())


#gets config
config = getConfig()

#if windows True, else False (mac, linux)
isWindows = True if os.name == 'nt' else False

#if mint on magiceden.io
if "magiceden.io" in config[0]:
    print("Found magiceden.io link")
    magiceden.mint(config, isWindows)
    
#if mint on monkeylabs.io
elif "monkelabs.io" in config[0]:
    print("Found monkelabs.io link")
    monkelabs.mint(config, isWindows)

#if platform not supported
else:
    print("Could not recognize link")


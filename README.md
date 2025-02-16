README

# SETUP AND DESCRIPTION
This script combines the use of 2 different APIs.
- streamlabs.io: This is used to get live stream alerts in real-time such as follows, donations, and subscriptions.
- litterbot API by natekspencer (https://github.com/natekspencer/pylitterbot/tree/main). We can use this to connect to the Whisker Feeder-Robot (https://www.litter-robot.com/feeder-robot.html) to dispense pet food.

By combining these API calls, we can dispense pet treats when someone follows, donates, or subscribes while live streaming.

<p align="center">
  <img src="https://raw.githubusercontent.com/aozgur360/twitch_auto_pet_feeder/main/example_twitch_cat_feeder.gif" alt="Demo of Auto Pet Feeder">
</p>

1) Input your streamlabs API token in the config.toml file.
2) Input your Feeder-Robot login username and password in the .env file.

Optional:
3) Configure a camera in front of the Feeder-Robot (example. Tapo C110 pet camera)
4) Add VLC source to connect to camera view in the streamlabs desktop app or OBS Studio

# RUNNING THE SCRIPT
Poetry is used to setup the environment and dependencies
    (poetry run py twitch_events_listener.py)

# ROBOT DETECTION
If multiple robots are detected, you can specify which one you would like to dispense the snack in twitch_events_listener.py

# STREAM SOURCE
This is configured for Twitch, but you can also run it easily for YouTube


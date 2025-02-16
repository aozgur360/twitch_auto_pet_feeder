import streamlabsio
import os
from logging import config

print('waiting for new events...')

# Set up logging for debugging
config.dictConfig(
    {
        "version": 1,
        "formatters": {
            "standard": {
                "format": "%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s"
            }
        },
        "handlers": {
            "stream": {
                "level": "DEBUG",
                "class": "logging.StreamHandler",
                "formatter": "standard",
            }
        },
        "loggers": {"streamlabsio.client": {"handlers": ["stream"], "level": "DEBUG"}},
    }
)

# Function to handle Twitch events


def on_twitch_event(event, data):
    if event == "follow":
        print(f"Received follow from {data.name}")
        os.system("python give_snack.py")  # Trigger snack-giving script
    elif event == "bits":
        print(f"{data.name} donated {data.amount} bits! With message: {data.message}")
        os.system("python give_snack.py")  # Trigger snack-giving script
    elif event == "donation":
        print(
            f"{data.name} donated {data.formatted_amount}! With message: {data.message}")
        os.system("python give_snack.py")  # Trigger snack-giving script
    elif event == "subscription":
        print(f"{data.name} subscribed to the channel!")
        os.system("python give_snack.py")  # Trigger snack-giving script

# Function to handle YouTube events


def on_youtube_event(event, data):
    print(f"YouTube Event: {event}: {data.attrs()}")

# Main function to set up the Twitch listener


def main():
    with streamlabsio.connect() as client:
        client.obs.on("streamlabs", on_twitch_event)
        client.obs.on("twitch_account", on_twitch_event)
        client.obs.on("youtube_account", on_youtube_event)

        # Keep the script running and listening for events
        client.sio.wait()


if __name__ == "__main__":
    main()

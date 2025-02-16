import asyncio
import nest_asyncio
import os
from pylitterbot import Account
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Apply the nest_asyncio patch
nest_asyncio.apply()

# Get username and password from environment variables
username = os.getenv("LITTERBOT_USERNAME")
password = os.getenv("LITTERBOT_PASSWORD")

if not username or not password:
    raise ValueError(
        "Please set LITTERBOT_USERNAME and LITTERBOT_PASSWORD environment variables")

# Define your async main function


async def main():
    # Create an account.
    account = Account()

    try:
        # Connect to the API and load robots.
        await account.connect(username=username, password=password, load_robots=True)

        # Print robots associated with account.
        print("Robots:")
        for index, robot in enumerate(account.robots):
            print(f"{index + 1}: {robot}")

        # Check if there are at least two robots
        if len(account.robots) >= 2:
            second_robot = account.robots[1]  # Index 1 is the second robot
            print(f"\nGiving snack to: {second_robot}")
            snack_given = await second_robot.give_snack()
            print(f"Snack given: {snack_given}")
        elif len(account.robots) == 1:
            first_robot = account.robots[0]  # Only one robot
            print(f"\nOnly one robot found. Giving snack to: {first_robot}")
            snack_given = await first_robot.give_snack()
            print(f"Snack given: {snack_given}")
        else:
            print("\nNo robots found in the account.")

    finally:
        # Disconnect from the API.
        await account.disconnect()

# Running the async function
if __name__ == "__main__":
    asyncio.run(main())

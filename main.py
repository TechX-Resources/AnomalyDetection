import os
from steam_web_api import Steam
from dotenv import load_dotenv, dotenv_values
load_dotenv()
KEY = os.getenv("STEAM_API_KEY")

steam = Steam(KEY)

user_id = input("Enter your Steam ID:")
user = steam.users.get_user_details(user_id)

print(user)
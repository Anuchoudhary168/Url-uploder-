#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "2754371"))
API_HASH = environ.get("API_HASH", "de419b65230116bb6c926198f74e34af")
BOT_TOKEN = environ.get("BOT_TOKEN", "7681794827:AAHe4t-sgkVrdBsIjxIvTZWEpoe9d_me1Ww")
OWNER = int(environ.get("OWNER", "6084025746"))
CREDIT = "bhura jaat"
AUTH_USER = os.environ.get('AUTH_USERS', '6084025746').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set

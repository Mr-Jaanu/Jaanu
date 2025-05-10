import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8197756021:AAEY4cmnK6BiwFgNs1peo4o3MjtvnOxHzOA")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26625764"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fd9b06421885c66f99587917f4127df1")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "5596521800"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://Jaanu:DKbcYBZnSsnnwPPN@jaanu.vbc65yl.mongodb.net/?retryWrites=true&w=majority&appName=Jaanu") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "MrJaanusavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', Flase))

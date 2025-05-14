import os

# Bot token from @botfather
BOT_TOKEN = os.environ.get("8081507527:AAHVRI2z4Ygx8ja9qLEz5RohPkqkC1jBma8")
# From my.telegram.org/
API_ID = int(os.environ.get("27623611", 0))
API_HASH = os.environ.get("4a326a928083750585c7f96408ced199")
# For /log cmd
OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "5180174682").split(" ")]
# No time limit for this users
AUTH_USERS = [int(i) for i in os.environ.get("AUTH_USERS", "5180174682").split(" ")]
# Time gap after each request (in seconds)
TIME_GAP = int(os.environ.get("TIME_GAP", "10"))
# Bot channel ID for ForceSub, don't forget to add bot in Bot Channel
UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", False)

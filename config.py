from os import environ


class Config(object):
    API_ID = int(environ.get("API_ID", 16743442))
    API_HASH = environ.get("API_HASH", "12bbd720f4097ba7713c5e40a11dfd2a")
    BOT_TOKEN = environ.get("BOT_TOKEN", "6221284663:AAGop_cKtr03r4Tv8k7NeDpV4lb0X1uLGck")
    

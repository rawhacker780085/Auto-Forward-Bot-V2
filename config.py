from os import environ 

class Config:
    API_ID = environ.get("API_ID", "28372387")
    API_HASH = environ.get("API_HASH", "11edc85521fb2d8f75e751bb284507e1")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7393831140:AAGVsIXYXx3_UquE3LpmmLpH3VZqhfw5vcw") 
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://rahulkumar200001002:j0W8JF5RWqXOguvM@cluster0.jmmzh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5921378472').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    

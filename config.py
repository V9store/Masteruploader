import os

class Config(object):
    BOT_TOKEN = os.environ.get("7251269795:AAFJ9yW6nw-rp7c2Zy4VUqsmxVfgiRS8imo")
    API_ID = int(os.environ.get("21283957"))
    API_HASH = os.environ.get("aade44a828de52da2a6ef816b120020b")
    AUTH_USER = os.environ.get('AUTH_USERS', '7602994049').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"

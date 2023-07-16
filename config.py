##OPEN API STUFF
OPENAI_API_KEY = 'insert your open ai key in quotes here'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "insert your open ai key in quotes here"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

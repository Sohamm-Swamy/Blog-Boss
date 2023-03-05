##OPEN API STUFF
OPENAI_API_KEY = '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'



## FLASK STUFF
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "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"


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

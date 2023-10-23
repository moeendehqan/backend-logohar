from mongoengine import connect

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/logohar',
    }
    HOST = '0.0.0.0'
    PORT = 5000

class DevelopmentConfig(Config):
    DEBUG = True
    PORT = 5000


class ProductionConfig(Config):
    HOST = '0.0.0.0'
    PORT = 2100

class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/logohar',
    }

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

connect(host=Config.MONGODB_SETTINGS['host'])

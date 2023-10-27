from mongoengine import connect

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/logohar',
    }
    HOST = '0.0.0.0'
    PORT = 8080

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    HOST = '0.0.0.0'

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

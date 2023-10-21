from mongoengine import connect

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'your_secret_key'
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/logohar',
    }

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    HOST = '0.0.0.0'
    PORT = 8080

class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/your_test_database_name',
    }

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}

# اتصال به دیتابیس در هنگام اجرای برنامه
connect(host=Config.MONGODB_SETTINGS['host'])

from app import create_app
from config import config
from waitress import serve

environment = 'production'
print('start',environment)

app = create_app(environment)

if environment in config:
    app_config = config[environment]
else:
    app_config = config['default']


if __name__ == '__main__':
    if environment == 'production0':
        serve(app, host=app_config.HOST, port=app_config.PORT)
    else:
        app.run(port=app_config.PORT, host=app_config.HOST)

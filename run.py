from app import create_app
from config import config
from waitress import serve
from lateral import init_fact_class, init_fact_color_type, init_fact_jobs
environment = 'development'
print('start',environment)

app = create_app(environment)

if environment in config:
    app_config = config[environment]
else:
    app_config = config['default']


if __name__ == '__main__':
    init_fact_class()
    init_fact_jobs()
    init_fact_color_type()
    if environment == 'production':
        serve(app, host=app_config.HOST, port=app_config.PORT)
    else:
        app.run(debug=True, port=app_config.PORT, host=app_config.HOST)

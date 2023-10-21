from app import create_app



environment = 'development'

app = create_app(environment)


if __name__ == '__main__':
    app.run(debug=True)

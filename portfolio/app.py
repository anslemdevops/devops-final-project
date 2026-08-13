from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Anslem Iwebor Portfolio</title>
        </head>
        <body>
            <h1>Welcome to Anslem Iwebor's Portfolio</h1>
            <p>Junior Cloud & DevOps Engineer</p>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

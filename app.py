from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "Insight web app created by marcmeijer."

if __name__ == '__main__':
    app.run()

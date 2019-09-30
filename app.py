from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    errors = []
    trends = ''
    if request.method == "POST":
        # get url that the user has entered
        try:
            word = request.form['word']
            # print statements just print to terminal
            print("word was:")
            print(word)
        except:
            print("error")
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

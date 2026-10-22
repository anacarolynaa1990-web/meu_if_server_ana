from flask import Flask, render _template

app = Flask(___name___)

@app.route('/')
def index ():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
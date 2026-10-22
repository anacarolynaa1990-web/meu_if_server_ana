from flask import Flask, render _template

app = Flask(___name___)

@app.route('/')
def index ():
    return render_template('index.html')

if_name_ == '__main__':
    app.run()
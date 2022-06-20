from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def say_hello():
    # greet = """
    # html>
    #     <body>
    #         <h1>Welcome</h1>
    #     </body>
    # </html>
    # """
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    return "Welcome Home"

@app.route('/welcome/back')
def welcome_back():
    return "Welcome Back"
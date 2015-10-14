from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route("/user/<paul>")
def show_user_profile(paul):
    return 'User %s' % paul

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return 'Post %d' % post_id

@app.route("/hello")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

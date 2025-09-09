from flask import Flask, render_template, request

app = Flask(__name__)

posts = []

@app.route('/')
def home():
    return render_template("index.html", posts=posts)

@app.route('/posts')
def posts_list():
    return posts

@app.route('/submit-forum-post', methods=['POST'])
def submit_forum_post():
    title = request.form.get('title')
    content = request.form.get('content')

    posts.append([title, content])
    return "You did it you submitted it"


if __name__=='__main__':
    app.run(debug=True)

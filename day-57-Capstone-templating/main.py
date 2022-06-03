from flask import Flask, render_template
import json
from post import Post


app = Flask(__name__)

post = Post()

@app.route('/')
def home():
    all_posts = post.all_posts
    return render_template("index.html", posts=all_posts)

@app.route('/post/<int:num>')
def read_post(num):
    all_posts = post.all_posts
    print(all_posts)
    return render_template("post.html", posts=all_posts, num=num)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    all_posts_from_site = get_all_blog_posts()
    return render_template("index.html", all_posts = all_posts_from_site)

@app.route("/blog/<int:post_id>")
def blog_post(post_id: int):
    all_posts_from_site = get_all_blog_posts()

    post_data = None
    for post in all_posts_from_site:
        if int(post.m_id) == post_id:
            post_data = post
            break

    print(post_data)
    return render_template("post.html", post=post_data)

def get_all_blog_posts():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    response.raise_for_status()

    retval = []
    all_blogs = response.json()
    for blog in all_blogs:
        retval.append(Post(blog['id'], blog['title'], blog['subtitle'], blog['body']))

    return retval

if __name__ == "__main__":
    app.run(debug=True)

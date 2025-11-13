import os

from flask import Flask, render_template, request
from email_account import EmailAccount
import os
import requests
from post import Post

GMAIL_ADDRESS = os.environ.get("GMAIL_ADDRESS")
GMAIL_PASSWORD = os.environ.get("GMAIL_PASSWORD")

account = EmailAccount(my_email=GMAIL_ADDRESS, my_password=GMAIL_PASSWORD)

app = Flask(__name__)

@app.route('/')
def home():
    all_posts_from_site = get_all_blog_posts()
    return render_template("index.html", all_posts = all_posts_from_site)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/form-entry', methods=['GET', 'POST'])
def receive_contact_us_data():

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
    elif request.method == 'GET':
        name = request.args.get('name', '')
        email = request.args.get('email', '')
        phone = request.args.get('phone', '')
        message = request.args.get('message', '')

    subject = f"BLOG Email from {name}"
    body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n {message}"

    account.send_email("earthmabus@hotmail.com", subject, body)

    return render_template("contact_successful.html")

@app.route("/blog/<int:post_id>")
def blog_post(post_id: int):
    all_posts_from_site = get_all_blog_posts()

    post_data = None
    for post in all_posts_from_site:
        if int(post.m_id) == post_id:
            post_data = post
            break

    print(post_data.m_id)
    print(post_data.m_title)
    print(post_data.m_subtitle)
    print(post_data.m_body)
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

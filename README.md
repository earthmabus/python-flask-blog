# Blog Post Display

This project displays fictious blog title and subtitles when a user navigates to the /index.html page.
The /index.html page contains "Read" links for each blog that load up individual blog pages when clicked.

This project shows the ability of flask to
- utilize multiple routes: **/** and **/blog/<post_id>**
- url building by using url_for(...) for "Read" links to navigate to a blog page
- utilize jinga to populate a blog.html template with python generated content (in this case, content that is retrieved in json, stored in a class, and unpacked in the template)

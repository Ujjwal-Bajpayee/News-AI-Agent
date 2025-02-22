from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost
from dotenv import load_dotenv
import os

load_dotenv()

def publish_to_wordpress(title, content):
    try:
        wp = Client(os.getenv("WORDPRESS_URL"), os.getenv("WORDPRESS_USERNAME"), os.getenv("WORDPRESS_PASSWORD"))
        post = WordPressPost()
        post.title = title
        post.content = content
        post.post_status = 'publish'
        wp.call(NewPost(post))
        print(f"Published: {title}")
    except Exception as e:
        print(f"Failed to publish: {e}")
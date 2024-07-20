import database

def handle_get_posts():
    return database.get_all_posts()

def handle_add_post(title, content):
    if not title or not content:
        raise ValueError("Title and content cannot be empty")
    database.add_post(title, content)

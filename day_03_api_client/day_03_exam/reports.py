


def print_posts_report(posts):
    print("POST REPORT")
    print("=" * 30)

    for post in posts:
        title = post.get("title", "Unknown")
        id = post.get("id", "Unknown")
        body = post.get("body", "Unknown")
        user = post.get('userId', 'Unknown')
        print(f"Post #{id} | User: {user} | Title: {title} | Body: {body}")

    print("=" * 30)
    print(f"Total posts: {len(posts)}")



def print_single_post_report(post):
    print("SINGLE POST REPORT")
    print("=" * 30)

    title = post.get("title", "Unknown")
    id = post.get("id", "Unknown")
    body = post.get("body", "Unknown")
    user = post.get('userId', 'Unknown')
    print(f"Post #{id} | User: {user} | Title: {title} | Body: {body}")

    print("=" * 30)
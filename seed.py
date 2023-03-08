import random
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post, Comment, Tag

def create_users(num_users):
    """
    Create 'num_users' users with normal role.
    """
    users = []
    for i in range(num_users):
        username = f"user{i}"
        password = "password123"
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            users.append(user)
        else:
            user = User.objects.create_user(username=username, password=password)
            users.append(user)
    return users

def create_posts(num_posts):
    """
    Create 'num_posts' posts.
    """
    post_titles = [
        "My first post",
        "Why I love programming",
        "10 tips for becoming a better developer",
        "The future of software development",
        "How to write clean code",
        "My favorite programming languages",
        "Debugging strategies for beginners",
        "The importance of good documentation",
        "Building scalable web applications",
        "Getting started with machine learning",
    ]
    tags = list(Tag.objects.all())
    for title in post_titles:
        content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed,          dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi                                                                   Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula massa, varius a, semper congue, euismod non, mi."
        author = User.objects.get(username="jocke_blog") # assuming you're the admin
        created_at = timezone.now() - timezone.timedelta(days=random.randint(1, 365))
        post = Post.objects.create(title=title, content=content, author=author, created_at=created_at)
        post.tags.set(random.sample(tags, k=random.randint(1, len(tags))))

# Helper function to create tags
def create_tags():
    """
    Create some tags.
    """
    tag_names = ["mac", "pc", "frontend", "backend", "full-stack"]
    for tag_name in tag_names:
        tag, _ = Tag.objects.get_or_create(name=tag_name, slug=tag_name)

# Helper function to create comments
def create_comments(users):
    posts = Post.objects.all()
    for post in posts:
        commenters = random.sample(users, k=random.randint(1, 10))
        for commenter in commenters:
            content = "Great post!"
            created_at = timezone.now() - timezone.timedelta(days=random.randint(1, 365))
            comment = Comment.objects.create(post=post, author=commenter, content=content, created_at=created_at)

            # Update some comments
            if random.random() < 0.1:
                comment.content = "I changed my mind, this post is terrible!"
                comment.updated_at = timezone.now()
                comment.save()

def seed_data():
    users = create_users(50)
    create_tags()
    create_posts(10)
    create_comments(users)

seed_data() # Call the function to run everything.

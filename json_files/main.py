import json
import requests


def read_tasks():
    with open('tasks.json', 'r') as task_file:
        tasks = json.loads(task_file.read())
        for task in tasks:
            print(task)


def read_posts():
    with open('posts.json', 'r') as posts_file:
        posts = json.load(posts_file)
        print(posts)


def require_posts(user_id: int) -> list:
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    posts = json.loads(response.text)

    user_posts = []

    for post in posts:
        if post['userId'] == user_id:
            user_posts.append(post)

    return user_posts


def store_user_posts(posts: list):
    with open('posts.json', 'w') as posts_file:
        json.dump(
            posts,
            posts_file,
            indent=2
        )


def process_posts(nome):
    file_name = 'posts.json'
    with open(file_name, 'r') as old_posts_file:
        posts = json.load(old_posts_file)
        for post in posts:
            post.update({'nome': nome})

    with open(file_name, 'w') as new_posts_file:
        json.dump(posts, new_posts_file, indent=2)


def main():
    user = {
        'id': 8,
        'nome': 'John Doe'
    }
    posts = require_posts(user['id'])
    store_user_posts(posts)
    process_posts(user['nome'])


if __name__ == '__main__':
    main()

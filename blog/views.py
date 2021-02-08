from django.shortcuts import render

posts = [
    {
        'author': 'John Doe',
        'title': 'Blog Post 1',
        'content': 'First blog post!',
        'date_posted': '8/2/2021'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second blog post!',
        'date_posted': '20/2/2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

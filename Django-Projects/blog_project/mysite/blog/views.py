from django.shortcuts import render
from datetime import date

# Create dummy data
all_posts = [
    {
        "slug": "nature-at-its-best",  # Updated slug
        "image": 'nature.jpg',
        "author": "Aditya",
        "date": date(2021, 7, 24),
        "title": "Nature at its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible.",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit..."
    },
    {
        "slug": "hike-in-the-mountains",  # Updated slug
        "image": 'mountains.jpg',
        "author": "Aditya",
        "date": date(2021, 7, 24),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains!",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit..."
    },
    {
        "slug": "programming-is-great",  
        "image": 'programming.jpg',
        "author": "Aditya",
        "date": date(2021, 7, 24),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours debugging that one error in your code? Yep, that’s what happened to me yesterday...",
        "content": "Lorem ipsum dolor sit amet consectetur adipisicing elit..."
    }
]

def get_date(post):
    return post.get('date')

# Create your views here.
def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]  
    return render(request, "blog/index.html", {"posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html", {'all_posts': all_posts})

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {"post": identified_post})


    

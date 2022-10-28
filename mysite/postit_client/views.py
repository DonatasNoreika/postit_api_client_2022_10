from django.shortcuts import render, redirect
import requests

token = "42b88cc2649142c8bcf11f59da0e28c36f023a65"

# Create your views here.
def posts(request):
    r = requests.get('http://127.0.0.1:8000/posts')
    context = {
        'posts': r.json()
    }
    return render(request, 'posts.html', context=context)


def post(request, pk):
    r = requests.get(f'http://127.0.0.1:8000/posts/{pk}')
    post = r.json()
    print(post)
    context = {
        'post': post,
    }
    return render(request, 'post.html', context=context)


def new_post(request):
    header = {
        "Authorization": f"Token {token}"}
    if request.method == "POST":
        naujas_irasas = {
            'title': request.POST['title'],
            'body': request.POST['body'],
        }
        r = requests.post('http://127.0.0.1:8000/posts', data=naujas_irasas, headers=header)
        return redirect('posts')
    else:
        return render(request, 'new_post.html')
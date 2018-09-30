from django.shortcuts import render, get_object_or_404, redirect
from .models import Joke


def jokes_render(request):
    jokes = Joke.objects.all().order_by('title')
    return render(request, 'jokes.html', {'jokes': jokes})

def joke_add_one(request, joke_id):
    joke = get_object_or_404(Joke, pk=joke_id)

    if request.method == 'POST':
        joke.count += 1
        joke.save()
        return redirect('jokes_render')
    else:
        return render(request, '404.html')

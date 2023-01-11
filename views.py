from django.shortcuts import render

# Create your views here.
from .forms import AricleForm

# Create your views here.
def product_create_view(request):
    form = AricleForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form' : form
    }
    return render(request, 'article_create.html', context)


def index(request):
    return render(request, 'index.html')
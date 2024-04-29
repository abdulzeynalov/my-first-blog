from django.shortcuts import render

def my_view(request):
    context = {
        'title': 'Welcome to My Website',
        'content': 'This is the content of my page.',
    }
    return render(request, 'my_template.html', context)

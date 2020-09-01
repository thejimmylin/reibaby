from django.shortcuts import render
from django.http.response import HttpResponse
from .forms import Question


def index(request):
    form = Question()
    context = {
        'form': form
    }
    if request.method == 'POST':
        form = Question(request.POST)
        if form.is_valid():
            the_date = form.cleaned_data['the_date']
            if the_date == '20180105' or the_date == '850608':
                return render(request, 'index.html')
    return render(request, 'question.html', context)
        

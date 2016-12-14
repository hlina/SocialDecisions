from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.utils import timezone
from random import randint

def url_generate():
    random_url = ""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    nums = [i for i in range(0,10)]
    for i in range(0, 9):
        if randint(0,1) == 1: random_url += str(nums[randint(0,9)])
        else: random_url += letters[randint(0,25)]
    random_url += letters[randint(0,25)]
    return random_url

def index(request):
    try: 
        q_text = request.POST['question']
        p_date = request.POST['date'].split("/")
        c_text = request.POST.getlist('option')
    except:
        return render(request, 'polls/index.html')
    else:
        date = p_date[2]+"-"+p_date[0]+"-"+p_date[1]
        q = Question(question_text= q_text, pub_date= date)
        q.save()
        for i in range(0, len(c_text)): q.choice_set.create(choice_text = c_text[i], votes=0)
        q.url_random = url_generate() + str(q.id)
        q.save()
        print q.url_random
        url = unicode(q.url_random, "utf-8")
        return HttpResponseRedirect(reverse("polls:detail", args=(url,)))

def about(request):
    return render(request, 'polls/about.html')

def detail(request, question_url):
    question = get_object_or_404(Question, url_random=question_url)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_url):
    question = get_object_or_404(Question, url_random=question_url)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_url):
    question = get_object_or_404(Question, url_random=question_url)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_url,)))
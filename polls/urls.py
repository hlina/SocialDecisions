from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/about/
    url(r'^about/$', views.about, name='about'),
    # ex: /polls/adsfafd5/
    url(r'^(?P<question_url>.{11}[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_url>.{11}[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_url>.{11}[0-9]+)/vote/$', views.vote, name='vote'),
]
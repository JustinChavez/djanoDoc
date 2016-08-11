from django.conf.urls import url

from . import views

app_name = 'polls'
urlpatterns = [
       # ex: /polls/
    url(r'^$', views.index, name='index'),
    #url for reigister
    url(r'^register/$', views.register, name='register'),
    #url for login
    url(r'^login/$', views.logins, name='login'),
    #logout
    url(r'^logout/$', views.logout_user, name='logout_user'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/main
    url(r'^main/$', views.dashboard, name='dashboard'),
#     policy
    url(r'^policy/$', views.policy, name='policy'),
    #already voted page
    url(r'^already/$', views.already, name='already'),
    #profile
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$', views.thanks, name='thanks'),

]


# Create your views here

from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import Http404
from .models import Question
from django.template import loader
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import ChoiceForm, UserForm
from .models import Choice, UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.template import RequestContext

#index request with render function. There is no longer a need to have a line to get
#the template. The second argument of render handles that for us.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    #return HttpResponse("You're looking at question %s." % question_id)

    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")

    #following function is a shortcut for a try except statement that tries to
    #identify a 404 error like above
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

#jonathan's edits
def results(request, question_id):
    form = ChoiceForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()

    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

    #question = get_object_or_404(Question, pk=question_id)
    #return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def dashboard(request):
    context = {
    'A_KEYWORD': "A_VARIABLE_OR_OBJECT",
    }

    return render(request, 'polls/main.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
       #adds the password and then save it
        user.set_password(password)
        user.save()
        print ("testing")
        #takes user and pass and see if it exists in database
        user = authenticate(username=username, password=password)
        #this is from above has return it
        if user is not None:
            #see if the account is not banned or disable or others things
            if user.is_active:
                #this is how you login in
                login(request, user)
                #redircts them to where you want them to go afeter they reigister
               # return redirect('polls:index')
                return HttpResponse("testing")
    #this is puporse to redierct them to a blank form
    #return render(request, self.template_name, {'form':form})
                #return render_to_response('polls:login', {}, context)
    return render_to_response('polls/register.html', {'form':form}, context_instance=
                                      RequestContext(request))

def logins(request):
    print("0")
    if request.method == 'POST':
        print("1")
        username =request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            print("2")
            if user.is_active:
                print("3")
                login(request, user)
                users = UserProfile.objects.filter(user=request.user)
                return render(request, 'polls/index.html', {'users':users})

            else:
                print("4")
                return render (request, 'polls/login.html', {'error_message': 'Your account has been disabed'})
        else:
            print("5")
            return render(request, 'polls/login.html', {'error_message':'Invalid_login'})
    return render(request, 'polls/login.html')



# def register(request):
# #TODO do we need request context? Abandon?
#     # context = RequestContext(request)
#
#     # A boolean value for telling the template whether the registeatation was succesful
#     #set to false initially code changes value to true when registratation succceds
#     registered = False
#
# #if it's a Http POST, we're interested in processing form data
#     if request.method == 'POST':
#         #attempt to grab information from the raw information
#         #not that we make use of bot USERform and UserPRofileForm
#
#     #if it's a Http POST we're interested in provessing form data
#


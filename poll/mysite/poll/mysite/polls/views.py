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
from django.contrib import messages

# Justin 2016/07/15:
# Now using message framework to relay messages to the user. Check messages.error lines to see it in action

#index request with render function. There is no longer a need to have a line to get
#the template. The second argument of render handles that for us.

def index(request):
    if request.user.is_authenticated():
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        return render(request, 'polls/index.html', context)
    else:
        messages.error(request, 'ERROR: Need to login first')
        return HttpResponseRedirect('/polls/login/')

def detail(request, question_id):
    if request.user.is_authenticated():
        #return HttpResponse("You're looking at question %s." % question_id)

        # try:
        #     question = Question.objects.get(pk=question_id)
        # except Question.DoesNotExist:
        #     raise Http404("Question does not exist")

        #following function is a shortcut for a try except statement that tries to
        #identify a 404 error like above
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/detail.html', {'question': question})
    else:
        messages.error(request, 'ERROR: Need to login first')
        return HttpResponseRedirect('/polls/login/')

#jonathan's edits
def results(request, question_id):
    if request.user.is_authenticated():
        form = ChoiceForm(request.POST or None)
        if form.is_valid():
            save_it = form.save(commit=False)
            print("what what")
            save_it.save()

        response = "You're looking at the results of question %s."
        # return HttpResponse(response % question_id)
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'polls/results.html', {'question': question})

        # return HttpResponseRedirect('/polls/results/')
        # return render(request, 'polls/results.html')

    else:
        messages.error(request, 'ERROR: Need to login first')
        return HttpResponseRedirect('/polls/login/')

def vote(request, question_id):
    if request.user.is_authenticated():
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
            selected_choice.user = request.user
            print (selected_choice.user.username)
            selected_choice.save()
            # Always return an HttpResponseRedirect after successfully dealing
            # with POST data. This prevents data from being posted twice if a
            # user hits the Back button.
            return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
    else:
        return render(request, 'polls/login.html', {'error_message': 'Need to login first'})

def dashboard(request):
    if request.user.is_authenticated():
        context = {
        'A_KEYWORD': "A_VARIABLE_OR_OBJECT",
        }

        return render(request, 'polls/main.html', context)

    else:
        return render(request, 'polls/login.html', {'error_message': 'Need to login first'})

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
                return HttpResponseRedirect('/polls')
                # return render(request, 'polls/index.html', {'users':users})
            else:
                print("4")
                return render (request, 'polls/login.html', {'error_message': 'Your account has been disabed'})
        else:
            print("5")
            return render(request, 'polls/login.html', {'error_message':'Username or Password did not match'})
    return render(request, 'polls/login.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            users = UserProfile.objects.filter(user=request.user)
            return render(request, 'polls/index.html', {'users':users})
    context = {
            "form":form,
    }
    return render(request, 'polls/register.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    # context = {
    #     "form":form,
    # }
    return HttpResponseRedirect('/polls/login/')
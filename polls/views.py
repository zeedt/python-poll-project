from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.utils import timezone
from .form import UploadForm, DocumentModelWithFileField, NameForm
from django.contrib.auth import authenticate, login, logout
import logging

logger = logging.getLogger(__name__)

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class DetailsView(generic.DetailView):
    model = Question
    template_name = "polls/details.html"


# def index(request):
#     question_list = Question.objects.order_by('id')[:5]
#     for q in question_list:
#         print(q.question_text)
#     template = loader.get_template("polls/index.html")
#     context = {'latest_question_list': question_list}
#     return HttpResponse(template.render(context, request))
#
#
# def details(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#
#     return render(request, "polls/details.html", {"question": question})
#
#
# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#
#     response = "You are looking at result of question %s"
#     return render(request, "polls/results.html", {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/details.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def handle_uploaded_file(f):
    with open('uploaded-documents/uploaded.png', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['document'])
            return HttpResponseRedirect(reverse('polls:upload'))
        return HttpResponse('this is not a valid file')
    else:
        return render(request, 'polls/file-upload.html')


def uploadWithFormModel(request):
    if request.method == 'POST':
        form = DocumentModelWithFileField(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('polls:upload'))
        return HttpResponse('this is not a valid file')
    else:
        return render(request, 'polls/file-upload.html')


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'polls/name.html', {'form': form})


# @login_required
# @permission_required('polls.can_vote')
def user_page(request):
    logger.info("Loading request page now")
    user = request.user
    print("Authenticated user is ", user.is_authenticated)
    return HttpResponse("Is user authenticated??? " + str(user.is_authenticated))

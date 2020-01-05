from django.shortcuts import render

from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.utils import timezone


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

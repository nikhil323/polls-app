from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.views import generic
from django.utils import timezone

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

# def index(request):
#     latest_qsn_list = Question.objects.order_by("-pub_date")[:5]
#     context = {
#         "latest_question_list": latest_qsn_list
#     }
#     return render(request, "polls/index.html", context)

# def detail(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/detail.html", {"question": q})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question })

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #request.Post is a dictionary like object that lets you access submitted data by key name. In this case, request.Post['choice] returns ID of the selected choice, as a string. request.Post values are always strings.
        print("the selected choice is", selected_choice)
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {"question": question, "error_message": "You didn't select a choice"})
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
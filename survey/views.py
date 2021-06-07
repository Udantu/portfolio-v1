from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.db import models
from .models import Survey, Question, Answer
from .forms import AnswerQuestion

def survey(request):
    context = {'surveys': Survey.objects.all()}
    return render(request,"survey/survey.html",context)

@login_required
def take_survey(request,id):

    if request.method == "POST":
        answers = []
        print(request.POST)

        questions = Question.objects.filter(survey=id)

        ans = request.POST.dict()
        del ans[next(iter(ans))]
        answerList = []
        for key in ans.keys():
            answerList.append(int(ans[key]))

        if len(questions) != len(answerList):
            messages.debug(request,f'You did not fill out all the questions.')
            return redirect(reverse('toSurvey'))

        que = request.POST.dict()
        del que[next(iter(que))]
        questionList = list(que.keys())

        for i,q in enumerate(answerList):
            questionNew = Question.objects.filter(question=questionList[i])[0]
            authorNew = request.user
            answerNew = answerList[i]
            newAnswer = Answer.objects.create(author=authorNew,
                                              answer=answerNew,
                                              question=questionNew)

        return redirect(reverse('toSurvey'))

    survey = get_object_or_404(Survey,pk=id)
    questions = Question.objects.filter(survey=id)

    context = {'questions':questions,
               'survey': survey}
    return render(request,"survey/take-survey.html",context)

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
# from django.template import loader
from django.urls import reverse
from .models import Question,Choice
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'lastest_question_list'
    def get_queryset(self):
        """返回最近发布的5个问卷"""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.ListView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.ListView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question,pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError,Choice.DoesNotExist):
        # 发生choice未找到的错误是，重新返回表单页面，并贴出提示信息
        return render(request,'polls/detail.html',{
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # 成功处理数据之后，自动跳转到结果页面，防止用户连续多次提交
        return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
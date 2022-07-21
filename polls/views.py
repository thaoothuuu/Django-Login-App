import datetime
from .models import Question
from django.shortcuts import render
from django.http import HttpResponse
from .forms import QuestionForm, ChoiceForm
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class indexclass(View):
    def get(self, request):
        self.name = 'STELLA'
        self.day = datetime.datetime.now()
        self.hobbies = ['Sleeping', 'Traveling', 'Playing with cat']
        self.asset = {'cat': 1, 'Lap': 1, 'Phone': 1}
        context = {
            'name': self.name,
            'day': self.day,
            'hobbies': self.hobbies,
            'asset': self.asset
        }
        return render(request, template_name='polls/index.html', context=context)


@decorators.login_required(login_url='/login/login')
def viewlist(request):
    list_question = Question.objects.all()
    context = {'lq': list_question}
    return render(request, template_name='polls/question_list.html', context=context)


def detailView(request, q_id):
    q = Question.objects.get(pk=q_id)
    context = {'qs': q}
    return render(request, template_name='polls/detail_question.html', context=context)


def vote(request, q_id):
    q = Question.objects.get(pk=q_id)  # lấy đối tượng có id là id question
    try:
        data = request.POST["choice"]  # lấy id choice mà người dùng chọn và gửi lên server
        c = q.choice_set.get(pk=data)
    except:
        return HttpResponse("Không có choice cho câu hỏi này")
    c.vote += 1
    c.save()
    context = {
        'qs': q,
    }
    return render(request, template_name='polls/result.html', context=context)
    # return HttpResponse(c.vote)


# def questionform(request):
#     a = QuestionForm()
#     context = {'f': a}
#     return render(request, template_name='polls/addquestion.html', context=context)


# def addquestion(request):
#     if request.method == 'POST':
#         g = QuestionForm(request.POST)
#         if g.is_valid():
#             g.save()
#             qs = g.cleaned_data['question_text']
#             context = {'qs': qs}
#             return render(request, template_name='polls/displayquestion.html', context=context)
#         else:
#             return HttpResponse("Nhập sai")
#     else:
#         return HttpResponse("Không lưu được")


def deletequestion(request, q_id):
    if request.method == 'POST':
        q = Question.objects.get(pk=q_id)
        q.delete()
    list_question = Question.objects.all()
    context = {'lq': list_question}
    return render(request, template_name='polls/question_list.html', context=context)


class savequestionclass(View):
    def get(self, request):
        a = QuestionForm()
        context = {'f': a}
        return render(request, template_name='polls/addquestion.html', context=context)

    def post(self, request):
        g = QuestionForm(request.POST)
        if g.is_valid():
            g.save()
            qs = g.cleaned_data['question_text']
            context = {'qs': qs}
            return render(request, template_name='polls/displayquestion.html', context=context)
        else:
            return HttpResponse("Nhập sai")

    # def delete(self, request):
    #     q = self.get_object()
    #     q.delete()
    #     list_question = Question.objects.all()
    #     context = {'lq': list_question}
    #     return render(request, template_name='polls/question_list.html', context=context)


# def choiceform(request):
#     c = ChoiceForm()
#     context = {
#         'c': c,
#     }
#     return render(request, template_name='polls/addchoice.html', context=context)


# def addchoice(request):
#     if request.method == 'POST':
#         c = ChoiceForm(request.POST)
#         if c.is_valid():
#             c.save()
#             list_question = Question.objects.all()
#             context = {'lq': list_question}
#             return render(request, template_name='polls/question_list.html', context=context)
#         else:
#             return HttpResponse("Fail to save")
#     else:
#         return HttpResponse("Fail to save")


class SaveChoice(View):
    def get(self, request):
        cf = ChoiceForm()
        context = {'c': cf}
        return render(request, template_name='polls/addchoice.html', context=context)

    def post(self, request):
        c = ChoiceForm(request.POST)
        if c.is_valid():
            c.save()
            list_question = Question.objects.all()
            context = {'lq': list_question}
            return render(request, template_name='polls/question_list.html', context=context)
        else:
            return HttpResponse("Fail to save")

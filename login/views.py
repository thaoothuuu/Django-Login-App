from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import PostForm
# Create your views here.

class indexclass(View):
    def get(self, request):
        return render(request, template_name='login/index.html')


class Loginclass(View):
    def get(self, request):
        return render(request, template_name='login/login.html')
    def post(self, request):
        name = request.POST['username']
        matkhau = request.POST['password']
        user = authenticate(username=name, password=matkhau)
        if user is not None:
            login(request, user)
            return render(request, 'login/loginsuccess.html')

        else:
            return HttpResponse('Không tồn tại user')


# class ViewUser(LoginRequiredMixin, View):
#     login_url = '/login/login'
#     def get(self, request):
#         return HttpResponse("View post")


@decorators.login_required(login_url='/login/login')
def viewproduct(request):
    return HttpResponse("View post")


class AddForm(LoginRequiredMixin, View):
    login_url = '/login/login'
    def get(self, request):
        f = PostForm()
        context = {
            'f': f
        }
        return render(request, template_name='login/addpost.html', context=context)

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            if request.user.has_perm('login_add_post'): #viết thường tên model request.user.get_all_permissions()
                g.save()
                t = g.cleaned_data['title']
                c = g.cleaned_data['content']
                context = {
                    't': t,
                    'c': c
                }
                return render(request, template_name='login/displaypost.html', context=context)
            else:
                return HttpResponse("Bạn không có quyền thêm")
        else:
            return HttpResponse("Nhập lại")


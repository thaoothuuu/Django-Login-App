from . import views
from django.urls import path

app_name = 'polls'  # url namespace
urlpatterns = [
    path('', views.indexclass.as_view(), name='index'),
    path('question/', views.viewlist, name='question'),
    path('question/detail/<int:q_id>', views.detailView, name='detail'),
    path('<int:q_id>', views.vote, name='vote'),
    # path('addform/', views.questionform, name='questionform'),
    # path('addquestion/', views.addquestion, name='addquestion'),
    path('savequestionclass/', views.savequestionclass.as_view(), name='savequestionclass'),
    path('deletequestion/<int:q_id>', views.deletequestion, name='deletequestion'),
    # path('choiceform/', views.choiceform, name='choiceform'),
    # path('addchoice/', views.addchoice, name='addchoice'),
    path('savechoice/', views.SaveChoice.as_view(), name='savechoice')


]

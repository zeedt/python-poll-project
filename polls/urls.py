from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
    path('<int:pk>/results', views.ResultView.as_view(), name='results'),
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('upload', views.uploadWithFormModel, name='upload'),
    # path('name', TemplateView.as_view(template_name="polls/name.html")),
    path('name', views.get_name, name='name'),
    path('userpage', views.user_page, name='userpage'),
]
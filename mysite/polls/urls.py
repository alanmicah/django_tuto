from django.urls import path

from . import views

# Adding path() calls for the new added views
# add namespaces to your URLconf for multiple apps
# so django knows which app view to create a url when using the {% url %} template tag
app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
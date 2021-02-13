from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.api_overview, name="api-overview"),
	path('task-create/', views.emptask_CreateView.as_view(), name="task-create"),	
	path('task-list/', views.emptask_list.as_view(), name="task-list"),       
        url(r'^task-update-delete/(?P<pk>[0-9]+)/$', views.emptask_UpdateView.as_view()),        
        
]

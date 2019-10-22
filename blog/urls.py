from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts', views.post_draft_list, name='post_draft_list'),
    path('post/<int:pk>/delete/', views.post_delete, name="post_delete"),
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.post_comment, name='post_comment'),
    url(r'^comment/(?P<pk>\d+)/ok/$', views.comment_ok, name='comment_ok'),
    url(r'^comment/(?P<pk>\d+)/delete/$', views.comment_del, name='comment_del'),
    path('prueba1', views.prueba1, name='prueba1'),
    #path('comment/<int:pk>/ok/', views.comment_ok, name='comment_ok'),
    #path('comment/<int:pk>/delete/', views.comment_del, name='comment_del'),
]

#url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
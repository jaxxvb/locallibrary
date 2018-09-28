from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    # path(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)$', views.AuthorDetailedView.as_view(), name='author-detail'),

]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
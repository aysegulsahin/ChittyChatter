from django.conf.urls import url
from forum.views import *

urlpatterns = [
    url(r'^$', CategoryView.as_view(), name="home"),
    url(r'^contact/$', ContactFormView.as_view(), name="contact"),
    url(r'^rules/$', RulesView.as_view(), name="rules"),
    url(r'^(?P<cslug>[A-Za-z0-9\-]+)/$', CategoryDetailView.as_view(), name="category_name"),
    url(r'^(?P<cslug>[A-Za-z0-9\-]+)/thread/(?P<tslug>[A-Za-z0-9\-]+)-(?P<pk>[0-9]+)/$', ThreadView.as_view(),
        name="thread_name"),
    url(r'^(?P<cslug>[A-Za-z0-9\-]+)/thread/create_thread/$', ThreadCreateView.as_view(), name="thread_create"),
    url(r"^api/like$", like, name="like_dislike"),
    url(r"^signup$", RegistrationView.as_view(), name="register"),
]

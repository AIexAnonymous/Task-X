from django.conf.urls import url
from django.views.static import serve
from . import search
urlpatterns = [
    url(r'^welcome$',search.welcome),
    url(r'^questionnaire$',search.questionnaire),
    url(r'^OK$',search.OK),
    url(r'^image/(?P<path>.*)$', serve, {'document_root': '/home/alex/aa/image'}),
    url(r'^test$', search.test),

]

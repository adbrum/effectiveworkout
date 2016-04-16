from django.conf.urls import url
from effectiveworkout.assiduousness.views import new, listassiduity, success


urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^lista/', listassiduity, name='list'),
    url(r'^sucesso/', success, name='success'),
    # url(r'^(\w+)/$', success, name='success'),

]

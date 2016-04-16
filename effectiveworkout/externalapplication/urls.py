from django.conf.urls import url
from effectiveworkout.externalapplication.views import new, success, empty_prototipo_form

urlpatterns = [
    url(r'^$', new, name='new'),
    # url(r'^form/', empty_prototipo_form, name='form'),
    url(r'^sucesso/', success, name='success'),
]

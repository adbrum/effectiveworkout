from django.conf.urls import url
from effectiveworkout.usersprofiles.views import new, listsubscription, empty_prototipo_form, editUserProfile, \
    delDataModalUserProfile, \
    delConfirmeUserProfile, success, activeDataModalUserProfile, activeConfirmeUserProfile

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editUserProfile, name="edit"),
    url(r'^form/', empty_prototipo_form, name='form'),
    url(r'^lista/', listsubscription, name='list'),
    url(r'^deletar/', delDataModalUserProfile, name='delete'),
    url(r'^ativar/', activeDataModalUserProfile, name='activate'),
    url(r'^confirmedeletar/', delConfirmeUserProfile, name='delconfirm'),
    url(r'^confirmeativar/', activeConfirmeUserProfile, name='activeconfirm'),
    url(r'^sucesso/', success, name='success'),
]

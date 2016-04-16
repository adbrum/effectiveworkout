from django.conf.urls import url
from effectiveworkout.monthlyplans.views import new, editPlano, delDataModalPlano, \
    delConfirmePlano, listmonthlyplan, success, activeDataModalUserProfile, activeConfirmeUserProfile

urlpatterns = [
    url(r'^$', new, name='new'),
    url(r'^edit/(?P<pk>\d+)$', editPlano, name="edit"),
    url(r'^lista/', listmonthlyplan, name='list'),
    url(r'^deletar/', delDataModalPlano, name='delete'),
    url(r'^ativar/', activeDataModalUserProfile, name='activate'),
    url(r'^confirmedeletar/', delConfirmePlano, name='delconfirme'),
    url(r'^confirmeativar/', activeConfirmeUserProfile, name='activeconfirm'),
    url(r'^sucesso/', success, name='success'),
]

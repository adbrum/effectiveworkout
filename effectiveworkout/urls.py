from django.conf.urls import url, include
from django.contrib import admin
from effectiveworkout.administration.views import Logout, Login
from effectiveworkout.core.views import home, unauthorized
from effectiveworkout.exercises.api import views as exercises_api_views
admin.site.site_header = 'Administração Effective Workout'

urlpatterns = [
    url(r'^$', home.as_view(), name='home'),
    # url(r'^sucesso/', success.as_view(), name='success'),
    url(r'^naoautorizada/', unauthorized.as_view(), name='redirect'),

    url(r'^administracao/', include('effectiveworkout.administration.urls',
                                namespace='administration')),
    url(r'^login/', Login, name='login'),

    url(r'^logout/$', Logout, name='logout'),
    # url(r'^novo/', include('effectiveworkout.usersprofiles.urls',
    #                             namespace='usersprofiles')),
    url(r'^inscricao/', include('effectiveworkout.usersprofiles.urls',
                                namespace='usersprofiles')),
    url(r'^inscricaoexterna/', include('effectiveworkout.externalapplication.urls',
                                namespace='external')),
    url(r'^presenca/', include('effectiveworkout.assiduousness.urls',
                               namespace='assiduousness')),
    url(r'^avaliacaofisica/', include('effectiveworkout.reviewsphysicals.urls',
                                      namespace='reviewsphysicals')),
    url(r'^planosmensais/', include('effectiveworkout.monthlyplans.urls',
                                      namespace='monthlyplans')),
    url(r'^saudeanamnese/', include('effectiveworkout.healthanamnese.urls',
                                    namespace='healthanamnese')),
    url(r'^config/', include('effectiveworkout.config.urls',
                                    namespace='config')),
    url(r'^exercise/', include('effectiveworkout.exercises.urls', namespace="exercise")),
    url(r'^api/v2/exercise/search/$',
        exercises_api_views.search,
        name='exercise-search'),
    url(r'^admin/', admin.site.urls),
]

from django.contrib import admin
from effectiveworkout.settings import MEDIA_ROOT, MEDIA_URL
from effectiveworkout.usersprofiles.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'foto_perfil', 'telefone', 'planomensalidade')
    fields = ('user','avatar', 'planomensalidade', 'datainicio', 'datanascimento', 'idade', 'cc', 'nif', 'telefone', 'telefone2',
              'ativo')

    date_hierarchy = 'created_at'
    search_fields = ('pk', 'user', 'telefone', 'created_at')
    list_filter = ('created_at',)

    def foto_perfil(self, obj):
        return '<img width="32px" src="{}" />'.format(MEDIA_URL + str(obj.avatar))

    foto_perfil.allow_tags = True
    foto_perfil.short_description = 'foto'

    # Remove botão add
    def get_form(self, request, obj=None, **kwargs):  # Just added this override
        form = super(UserProfileAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['planomensalidade'].widget.can_add_related = False
        return form

    # Cria link no item do segundo campo da lista.
    def foo_link(self, obj):
        return u'<a href="/nome/%s/">%s</a>' % (obj.user.name, obj)

    foo_link.allow_tags = True
    foo_link.short_description = "user"

    def __init__(self, *args, **kwargs):
        super(UserProfileAdmin, self).__init__(*args, **kwargs)
        self.list_display_links = ('pk', 'user')

    def pk(self, obj):
        nmatricula = UserProfile.objects.get(pk=obj.pk)
        return str(nmatricula)

    pk.short_description = 'Nome'


admin.site.register(UserProfile, UserProfileAdmin)
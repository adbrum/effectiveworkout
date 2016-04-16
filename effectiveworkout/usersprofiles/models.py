from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from effectiveworkout.monthlyplans.models import PlanoMensalidade

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.pk, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user')
    avatar = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    planomensalidade = models.ForeignKey(PlanoMensalidade, verbose_name='Planos e mensalidade')
    datainicio = models.DateField('Data de inicio')
    datanascimento = models.DateField('Data de nascimento')
    idade = models.IntegerField('Idade', blank=True)
    cc = models.CharField('Cartão do Cidadão', max_length=12)
    nif = models.IntegerField('Número de Identifacação Fiscal')
    telefone = models.CharField('Nº Telefone', max_length=9)
    telefone2 = models.CharField('Nº Telefone urgência', max_length=9, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    ativo = models.BooleanField('Ativo', default=True, choices=BOOL_CHOICES)

    class Meta:
        verbose_name_plural = 'Perfis de Utilizadores'
        verbose_name = 'Perfil do utilizador'
        ordering = ('user__first_name',)

    def get_absolute_url(self):
        return reverse('editatleta', kwargs={'pk': self.pk})

    def __str__(self):
        return self.user.get_full_name()
    # def __str__(self):
    #     return str(self.pk)  # self.nome + ' ' + self.sobrenome
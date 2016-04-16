from django import forms
from django.contrib.auth.models import User, Group
from django.forms import ModelForm
from django.utils.safestring import mark_safe
from effectiveworkout.healthanamnese.models import SaudeAnamnese
from effectiveworkout.monthlyplans.models import PlanoMensalidade
from effectiveworkout.usersprofiles.models import UserProfile

BOOL_CHOICES = ((True, 'Sim'), (False, 'Não'))


class UserProfileForm(ModelForm):
    datainicio = forms.DateField(label='Data inicio',
                                 widget=forms.DateInput(
                                     attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date mask-date',
                                            ' data-provide': 'datepicker',
                                            'data-date-format': 'dd/mm/yyyy'}))
    datanascimento = forms.DateField(label='Data de Nascimento',
                                     widget=forms.DateInput(
                                         attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
                                                ' data-provide': 'datepicker',
                                                'data-date-format': 'dd/mm/yyyy'}))
    idade = forms.CharField(label='Idade', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Idade', 'class': 'form-control'}))
    nif = forms.CharField(label='NIF', widget=forms.TextInput(
        attrs={'placeholder': 'Número de identificação fiscal', 'class': 'form-control'}))
    cc = forms.CharField(label='CC', widget=forms.TextInput(
        attrs={'placeholder': 'Cartão do Cidadão', 'class': 'form-control'}))

    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato', 'class': 'form-control'}))
    telefone2 = forms.CharField(label='Telefone 2', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato urgente', 'class': 'form-control'}))

    planomensalidade = forms.ModelChoiceField(PlanoMensalidade.objects.all(),
                                              label=('Plano'),
                                              widget=forms.Select(attrs={'placeholder': 'Plano mensalidade',
                                                                         'class': 'form-control input-sm medio required_form'})
                                              )

    class Meta:
        model = UserProfile
        fields = ['datainicio', 'datanascimento', 'idade', 'nif', 'cc', 'telefone',
                  'telefone2', 'planomensalidade']


class EditUserProfileForm(ModelForm):
    ativo = forms.ChoiceField(BOOL_CHOICES,
                              label=('Ativo'),
                              widget=forms.Select(attrs={'placeholder': '--',
                                                         'class': 'form-control input-sm medio required_form'})
                              )

    datainicio = forms.DateField(label='Data inicio',
                                 widget=forms.DateInput(
                                     attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
                                            ' data-provide': 'datepicker',
                                            'data-date-format': 'dd/mm/yyyy'}))
    datanascimento = forms.DateField(label='Data de Nascimento',
                                     widget=forms.DateInput(
                                         attrs={'placeholder': 'dd/mm/yyyy', 'class': 'form-control date',
                                                ' data-provide': 'datepicker',
                                                'data-date-format': 'dd/mm/yyyy'}))
    idade = forms.CharField(label='Idade', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Idade', 'class': 'form-control'}))
    nif = forms.CharField(label='NIF', widget=forms.TextInput(
        attrs={'placeholder': 'Número de identificação fiscal', 'class': 'form-control'}))
    cc = forms.CharField(label='CC', widget=forms.TextInput(
        attrs={'placeholder': 'Cartão do Cidadão', 'class': 'form-control'}))

    telefone = forms.CharField(label='Telefone', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato', 'class': 'form-control'}))
    telefone2 = forms.CharField(label='Telefone 2', required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Contato urgente', 'class': 'form-control'}))

    planomensalidade = forms.ModelChoiceField(PlanoMensalidade.objects.all(),
                                              label=('Plano'),
                                              widget=forms.Select(attrs={'placeholder': 'Plano mensalidade',
                                                                         'class': 'form-control input-sm medio required_form'})
                                              )

    class Meta:
        model = UserProfile
        fields = ['datainicio', 'datanascimento', 'idade', 'nif', 'cc',
                  'telefone',
                  'telefone2', 'planomensalidade']


# Cria o form de criação de users
class AddUserForm(forms.Form):
    error_messages = {
        'err_pass': (u"A Palavra-passe não coincide."),
        'err_dup': (u"Nome de utilizador já existente."),
        'err_email': (u"Já existe um utilizador com este e-mail."),
        'required': (u"Campo de preenchemento obrigatório."),
    }

    username = forms.CharField(max_length=30, label=(u'Nome utilizador'), widget=forms.TextInput(
        attrs={'class': 'form-control input-sm medio required_form', 'autofocus': "autofocus"}))
    first_name = forms.CharField(max_length=30, label=(u'Nome'),
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    last_name = forms.CharField(required=False, max_length=30, label=(u'Sobrenome'),
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio'}))
    email = forms.EmailField(max_length=75, label=(u'E-mail'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio required_form'}),
                               max_length=128, label=(u'Palavra-passe'))
    password_ack = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio required_form'}),
        max_length=128, label=(u'Confirmar Palavra-passe'))

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(self.error_messages['err_dup'])

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError(self.error_messages['err_email'])

    def clean_password_ack(self):
        password = self.cleaned_data.get("password")
        password_ack = self.cleaned_data.get("password_ack")
        if password and password_ack and password != password_ack:
            raise forms.ValidationError(
                self.error_messages['err_pass'])
        return password_ack

    class Meta:
        model = User
        fields = ("username", "password", "email")
        pass


# Formulário para a edição do utilizador
class EditUserForm(ModelForm):
    error_messages = {
        'err_pass': (u"A Palavra-passe não coincide."),
        'err_dup': (u"Nome de utilizador já existente."),
        'err_email': (u"Já existe um utilizador com este e-mail."),
        'required': (u"Campo de preenchimento obrigatório."),
    }

    username = forms.CharField(max_length=30,
                               label=(u'Nome utilizador'),
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form',
                                                             'autofocus': "autofocus"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30,
                                 label=(u'Nome'),
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    last_name = forms.CharField(required=False, max_length=30,
                                label=(u'Sobrenome'),
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio'}))
    email = forms.EmailField(max_length=75,
                             label=(u'E-mail'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))

    def __init__(self, username, email, listaGupos, *args, **kwargs):
        super(EditUserForm, self).__init__(*args, **kwargs)
        self.username = username
        self.email = email
        # self.fields['grupos'].initial = Group.objects.filter(name=[int(idGroup.id) for idGroup in listaGupos])

    def clean_username(self):
        username = self.cleaned_data["username"]
        if self.username != username:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(self.error_messages['err_dup'])
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if self.email != email:
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(self.error_messages['err_email'])
        else:
            return email

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        pass


# Formulário para a ver a ficha do utilizador
class FichaUserForm(ModelForm):
    username = forms.CharField(max_length=30,
                               label=(u'Nome utilizador'),
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                             'disabled': "disabled"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30,
                                 label=(u'Nome'),
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                               'disabled': "disabled"}
                                                        )
                                 )
    last_name = forms.CharField(required=False,
                                max_length=30,
                                label=(u'Sobrenome'),
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                              'disabled': "disabled"}
                                                       )
                                )
    email = forms.EmailField(max_length=75,
                             label=(u'E-mail'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                           'disabled': "disabled"}
                                                    )
                             )

    grupos = forms.ModelMultipleChoiceField(Group.objects.all(), label=(u'Perfil'), widget=forms.SelectMultiple(
        attrs={'multiple class': 'form-control', 'disabled': "disabled"}))

    def __init__(self, listaGupos, *args, **kwargs):
        super(FichaUserForm, self).__init__(*args, **kwargs)
        self.fields['grupos'].queryset = Group.objects.filter(id__in=[int(idGroup.id) for idGroup in listaGupos])
        self.fields['grupos'].initial = Group.objects.filter(id__in=[int(idGroup.id) for idGroup in listaGupos])


class PasswordChangeFormReset(forms.Form):
    error_messages = {
        'password_mismatch': (u"As passwords não coincidem."),
    }

    password1 = forms.CharField(label=("Nova Password"),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control input-sm medio required_form'}))

    password2 = forms.CharField(label=("Nova Password (novamente)"),
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control input-sm medio required_form'}))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordChangeFormReset, self).__init__(*args, **kwargs)

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):

        self.user.set_password(self.cleaned_data["password1"])
        if commit:
            self.user.save()
        return self.user


class MeuPerfilForm(ModelForm):
    error_messages = {
        'err_pass': (u"A Palavra-passe não coincide."),
        'err_dup': (u"Nome de utilizador já existente."),
        'err_email': (u"Já existe um utilizador com este e-mail."),
        'required': (u"Campo de preenchimento obrigatório."),
        'password_mismatch': (u"As palavra-passe não coincidem."),
        'password_incorrect': (u"As palavra-passe não coincidem."),
    }

    username = forms.CharField(max_length=30,
                               label=(u'Nome utilizador'),
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form',
                                                             'autofocus': "autofocus"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30,
                                 label=(u'Nome'),
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    last_name = forms.CharField(required=False,
                                max_length=30,
                                label=(u'Sobrenome'),
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio'}))
    email = forms.EmailField(max_length=75,
                             label=(u'E-mail'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio required_form'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio required_form'}),
                               max_length=128,
                               label=(u'Palavra-passe atual'))

    password1 = forms.CharField(required=False,
                                label=("Palavra-passe"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio'}))

    password2 = forms.CharField(required=False,
                                label=("Palavra-passe (novamente)"),
                                widget=forms.PasswordInput(attrs={'class': 'form-control input-sm medio'}))

    def __init__(self, username, email, userAtual, *args, **kwargs):
        super(MeuPerfilForm, self).__init__(*args, **kwargs)
        self.username = username
        self.email = email
        self.userAtual = userAtual

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not self.userAtual.check_password(password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return password

    def clean_username(self):
        username = self.cleaned_data["username"]
        if self.username != username:
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(self.error_messages['err_dup'])
        else:
            return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if self.email != email:
            try:
                User.objects.get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(self.error_messages['err_email'])
        else:
            return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2:
            if password1 != password2:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'])
        return password2

    def save(self, commit=True):

        self.userAtual.set_password(self.cleaned_data["password1"])
        if commit:
            if len(str(self.cleaned_data["password1"])) > 0:
                self.userAtual.save()
        return self.userAtual

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password")
        pass


class FichaMeuPerfilForm(ModelForm):
    username = forms.CharField(max_length=30,
                               label=(u'Nome utilizador'),
                               widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                             'disabled': "disabled"}
                                                      )
                               )
    first_name = forms.CharField(max_length=30,
                                 label=(u'Nome'),
                                 widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                               'disabled': "disabled"}
                                                        )
                                 )
    last_name = forms.CharField(required=False,
                                max_length=30,
                                label=(u'Sobrenome'),
                                widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                              'disabled': "disabled"}
                                                       )
                                )
    email = forms.EmailField(max_length=75,
                             label=(u'E-mail'),
                             widget=forms.TextInput(attrs={'class': 'form-control input-sm medio',
                                                           'disabled': "disabled"}
                                                    )
                             )

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")

class HorizontalRadioRenderer(forms.RadioSelect.renderer):
    def render(self):
        return mark_safe(u'\n'.join([u'%s\n' % w for w in self]))


class HealthAnamneseForm(ModelForm):
    # atleta = forms.IntegerField(label='Nº do atleta', widget=forms.TextInput(
    #     attrs={'class': 'form-control', 'style': 'width:50px'}))

    # DOENÇA CONHECIDA CARDIOVASCULAR E/OU PULMONAR#
    quest01 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=('Doença cardiovascular ou pulmonar (asma, bronquite, etc.)'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest02 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=('Doença metabólica (tiroide, renal ou hepática'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest03 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=('Diabetes tipo I ou II'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest04 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=('Dor ou desconforto no peito em repouso ou exercício'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest05 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=('Desmaios, tonturas ou perda de consciência'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest06 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=(
                                    'Dificuldades em respirar ou problemas respiratórios repentinos durante a noite'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest07 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=(
                                    'Palpitações ou taquicardia'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest08 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=(
                                    'Dor severa nas pernas durante a marcha'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest09 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                label=(
                                    'Tensão arterial maior que 140/90 mm Hg ou sob medicação'),
                                widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                         attrs={'class': 'form-control input-sm medio required_form'})
                                )

    quest010 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Edema no tornozelo'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    # DOENÇA CORONÁRIA#
    quest011 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Colesterol Total maior que 240 mg/dl ou sob medicação'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest012 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'História familiar de enfarte do miocárdio ou morte súbita do pai/mãe ou outro familiar em primeiro grau antes dos 55/65 anos'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest013 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Índice de Massa Corporal maior que 30 (kg/m2)'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'})
                                 )

    quest014 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Fumador ou que tenha deixado de fumar nos últimos 6 mese'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest015 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Sem programa de exercício regular há mais de 6 meses'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    # OUTRAS SITUAÇÕES ASSOCIADAS AO SEU ESTADO DE SAÚDE#
    quest016 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Algum problema de saúde não mencionado e/ou qualquer outro fator condicionante do programa de exercício físico a elaborar?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest017 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Doença recente?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest018 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Hospitalização recente?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest019 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Procedimentos cirúrgicos?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    # ANAMINESE DESPORTIVA#
    quest020 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Pratica algum tipo de exercício regularmente fora do KC?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    quest021 = forms.CharField(required=False,
                               label=(
                                   'Se sim, qual e quantas vezes por semana?'),
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control input-sm'}))

    quest022 = forms.CharField(required=False,
                               label=(
                                   'Alguma observação importante a declarar?'),
                               widget=forms.Textarea(
                                   attrs={'class': 'form-control input-sm'}))

    quest023 = forms.ChoiceField(BOOL_CHOICES, required=True,
                                 label=(
                                     'Declara que compreendeu integralmente o conteúdo deste documento?'),
                                 widget=forms.RadioSelect(renderer=HorizontalRadioRenderer,
                                                          attrs={'class': 'form-control input-sm medio required_form'}))

    class Meta:
        model = SaudeAnamnese
        fields = '__all__'
        exclude = ['atleta']

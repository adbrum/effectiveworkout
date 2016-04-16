from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r
from effectiveworkout.monthlyplans.models import PlanoMensalidade

from effectiveworkout.usersprofiles.forms import UserProfileForm, EditUserProfileForm, EditUserForm, AddUserForm
from effectiveworkout.usersprofiles.models import UserProfile


@login_required
def listsubscription(request, *args, **kwargs):
    list_ = PlanoMensalidade.objects.all()

    if list_:
        data = UserProfile.objects.all()
        if not data:
            context = {
                'list': data,
                'tamLista': 0,
            }

            return render(request, "usersprofiles/index.html", context)
        else:
            context = {
                'list': data,
                'tamLista': 1,
            }

            return render(request, "usersprofiles/index.html", context)
    else:
        context = {
            'list_': 0
        }

        return render(request, "usersprofiles/index.html", context)


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'usersprofiles/add.html',
                  {'form': AddUserForm(), 'form2': UserProfileForm()})


def empty_prototipo_form(request):
    return render(request, 'usersprofiles/subscription_form.html',
                  {'form': UserProfileForm()})


@login_required
def create(request):
    # saveNew = True
    # form = UserProfileForm(request.POST or None)

    form = AddUserForm(request.POST or None)
    form2 = UserProfileForm(request.POST or None)
    if not (form.is_valid() and form2.is_valid()):
        return render(request, 'usersprofiles/add.html', locals())
    else:
        # user = User.objects.create(**form2.cleaned_data)
        # user.set_password(form.cleaned_data['password'])
        user = User(username=form.cleaned_data['username'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    email=form.cleaned_data['email'],
                    password=form.cleaned_data['password']

                    )

        # encripta a password
        user.set_password(form.cleaned_data['password'])

        user.save()
        # form.save()
        UserProfile.objects.create(**form2.cleaned_data, user_id=user.pk)
        # form2.save()
        return HttpResponseRedirect(r('usersprofiles:success'))


@login_required
def editUserProfile(request, pk):
    perfil = get_object_or_404(UserProfile, pk=pk)
    user = get_object_or_404(User, pk=perfil.user_id)

    argUser = user.username
    argEmail = user.email

    # listaGrupos = user.groups.filter(name='utilizador')

    form = EditUserProfileForm(request.POST or None, instance=perfil)
    form2 = EditUserForm(argUser, argEmail, request.POST or None, instance=user)

    # form2 = EditUserForm(argUser, argEmail, listaGrupos, request.POST or None, instance=user)
    if not (form.is_valid() or form.is_valid()):
        return render(request, 'usersprofiles/edit.html', locals())
    else:
        form.save()
        return HttpResponseRedirect(r('usersprofiles:success'))


@login_required
def success(request):
    return render(request, 'usersprofiles/subscription_success.html')


@login_required
def delDataModalUserProfile(request):
    id_list = []
    if request.is_ajax():
        select = request.POST.getlist('valores[]')

        for pk in select:
            id_list.append(int(pk))

    users = UserProfile.objects.filter(pk__in=id_list, ativo=True)

    return render(request, 'usersprofiles/desativar_modal.html', {'users': users})


@login_required
def activeDataModalUserProfile(request):
    id_list = []
    if request.is_ajax():
        select = request.POST.getlist('valores[]')

        for pk in select:
            id_list.append(int(pk))

    user = UserProfile.objects.filter(pk__in=id_list, ativo=False)
    # for i in user:
    #     i.user.us
    return render(request, 'usersprofiles/ativar_modal.html', {'users': user})


@login_required
def delConfirmeUserProfile(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        UserProfile.objects.filter(pk=valor).update(ativo=False)

    return HttpResponseRedirect(r('usersprofiles:list'))


@login_required
def activeConfirmeUserProfile(request, *args, **kwargs):
    select = request.POST.getlist('valores_list[]')
    for valor in select:
        UserProfile.objects.filter(pk=valor).update(ativo=True)

    return HttpResponseRedirect(r('usersprofiles:list'))


def fichaUserProfile(request, *args, **kwargs):
    idUserProfile = kwargs['idUserProfile']

    editar = True
    saveNew = False

    users = UserProfile.objects.get(id=idUserProfile)
    argCode = users.pk

    if request.method == 'GET':
        url = reverse('/inscricao/ficha/' + idUserProfile)
        return HttpResponseRedirect(url)
    else:

        return HttpResponseRedirect(r('usersprofiles:list'))

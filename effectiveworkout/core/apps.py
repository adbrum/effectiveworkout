from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'effectiveworkout.core'
    verbose_name = 'Administração Effective Workout'


class UsersProfilesConfig(AppConfig):
    name = 'effectiveworkout.usersprofiles'
    verbose_name = 'Inscrições atletas'


class AssiduousnessConfig(AppConfig):
    name = 'effectiveworkout.assiduousness'
    verbose_name = 'Assiduidade'


class HealthanamneseConfig(AppConfig):
    name = 'effectiveworkout.healthanamnese'
    verbose_name = 'Saude e Anamnese'


class MonthlyplansConfig(AppConfig):
    name = 'effectiveworkout.monthlyplans'
    verbose_name = 'Planos mensais'

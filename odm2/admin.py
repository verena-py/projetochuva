
from django.apps import apps #registo que armazena uma lista de modelos disponiveis
from django.contrib import admin
from django.contrib.admin.sites import AlreadyRegistered

app_models = apps.get_app_config('odm2').get_models()
list = []
for model in app_models:
    list.append(model)
    try:
        admin.site.register(model)
    except AlreadyRegistered:
        pass

#print(list)



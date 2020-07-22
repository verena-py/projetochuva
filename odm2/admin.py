
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


#Actions -Actions are performed by people and may have a result.
#Datasets - Enables grouping of results into a larger dataset.
#FeatureActions - Provides flexible linkage between Actions and the SamplingFeatures on which or at which they were performed.
#Methods - The procedure used to perform an action.
#Organizations - A group of people.
#People - Individuals that perform actions.
#Processing Levels - Levels to which data have been quality controlled.
#Related Actions - Enables specifying relationships among Actions (e.g., workflows, etc.)
#Results - The result of an action.
#Sampling Features - Where or on what an action was performed.
#Taxonomic Classifiers - Terms for classifying results.
#Units - Units of measure.
#Variables - What was observed.
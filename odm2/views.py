from django.shortcuts import render
from .models import Timeseriesresults, Timeseriesresultvalues, CvCensorcode, CvQualitycode, Units, Organizations
from hydro_api.ana.hidro.serie_temporal import SerieTemporal
import pandas as pd

def paginainicial(request):
    context = {}
    return render(request, 'index.html',context)

def projeto(request):
    context = {}
    return render(request,'odm2/base.html',context)

def anual(request):
    stations = {'1036050':1}
    result = Timeseriesresults.objects.get(pk=stations['1036050'])
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue','valuedatetime')
    dic = {'Date': [], 'Data': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['Data'].append(i[0])
    df = pd.DataFrame(dic)
    print(df)

    return render(request,'odm2/anual.html')

def media(request):

    result = Timeseriesresults.objects.get(pk=1)#esse
    censor = CvCensorcode.objects.get(name='Unknown')
    quality = CvQualitycode.objects.get(name='Unknown')
    units_time = Units.objects.get(pk=1)
    time_inter = 1
    value_utc = 1
    source = Organizations.objects.get(pk=1)
    station = result.resultid.featureactionid.samplingfeatureid.samplingfeaturename

    rain = SerieTemporal(code='1036050', type_data='2')#issodaqpbaixo
    df = pd.DataFrame(rain.data)
    df = df.reset_index()
    df.drop_duplicates(df.columns[df.columns.isin(["Date"])], keep="last",
                       inplace=True)  # Seleciona apenas a coluna data ignorando o index, o keep last mantém apenas o último dado duplicado (ou seja o consistido que nos interessa)
    df = df.reset_index()
    df = df.drop(['index', 'Consistence'], axis=1)
    df = df.set_index('Date')
    dados = df
    time_serie_result_list = []

    for i in dados.index:
        obj_ts = Timeseriesresultvalues(resultid=result, censorcodecv=censor,
                                        qualitycodecv=quality, valuedatetimeutcoffset=value_utc,
                                        timeaggregationinterval=time_inter,
                                        timeaggregationintervalunitsid=units_time,
                                        valuedatetime=i,
                                        datavalue=dados[dados.columns.values[0]][i])


        time_serie_result_list.append(obj_ts)
    Timeseriesresultvalues.objects.bulk_create(time_serie_result_list)

    return render(request,'odm2/media.html')



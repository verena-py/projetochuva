from django.shortcuts import render
from .models import Timeseriesresults, Timeseriesresultvalues, CvCensorcode, CvQualitycode, Units, Organizations
from django.utils import timezone
import pandas as pd
from django.utils import timezone
import datetime
from hidrocomp.series import Rainfall
import plotly.offline as pyo
import plotly.graph_objs as go
from functools import reduce
import hydro_api
from hydro_api.ana.hidro.serie_temporal import SerieTemporal
import matplotlib.pyplot as plt

datetime.datetime.now(tz=timezone.utc)



def paginainicial(request):
    context={}
    return render(request, 'index.html',context)

def projeto(request):
    context = {}

    return render(request,'odm2/base.html',context)

def consulta(request):
    stations = {'1036050':1}
    result = Timeseriesresults.objects.get(pk=stations['1036050'])
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue','valuedatetime')
    dic = {'Date': [], 'Data': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['Data'].append(i[0])
    df = pd.DataFrame(dic)
    #print(df)

    return render(request, 'odm2/consulta.html')

def dados(request):
    context = {}
    #anotacoes.txt
    return render(request,'odm2/dados.html')

def gantt(request):

    rainfall = Rainfall(station=['1036050', '1036008', '1036007', '1036064', '1036005',
                                 '1036009', '936066', '936065', '936022', '936020', '1036003'], source='ANA')
    fig, data = rainfall.gantt(title="Gráfico gantt da bacia hidrográfica do Rio Piaui, AL")
    pyo.plot(fig, filename="odm2/gantt_riopiaui.html")

    return render(request,'odm2/gantt.html')

def piacabucu(request):
    #consulta ao banco, apenas estações de piacabucu

    result = Timeseriesresults.objects.get(pk=1)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036050': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036050'].append(i[0])
    df1 = pd.DataFrame(dic)

    result = Timeseriesresults.objects.get(pk=2)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036008': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036008'].append(i[0])
    df2 = pd.DataFrame(dic)

    result = Timeseriesresults.objects.get(pk=12)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036007': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036007'].append(i[0])
    df3 = pd.DataFrame(dic)

    result = Timeseriesresults.objects.get(pk=13)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036004': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036004'].append(i[0])
    df5 = pd.DataFrame(dic)

    data_frames = [df1, df2, df3, df5]
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['Date'],
                                                    how='outer'), data_frames)
    df_merged = df_merged.sort_values(by='Date')
    df_merged = df_merged.reset_index(drop=True)

    trace1 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['1036050'],
                        mode='lines',
                        name='1036050')
    trace2 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['1036008'],
                        mode='lines',
                        name='1036008')
    trace3 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['1036007'],
                        mode='lines',
                        name='1036007')
    trace4 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['1036004'],
                        mode='lines',
                        name='1036004')

    grafico = [trace1,trace2,trace3,trace4]

    layout = go.Layout(title='Dados de chuva nas estações de Piaçabuçu',
                       yaxis={'title': 'Dados (mm)'},
                       xaxis={'title': 'Tempo'})
    fig = go.Figure(data=grafico, layout=layout)
    pyo.plot(fig, filename="odm2/graficopiacabucu.html")

    return render(request,'odm2/piacabucu.html')

def exportar(request):
    #exporta arquivo xls contendo as medições da bacia

    result = Timeseriesresults.objects.get(pk=1)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036050': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036050'].append(i[0])
    df1 = pd.DataFrame(dic)


    result = Timeseriesresults.objects.get(pk=2)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036008': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036008'].append(i[0])
    df2 = pd.DataFrame(dic)


    result = Timeseriesresults.objects.get(pk=12)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036007': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036007'].append(i[0])
    df3 = pd.DataFrame(dic)


    result = Timeseriesresults.objects.get(pk=13)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036005': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036005'].append(i[0])
    df4 = pd.DataFrame(dic)



    result = Timeseriesresults.objects.get(pk=14)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036064': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036064'].append(i[0])
    df5 = pd.DataFrame(dic)


    result = Timeseriesresults.objects.get(pk=15)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036009': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036009'].append(i[0])
    df6 = pd.DataFrame(dic)



    result = Timeseriesresults.objects.get(pk=7)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936066': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936066'].append(i[0])
    df7 = pd.DataFrame(dic)



    result = Timeseriesresults.objects.get(pk=8)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936065': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936065'].append(i[0])
    df8 = pd.DataFrame(dic)



    result = Timeseriesresults.objects.get(pk=9)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936022': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936022'].append(i[0])
    df9 = pd.DataFrame(dic)


    result = Timeseriesresults.objects.get(pk=10)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936020': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936020'].append(i[0])
    df10 = pd.DataFrame(dic)



    result = Timeseriesresults.objects.get(pk=11)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '1036003': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['1036003'].append(i[0])
    df11 = pd.DataFrame(dic)


    dfs = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11]
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['Date'],
                                                    how='outer'), dfs)

    df_merged = df_merged.sort_values(by='Date')
    df_merged = df_merged.reset_index(drop=True)
    df_merged['Date'] = df_merged['Date'].apply(lambda a: pd.to_datetime(a).date())
    df_merged.to_excel("medicoes_baciapiauialagoas.xlsx")


    return render(request, 'odm2/exportar.html')


def norte(request):

    result = Timeseriesresults.objects.get(pk=7)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936066': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936066'].append(i[0])
    df1 = pd.DataFrame(dic)

    result = Timeseriesresults.objects.get(pk=8)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936065': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936065'].append(i[0])
    df2 = pd.DataFrame(dic)

    result = Timeseriesresults.objects.get(pk=9)
    data = Timeseriesresultvalues.objects.filter(resultid=result).values_list('datavalue', 'valuedatetime')
    dic = {'Date': [], '936022': []}
    for i in data:
        dic['Date'].append(i[1])
        dic['936022'].append(i[0])
    df3 = pd.DataFrame(dic)

    data_frames = [df1, df2, df3]
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['Date'],
                                                    how='outer'), data_frames)
    df_merged = df_merged.sort_values(by='Date')
    df_merged = df_merged.reset_index(drop=True)

    trace1 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['936066'],
                        mode='lines',
                        name='936066')
    trace2 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['936065'],
                        mode='lines',
                        name='936065')
    trace3 = go.Scatter(x=df_merged['Date'],
                        y=df_merged['936022'],
                        mode='lines',
                        name='936022')

    grafico = [trace1,trace2,trace3]

    layout = go.Layout(title='Dados de chuva nas estações localizadas ao norte da Bacia H. do Rio Piauí',
                       yaxis={'title': 'Dados (mm)'},
                       xaxis={'title': 'Tempo'})
    fig = go.Figure(data=grafico, layout=layout)
    pyo.plot(fig, filename="odm2/norte.html")


    return render(request, 'odm2/norte.html')



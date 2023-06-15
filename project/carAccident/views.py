from django.shortcuts import render, redirect
from plotly.offline import plot
from plotly.graph_objs import Scatter

# Create your views here.
from django.http import HttpResponse
import plotly.express as px

from .models import *
import json 
import math

import pandas as pd
from .forms import CaraccidentForm


# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form =  CaraccidentForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form =  CaraccidentForm()  
    return render(request,'index.html',{'form':form})  
def show(request, page=1):  
    caraccidents = Caraccident.objects.all()
    row = 100
    min = 1
    max = math.ceil(len(caraccidents)/row)
    return render(request,"show.html",{'caraccidents':caraccidents[(page-1)*row:page*row], 
                                       'page': page, 
                                       'prev': page - 1 if page > min else min, 
                                       'next': page + 1 if page < max else max,
                                       'min': min, 'max': max})  
def edit(request, id):  
    caraccident = Caraccident.objects.get(id=id)  
    return render(request,'edit.html', {'caraccident':caraccident})  
def update(request, id):  
    caraccident = Caraccident.objects.get(id=id)  
    form =  CaraccidentForm(request.POST, instance = caraccident)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'caraccident': caraccident})  
def destroy(request, id):  
    caraccident = Caraccident.objects.get(id=id)  
    caraccident.delete()  
    return redirect("/show")  

def index(request):
    df = pd.DataFrame(list(zip(list(AmountAccidentbymonth().keys()),list(AmountAccidentbymonth().values()))), columns=['month', 'count'])
    print(df)
    fig = px.line(df, y='count', x='month', title='Amount of accident per month (2022)')
    plot_div = plot(fig, output_type='div')

    x = ['rainy', 'sunny', 'snow']
    y = [52, 104, 33]
    df = pd.DataFrame(list(zip(list(GetDeathByGender().keys()),list(GetDeathByGender().values()))), columns=['gender', 'count'])
    print(df)
    fig = px.pie(df, values='count', names='gender', title='Death by gender(2022)')
    plot2_div = plot(fig, output_type='div')
     
    df = pd.DataFrame(list(zip(list(Weather().keys()),list(Weather().values()))), columns=['weather', 'count'])
    print(df)
    fig = px.pie(df, values='count', names='weather', title='Percentage of weather conditions under which accidents happened(2022)')
    plot3_div = plot(fig, output_type='div')

    df = pd.DataFrame(list(zip(list(GetLevelofinjurybygender()['male'].keys()),list(GetLevelofinjurybygender()['male'].values()))), columns=['male', 'count'])
    print(df)
    fig = px.pie(df, values='count', names='male', title='Level of injury for male (2022)')
    plot4_div = plot(fig, output_type='div')

    df = pd.DataFrame(list(zip(list(GetLevelofinjurybygender()['female'].keys()),list(GetLevelofinjurybygender()['female'].values()))), columns=['female', 'count'])
    print(df)
    fig = px.pie(df, values='count', names='female', title='Level of injury for female (2022)')
    plot5_div = plot(fig, output_type='div')
    return render(request, "home.html", context={'plot_div': plot_div,'a_div': plot2_div,'b_div': plot3_div , 'c_div': plot4_div, 'd_div': plot5_div})


def database_test(request):
    # return HttpResponse(json.dumps(AmountAccidentbymonth()))
    return HttpResponse(json.dumps(list(GetLevelofinjurybygender()['male'].values())))
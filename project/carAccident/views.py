from django.shortcuts import render, redirect
from plotly.offline import plot
from plotly.graph_objs import Scatter

# Create your views here.
from django.http import HttpResponse
import plotly.express as px

from .models import *
import json 

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
def show(request):  
    accidents = Caraccident.objects.all()  
    return render(request,"show.html",{'accidents':accidents})  
def edit(request, id):  
    accident = Caraccident.objects.get(id=id)  
    return render(request,'edit.html', {'accident':accident})  
def update(request, id):  
    accident = Caraccident.objects.get(id=id)  
    form =  CaraccidentForm(request.POST, instance = accident)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'accident': accident})  
def destroy(request, id):  
    accident = Caraccident.objects.get(id=id)  
    accident.delete()  
    return redirect("/show")  

def index(request):
    x_data = list(AmountAccidentbymonth().keys())
    y_data = list(AmountAccidentbymonth().values())
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    x = ['rainy', 'sunny', 'snow']
    y = [52, 104, 33]
    df = pd.DataFrame(list(zip(list(GetDeathByGender().keys()),list(GetDeathByGender().values()))), columns=['gender', 'count'])
    print(df)
    fig = px.pie(df, values='count', names='gender', title='Death by gender')
    plot2_div = plot(fig, output_type='div')
     
    df = pd.DataFrame(list(zip(list(Weather().keys()),list(Weather().values()))), columns=['weather', 'count'])
    print(df)
    fig = px.pie(df, values='count', names='weather', title='Weather conditions at the time of the accident')
    plot3_div = plot(fig, output_type='div')

    df = pd.DataFrame(list(zip(list(GetLevelofinjurybygender()['male'].keys()),list(GetLevelofinjurybygender()['male'].values()))), columns=['male', 'count'])
    
    print(df)
    fig = px.pie(df, values='count', names='male', title='Level of injury for male')
    plot4_div = plot(fig, output_type='div')
    return render(request, "home.html", context={'plot_div': plot_div,'a_div': plot2_div,'b_div': plot3_div , 'c_div': plot4_div})


def database_test(request):
    # return HttpResponse(json.dumps(AmountAccidentbymonth()))
    return HttpResponse(json.dumps(list(GetLevelofinjurybygender()['male'].values())))
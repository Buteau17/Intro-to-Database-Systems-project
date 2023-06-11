from django.shortcuts import render
from plotly.offline import plot
from plotly.graph_objs import Scatter

# Create your views here.
from django.http import HttpResponse
import plotly.express as px

def index(request):
    x_data = [0,1,2,3]
    y_data = [x**2 for x in x_data]
    plot_div = plot([Scatter(x=x_data, y=y_data,
                        mode='lines', name='test',
                        opacity=0.8, marker_color='green')],
               output_type='div')

    x = ['rainy', 'sunny', 'snow']
    y = [52, 104, 33]
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', names='country', title='Population of European continent')
    plot2_div = plot(fig, output_type='div')
    return render(request, "index.html", context={'plot_div': plot_div,'a_div': plot2_div })

from .models import *

def database_test(request):
    x = list(Caraccident.objects.all().values())
    return HttpResponse(x)
from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json
from .models import Stock
from .forms import StockForm


#Publishable API Token: pk_e72e1d360c58425e8a038cb4a8409963 

# Create your views here.
def home(request):
    if request.method=='POST':
        ticker=request.POST['ticker']
        api_request=requests.get('https://cloud.iexapis.com/stable/stock/'+ticker+'/quote?token=pk_e72e1d360c58425e8a038cb4a8409963')
        try:
            response=json.loads(api_request.content)
        except Exception as e:
            response='error'
        return render(request, 'home.html', {'response':response})
    else:
        return render(request, 'home.html', {'ticker':'Enter a ticker symbol above.'})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method=='POST':
        form=StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock has been added!')
            return redirect(add_stock)
    else:
        stocks=Stock.objects.all()
        output_stocks=[]
        for stock in stocks:
            api_request=requests.get('https://cloud.iexapis.com/stable/stock/'+str(stock)+'/quote?token=pk_e72e1d360c58425e8a038cb4a8409963')
            try:
                response=json.loads(api_request.content)
                output_stocks.append(response)
            except Exception as e:
                response='error'
        return render(request, 'add_stock.html', {'stocks':stocks, 'output_stocks':output_stocks})


def delete(request, stock_id):
    item=Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, 'Stock has been deleted!')
    return redirect(add_stock) 


def delete_stock(request):
    stocks=Stock.objects.all()
    return render(request, 'delete_stock.html', {'stocks':stocks})
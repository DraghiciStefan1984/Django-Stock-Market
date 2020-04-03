from django.shortcuts import render
import requests
import json

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
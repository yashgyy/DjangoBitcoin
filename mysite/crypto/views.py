from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json

    price_requests=requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,BCH,ETH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD')
    price=json.loads(price_requests.content)


    api_requests=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_requests.content)
    return render(request,'home.html',{'api':api, 'price':price})
    
def prices(request):
    import requests
    import json
    if request.method=='POST':
        quote=request.POST['quote']
        quote=quote.upper()
        price_requests=requests.get('https://min-api.cryptocompare.com/data/pricemultifull?fsyms='+quote+'&tsyms=USD')
        crypto=json.loads(price_requests.content)
        return render(request,'prices.html',{'quote':quote,'crypto':crypto})
    else:
        return render(request,'prices.html',{'notfound':True})
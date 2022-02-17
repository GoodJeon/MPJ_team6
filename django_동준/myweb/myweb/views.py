from django.shortcuts import render, redirect
from django.http import HttpRequest

def index(request):
    return render(request, 'index.html')

def selectgu(request):
    list = [
        '종로구','중구','용산구','성동구','광진구',
        '동대문구','중랑구','성북구','강북구',
        '도봉구','노원구','은평구','서대문구',
        '마포구','양천구','강서구','구로구',
        '금천구','영등포구','동작구','관악구',
        '서초구','강남구','송파구','강동구']
    return render(request, 'selectgu.html', {'guList':list})

def get_post(request):
    if request.method == 'POST':
        gu = request.POST['gu']
        return render(request, 'guinfo.html', {'gu':gu})
    else:
        return redirect('selectgu')
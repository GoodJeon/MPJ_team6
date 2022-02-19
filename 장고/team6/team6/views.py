from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from numpyencoder import NumpyEncoder
import numpy as np
import pandas as pd
import json



def index(request):
    return render(request,'index.html')

def storepage(request):
    list = [
        '종로구', '중구', '용산구', '성동구', '광진구',
        '동대문구', '중랑구', '성북구', '강북구',
        '도봉구', '노원구', '은평구', '서대문구',
        '마포구', '양천구', '강서구', '구로구',
        '금천구', '영등포구', '동작구', '관악구',
        '서초구', '강남구', '송파구', '강동구']
    return render(request,'페이지2-2.html', {'guList': list})

def personpage(request):
    return render(request,'페이지2-1.html')

@csrf_exempt
def comeTodata(request):
    if 'gu' in request.POST:
        gu = request.POST['gu']
    moneymoney = pd.read_csv("C:\\workspaces\\team6\\team6\\templates\\moneypower.csv")
    gud = moneymoney[moneymoney['행정구_명']== gu ]
    # 성별 퍼센트 데이터 보내기
    male = (gud['남성_매출_금액'].sum())
    female = (gud['여성_매출_금액'].sum())
    m = int(male)
    f = int(female)
    mPer = round(m / (m + f) * 100)
    fPer = round(f / (m + f) * 100)

    # 분기 별, 요일별 총 생활인구 수
    mon = gud['월요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    tue = gud['화요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    wed = gud['수요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    thu = gud['목요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    fri = gud['금요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    sat = gud['토요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    sun = gud['일요일_매출_금액'].groupby(gud['기준_분기_코드']).sum().values



    # 분기 별, 연령대별 총 생활인구 수
    age10 = gud['연령대_10_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    age20 = gud['연령대_20_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    age30 = gud['연령대_30_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    age40 = gud['연령대_40_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    age50 = gud['연령대_50_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    age60 = gud['연령대_60_이상_매출_금액'].groupby(gud['기준_분기_코드']).sum().values


    # 분기 별, 시간대별 총 생활 인구 수
    t1 = gud['시간대_00~06_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    t2 = gud['시간대_06~11_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    t3 = gud['시간대_11~14_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    t4 = gud['시간대_14~17_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    t5 = gud['시간대_17~21_매출_금액'].groupby(gud['기준_분기_코드']).sum().values
    t6 = gud['시간대_21~24_매출_금액'].groupby(gud['기준_분기_코드']).sum().values



    result = {'gu': gu, 'm': mPer, 'f': fPer,'mon': mon, 'tue': tue, 'wed': wed, 'thu': thu, 'fri': fri, 'sat': sat, 'sun': sun,'age10': age10, 'age20': age20, 'age30': age30, 'age40': age40, 'age50': age50, 'age60': age60,'t1': t1, 't2': t2, 't3': t3, 't4': t4, 't5': t5, 't6': t6}
    result =(json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))
    return JsonResponse(result,safe=False)
#result에서 그냥 하면 오류나와서 narry형식 변환해줘야합니다(json.dumps(result, cls=NumpyEncoder, indent=4, ensure_ascii=False))
#그리고 jsonresponse에서 safe=false안해줘도 오류입니다.
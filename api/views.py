from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def fill_authors(request):
    '''填充作者数据'''
    if request.method == 'POST':
        str_data = str(request.body,encoding='utf-8')
        utf_data = json.loads(str_data,encoding='utf-8')
        print(utf_data[0:3])
        return HttpResponse('收到')
        pass
    else:
        return HttpResponse('ok')
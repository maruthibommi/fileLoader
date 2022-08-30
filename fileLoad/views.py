from calendar import c
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import pandas as pd
import json
from io import BytesIO


def home(request):
    return render(request,'fileLoad/Html_css_files/base.html')


def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        print("file upload of ", uploaded_file.name ," is successful")
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        df = pd.read_csv( BytesIO(request.FILES['file'].read().decode("utf-8")))
        json_records = df.reset_index().to_json(orient='records')
        arr = []
        arr = json.loads(json_records)
        context['d'] = arr
        context['url'] = fs.url(name)
        
    return render(request,'fileLoad/Html_css_files/mainLoad.html',context)


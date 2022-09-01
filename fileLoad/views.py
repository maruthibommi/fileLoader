from calendar import c
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.core.files.storage import Storage
import pandas as pd
import json
from io import BytesIO
import openpyxl

def read_file(file_name):
    fs = FileSystemStorage()
    if(fs.exists(file_name)):
        uploaded_file = fs.open(file_name)
        df = openpyxl.load_workbook(uploaded_file,data_only=True)
    for i in df.sheetnames:
        excel_data = list()
        for row in df[i].iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(cell.value)
            excel_data.append(row_data)
    return excel_data

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['documents']
        fs = FileSystemStorage()
        if(fs.exists(uploaded_file.name)):
            fs.delete(uploaded_file.name)
        name = fs.save(uploaded_file.name,uploaded_file)
        context['name'] = uploaded_file.name
        context['url'] = fs.url(name)
        context['excel_data'] = read_file(context['name'])
        
    return render(request,'fileLoad/Html_css_files/mainLoad.html',context)
    

def validate(request):
    context = {}
    if(request.method == 'POST'):
        context['name'] = request.POST['file_name']
        fs = FileSystemStorage()
        context['excel_data'] = read_file(context['name'])
        return render(request,'fileLoad/Html_css_files/validate.html',context)
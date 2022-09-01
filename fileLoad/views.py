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



def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['documents']
        #print("file upload of ", uploaded_file.name ," is successful")
        fs = FileSystemStorage()
        s = Storage()
        if(fs.exists(uploaded_file.name)):
            fs.delete(uploaded_file.name)
        name = fs.save(uploaded_file.name,uploaded_file)
        context['name'] = uploaded_file.name
        context['url'] = fs.url(name)
        df = openpyxl.load_workbook(uploaded_file,data_only=True)
        for i in df.sheetnames:
            excel_data = list()
            for row in df[i].iter_rows():
                row_data = list()
                for cell in row:
                    row_data.append(cell.value)
                excel_data.append(row_data)
            #print(excel_data)
        context['excel_data'] = excel_data
        
    return render(request,'fileLoad/Html_css_files/mainLoad.html',context)
    

def validate(request,data):
    
    return render(request,'fileLoad/Html_css_files/validate.html',data)
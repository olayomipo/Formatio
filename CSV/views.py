from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import os

from .logic import CSV, random_ascii, delete_files_before
# Create your views here.

def home(request):
    return render(request, 'csv/home.html')

def tojson(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            csv = CSV(file, path_to_upload)
            path = csv.to_json()
                        
        # path = f"{str(res)}_{file_name}"
        return render(request, 'csv/tojson.html', {'url': path})        

    return render(request, 'csv/tojson.html')


def toxls(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            csv = CSV(file, path_to_upload)
            path = csv.to_xls()
        
        return render(request, 'csv/toxls.html', {'url': path})        

    return render(request, 'csv/toxls.html')

def toxml(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            csv = CSV(file, path_to_upload)
            path = csv.to_xml()
        
        return render(request, 'csv/toxml.html', {'url': path})        

    return render(request, 'csv/toxml.html')

def tohtml(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            csv = CSV(file, path_to_upload)
            path = csv.to_html()
        
        return render(request, 'csv/tohtml.html', {'url': path})        

    return render(request, 'csv/tohtml.html')

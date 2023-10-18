from django.shortcuts import render

import os

from .logic import EXCEL, random_ascii, delete_files_before
# Create your views here.

def home(request):
    return render(request, 'xls/home.html')

def tocsv(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            xls = EXCEL(file, path_to_upload)
            path = xls.to_csv()
        
        # paths = []
        
        # if files:
        #     for file in files.getlist('files'):
        #         xls = EXCEL(file, path_to_upload)
        #         path = xls.to_csv()
        #         paths.append(path)
                
        # print(paths)
                        
        # path = f"{str(res)}_{file_name}"
        return render(request, 'xls/tocsv.html', {'url': path})        

    return render(request, 'xls/tocsv.html')


def tojson(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            xls = EXCEL(file, path_to_upload)
            path = xls.to_json()
        
        return render(request, 'xls/tojson.html', {'url': path})        

    return render(request, 'xls/tojson.html')

def toxml(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            xls = EXCEL(file, path_to_upload)
            path = xls.to_xml()
        
        return render(request, 'xls/toxml.html', {'url': path})        

    return render(request, 'xls/toxml.html')

def tohtml(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            xls = EXCEL(file, path_to_upload)
            path = xls.to_html()
        
        return render(request, 'xls/tohtml.html', {'url': path})        

    return render(request, 'xls/tohtml.html')

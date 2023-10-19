from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import os

from .logic import JSON, random_ascii, delete_files_before
# Create your views here.

def home(request):
    return render(request, 'json/home.html')

def tocsv(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            json = JSON(file, path_to_upload)
            path = json.to_csv()
                        
        # path = f"{str(res)}_{file_name}"
        return render(request, 'json/tocsv.html', {'url': path})        

    return render(request, 'json/tocsv.html')


def toxls(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            json = JSON(file, path_to_upload)
            path = json.to_xls()
        
        return render(request, 'json/toxls.html', {'url': path})        

    return render(request, 'json/toxls.html')

def toxml(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        
        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            json = JSON(file, path_to_upload)
            path = json.to_xml()
        
        return render(request, 'json/toxml.html', {'url': path})        

    return render(request, 'json/toxml.html')

def tohtml(request):

    if request.method == "POST":   
        delete_files_before('uploaded_files')
        # print(request.FILES)     
        
        file = request.FILES['files']

        if file:
            asc = random_ascii()
            path_to_upload = os.path.join('uploaded_files', asc)
            os.makedirs(path_to_upload)  
            json = JSON(file, path_to_upload)
            path = json.to_html()
        
        return render(request, 'json/tohtml.html', {'url': path})        

    return render(request, 'json/tohtml.html')

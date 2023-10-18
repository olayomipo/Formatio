

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
import zipfile
from django.http import FileResponse
import mimetypes


def home(request):
    return render(request, 'home.html')

def download_file(request, path):
    # Replace 'path/to/file' with the actual path to your file
    
    # print(path)
    
    if request.method == "GET":
    
        # path = path.replace('_', '/')
        abs_file_path = path    
        
        
        abs_file_path = os.path.join(os.getcwd(), abs_file_path)
        
        # Create a Django response object
        response = FileResponse(open(abs_file_path, 'rb'))
        # print(os.path.basename(abs_file_path))

        # Set the Content-Disposition header to make the browser download the file
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(abs_file_path))
            
        
        return response




def download_files(request, path):
    # 'paths' is a list of paths to the files you want to download
    
    paths = path
    if request.method == "GET":
        # Create a new zip file
        zip_file_path = os.path.join(os.getcwd(), 'files.zip')
        
        print(zip_file_path)
        
        with zipfile.ZipFile(zip_file_path, 'w') as zip_file:
            for path in paths:
                abs_file_path = os.path.join(os.getcwd(), path)
                # Add each file to the zip file
                zip_file.write(abs_file_path, arcname=os.path.basename(abs_file_path))

        # Create a Django response object and set the Content-Disposition header
        response = FileResponse(open(zip_file_path, 'rb'))
        response['Content-Disposition'] = 'attachment; filename="{}"'.format(os.path.basename(zip_file_path))

        return response



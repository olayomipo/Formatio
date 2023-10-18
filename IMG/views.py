from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

import img2pdf
import pandas as pd
import os
from pdf2image import convert_from_path, convert_from_bytes
from zipfile import ZipFile
import re

from .logic import delete_files_before, random_ascii


# Create your views here.
def home(request):
    return render(request, 'img/home.html')


def pdf_view(request):
    with open('./convertor/sample_10.pdf', 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline'
        return response


def jpgToPdf(request):
    # img2pdf pip
    delete_files_before('uploaded_files')
    if request.method == "POST":
        # creating random folder name for each user
        
        res = random_ascii()
        path_to_upload = os.path.join('uploaded_files', res)
        
        os.makedirs(path_to_upload)
        
        path = path_to_upload+"/result.pdf"
        
        print(path)
        
        files = request.FILES
        
        files_list = []
        for file in files.getlist('files'):
            # print(file.temporary_file_path())
            files_list.append(file)
                        
        if files_list  != []:
            # Do the file creation
            a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
            layout_fun = img2pdf.get_layout_fun(a4inpt)
            
            with open(path_to_upload + "/result.pdf", "wb") as f:
                f.write(img2pdf.convert(files_list, layout_fun=layout_fun))
            # End of file creation
        
            
        # os.rename(path_to_upload + "/sample.pdf", path_to_upload + "/result.pdf")
        
        
        return render(request, 'img/jpgtopdf.html', {'url': path})
    
    return render(request, 'img/jpgtopdf.html')


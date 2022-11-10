from django.shortcuts import render
from web_datappt.forms import FileForm
from web_datappt.functions import handle_uploaded_file, file_name_function
from web_datappt.gustavo_code import convert_file2data, column_attributes

def index(request):
    file_name = ''
    op_one = ''
    op_two = ''
    file_form = FileForm(request.POST, request.FILES)
    if file_form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        file_name = file_name_function(request.FILES['file'])
        op_one = convert_file2data(request.FILES['file'])
        op_two = column_attributes(op_one)

    return render(request,"web_datappt/index.html",{'form':file_form, 'name_offile': file_name, 'operacao': op_two})

def dashboard(request):
    return render(request, "web_datappt/dashboard.html" )

def about(request):
    return render(request, "web_datappt/about.html")


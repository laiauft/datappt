from django.shortcuts import render
from web_datappt.forms import FileForm
from web_datappt.functions import handle_uploaded_file, file_name_function, list_of_columns, list_of_rows
from web_datappt.gustavo_code import convert_file2data, column_attributes

def index(request):
    file_name = ''
    file = ''
    op_two = ''
    file_columns = ''
    num_of_rows = ''
    file_form = FileForm(request.POST, request.FILES)
    if file_form.is_valid():
        handle_uploaded_file(request.FILES['file'])
        file_name = file_name_function(request.FILES['file'])
        file = convert_file2data(request.FILES['file'])
        op_two = column_attributes(file)
        file_columns = list_of_columns(file)
        num_of_columns = len(file_columns)
        num_of_rows = list_of_rows(file)

    context = {
        'form':file_form, 
        'name_offile': file_name, 
        'operacao': op_two,
        'columns': file_columns,
        'num_columns': num_of_columns,
        'range': range(num_of_columns),
        'rows': num_of_rows,
    }
    return render(request,"web_datappt/index.html", context)

def dashboard(request):
    return render(request, "web_datappt/dashboard.html" )

def about(request):
    return render(request, "web_datappt/about.html")


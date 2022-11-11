from django.core.exceptions import ValidationError

def handle_uploaded_file(f):  
    with open('web_datappt/static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)

def validate_file_extension(value):
    if not value.name.endswith('.csv'):
        raise ValidationError(u'Error message')

def file_name_function(f):
    file_name = f.name
    return file_name

def list_of_columns(f):
    list_of_columns = []
    for col in f.columns:
        list_of_columns.append(col)
    return list_of_columns

def list_of_rows(f):
    num_of_rows = f.shape[0]
    return num_of_rows



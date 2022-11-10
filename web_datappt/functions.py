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


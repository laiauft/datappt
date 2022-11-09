from django.shortcuts import render
<<<<<<< HEAD
from web_datappt.forms import FileForm
from web_datappt.functions import handle_uploaded_file  

def index(request):
    file_form = FileForm(request.POST, request.FILES)
    if file_form.is_valid():
        handle_uploaded_file(request.FILES['file'])
    return render(request,"web_datappt/index.html",{'form':file_form})

def dashboard(request):
    return render(request, "web_datappt/dashboard.html" )

def about(request):
    return render(request, "web_datappt/about.html")

=======

# Create your views here.
>>>>>>> 0484ab92fb8464e8f8ac59402490aca2aaa9ba36

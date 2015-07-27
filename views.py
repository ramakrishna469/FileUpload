from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from .forms import FileUploadModelForm
from .models import FileUpload
# Create your views here.

def index(request):
    template_name = 'index.html'

    if(request.method == 'POST'):
        form = FileUploadModelForm(request.POST,request.FILES)
        if(form.is_valid):
            if "File" in request.FILES:
                file = request.FILES["File"]
                form.save()
                print file,"saved"
                return HttpResponseRedirect(reverse('fileuploader:display'))
        dict_items = {'form':form}
        return render(request,template_name,dict_items)
    else:
        form = FileUploadModelForm()
        dict_items = {'form':form}
        return render(request,template_name,dict_items)
    return HttpResponse("It works")

def display(request):
    template_name = 'display.html'
    files = FileUpload.objects.all()
    dict_items = {'files':files}
    return render(request,template_name,dict_items)
from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from imgComment.fileHandler import FileHandler
from imgComment.models import *
from imgComment.forms import *


# Create your views here.
def index(request):
    return render(request,'index.html')

def upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fh = FileHandler()
            fileID = fh.handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/edit/'+str(fileID)+"/")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',RequestContext(request,locals()))

def edit(request,fileID):
    if request.method == 'POST':
        # form = UploadFileForm(request.POST, request.FILES)
        # if form.is_valid():
        #     fh = FileHandler()
        #     fileID = fh.handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/index/')
    else:
        image = Image.objects.get(id=fileID)
        form = SaveImageForm()
    return render_to_response('edit.html',RequestContext(request,locals()))

def browse(request):
    comments = Comment.objects.order_by('-uploadTime')
    return render_to_response('browse.html',RequestContext(request,locals()))

def comment(request):
    return render_to_response('comment.html',RequestContext(request,locals()))



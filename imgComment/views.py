from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext

from imgComment.fileHandler import FileHandler
from imgComment.ptt_post import ptt_post
from imgComment.img_uploader import ImgurUploader
from imgComment.pushCrawler import pushCrawler
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
            imgFilePath = fh.handle_uploaded_file(request.FILES['file'])
            image = Image.objects.create(origFile=imgFilePath)
            return HttpResponseRedirect('/edit/'+str(image.id)+"/")
    else:
        form = UploadFileForm()
    return render_to_response('upload.html',RequestContext(request,locals()))

def edit(request,fileID):
    image = Image.objects.get(id=fileID)
    if request.method == "POST":
        form = SaveImageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]

##            # handle the edit image
##            fh = FileHandler()
##            imgFilePath = fh.handle_uploaded_file(request.FILES['file'])

            # upload to imgur
            imgur = ImgurUploader()
            imageUrl = imgur.upload(image.origFile)

            # automatically post
            ptt = ptt_post()
            postUrl = ptt.to_post(title,content,imageUrl)

            # update image object
            #image.editFile = imgFilePath
            image.postUrl = postUrl
            image.imageUrl = imageUrl
            image.title = title
            image.content = content
            image.save()
            return HttpResponseRedirect('/comment/'+str(image.id)+"/")
    else:
        image = Image.objects.get(id=fileID)
        form = SaveImageForm()
    return render_to_response('edit.html',RequestContext(request,locals()))

def browse(request):
    images = Image.objects.order_by('-uploadTime')
    return render_to_response('browse.html',RequestContext(request,locals()))

def comment(request,fileID):
    image = Image.objects.get(id=fileID)

    crawler = pushCrawler()
    postList = crawler.get(image.postUrl)

    # TODO store the postList to the DB


    comments = [str(comm.text) for comm in image.comment_set.all()]

    return render_to_response('comment.html',RequestContext(request,locals()))







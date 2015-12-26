import os
import time
import string
import random

from imgComment.models import *

TEST_MANAGER_DIR = os.path.dirname(os.path.abspath(__file__))

class FileHandler():
    def __init__(self):
        pass

    def handle_uploaded_file(self,f):
        # handle uploaded file
        uploadDir = os.path.join(TEST_MANAGER_DIR,'upload')
        self.mkdir(uploadDir) # imgComment/upload/
        uploadTime = time.localtime(time.time())
        todayDir = os.path.join(uploadDir,time.strftime("%Y-%m-%d",uploadTime))
        self.mkdir(todayDir) # imgComment/upload/2015-12-18/

        # write the image file
        fileType = "."+f.name.split(".")[-1]
        tempFileName = os.path.join(todayDir,self.random_str()+'.'+fileType)
        with open(tempFileName, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

        return tempFileName

    def mkdir(self,path):
        if os.path.isdir(path):
            return
        else:
            os.mkdir(path)

    def store(self,imgFilePath):
        # create image
        self.image = Image.objects.create(origFile=imgFilePath)
        return self.image.id

    def random_str(self,size=40, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


#-------------------------------------------------------------------------------
# Name:        ??1
# Purpose:
#
# Author:      b9890_000
#
# Created:     16/12/2015
# Copyright:   (c) b9890_000 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import os
import time

from imgComment.models import *

TEST_MANAGER_DIR = os.path.dirname(os.path.abspath(__file__))

class FileHandler():
    def __init__(self):
        pass

    def handle_uploaded_file(self,f):
        pass
##        # handle uploaded file
##        uploadDir = os.path.join(TEST_MANAGER_DIR,'upload')
##        self.mkdir(uploadDir) # test_manager/upload/
##        uploadTime = time.localtime(time.time())
##        todayDir = os.path.join(uploadDir,time.strftime("%Y-%m-%d",uploadTime))
##        self.mkdir(todayDir) # test_manager/upload/2015-12-18/
##
##        # write the temp apk file
##        tempFileName = os.path.join(todayDir,time.strftime("%H_%M_%S_",uploadTime)+f.name)
##        with open(tempFileName, 'wb+') as destination:
##            for chunk in f.chunks():
##                destination.write(chunk)
##
##        # get APK information
##        self.parse(tempFileName)
##
##        # store to DB
##        self.store(user.username,f.name)
##
##        # make project directory
##        projectDir = os.path.join(todayDir,"project_"+str(self.project.id))
##        self.mkdir(projectDir)
##
##        # rename the temp apk file
##        os.rename(tempFileName,os.path.join(projectDir,f.name))
##
##        #output project.json
##        self.dump(projectDir,f.name)

##
##    def mkdir(self,path):
##        if os.path.isdir(path):
##            return
##        else:
##            os.mkdir(path)
##
##    def parse(self,apkFile):
##        out_bytes = check_output(["aapt","dump","badging",apkFile])
##        out_text = out_bytes.decode('utf-8')
##        for line in out_text.split('\n'):
##            if line.startswith("package"):
##                for attr in line.split(" "):
##                    if attr.startswith("name"):
##                        self.appPackageName = attr.replace("name=","").replace("'","")
##                        #print(self.appPackageName)
##                    if attr.startswith("versionName"):
##                        self.versionNum = attr.replace("versionName=","").replace("'","").replace("\r","")
##                        #print(self.versionNum)
##            elif line.startswith("launchable-activity"):
##                for attr in line.split(" "):
##                    if attr.startswith("name"):
##                        self.appFirstActivity = attr.replace(self.appPackageName,"").replace("name=","").replace("'","")
##                        #print(self.appFirstActivity)
##
##    def store(self,userName,apkFileName):
##        # get user
##        self.user = User.objects.get(username=userName)
##
##        # get app
##        try:
##            self.app = App.objects.get(packageName=self.appPackageName,fstActivityName=self.appFirstActivity,versionNum=self.versionNum)
##        except App.DoesNotExist as e:
##            print("app doesn't exist, and create one")
##            appName = self.appPackageName.split(".")[-1]
##            self.app = App.objects.create(name=appName,packageName=self.appPackageName,fstActivityName=self.appFirstActivity,versionNum=self.versionNum,apkFile=apkFileName)
##
##        # create project
##        self.project = Project.objects.create(user=self.user,app=self.app,level=1)
##
##    def dump(self,outputDir,apkFileName):
##        outputFile = os.path.join(outputDir,"project.json")
##        data ={"userID":self.user.id}
##        data["appID"] = self.app.id
##        data["account"] = self.user.username
##        data["appPackageName"] = self.appPackageName
##        data["firstActivityName"] = self.appFirstActivity
##        data["apkFile"] = apkFileName
##        data["versionNum"] = self.versionNum
##
##        with open(outputFile, "w") as outfile:
##            json.dump(data, outfile, indent=4)





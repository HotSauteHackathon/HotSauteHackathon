# -*- coding: utf8 -*-

'''
input: hash tag or URL of certain post
output: Lists of pusher_name, push_time, push_content
'''
import re
import urllib
import codecs # usding for chinese utf-8

#ptt filehandler
class pushCrawler(object):
    def __init__(self,html):
        self.html = html

    def get(self):
        pttfh = urllib.urlopen(self.html).read() # filehandler
        push_counter = 0    # num of push
        push_list = []
        #print 'push: ' ,push.decode('utf-8')
        for floor in re.findall('class="push">.+',pttfh):
            #push-userid">frankofranko</span>
            pusherName = re.findall('push-userid">(.+?)<',floor)[0]
            #<span class="push-ipdatetime"> 12/26 12:58
            pushTime = re.findall('push-ipdatetime">(.+)',floor)[0]
            # push-content">: 你好</span>
            pushContent = re.findall('push-content">: (.+?)</span',floor)[0]
            # push-tag">推 </span>
            pushType = re.findall('push-tag">(.+?) <',floor)[0]

            pushDict = {'pusher_name':pusherName, 'push_time':pushTime,
            'push_content':pushContent.decode('utf-8'),'push_type':pushType.decode('utf-8')}
            push_list.append(pushDict)
            push_counter = push_counter +1

        #print 'push_counter: ', str(push_counter)
        #print push_list
        return push_list

# test bench
tb = pushCrawler( 'https://www.ptt.cc/bbs/Test/M.1451105872.A.B9F.html')
getDict = tb.get()
print(getDict)
print(getDict[1]['push_type'])
'''
'''

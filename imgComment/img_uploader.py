import requests
import json

class ImgurUploader():
    def __init__(self):
        pass

    def upload(self,path):
        r = requests.post(
        'https://api.imgur.com/3/image',
        data = { 'image': open(path, 'rb').read(), 'type': 'file' },
        headers = {'Authorization': 'Client-ID 90830744d606498'}
        )

        rr = r.json()
        print (rr['data']['link'])

        return (rr['data']['link'])




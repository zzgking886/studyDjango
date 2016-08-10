import urllib.request
import json
import time

def testInterFaceTime(name,url):
    timestamp = ""
    start = time.time()
    returndata = urllib.request.urlopen(url).read()
    dataobj = json.loads(returndata.decode("utf-8"))
    end = ""
    if len(dataobj) > 0:
        end = time.time()
    else:
        end = "time out"

    if end == "time out":
        timestamp = "time out"
    else:
        timestamp = ('Task runs %0.2f seconds.' % (end - start))

    return [name,url,timestamp]
 
url = "http://cbox.cntv.cn/json2015/topshouye/tuijianaoyun/index.json"
returndata = urllib.request.urlopen(url).read()
dataobj = json.loads(returndata.decode("utf-8"))
dataDic = dataobj['data']
categoryList = dataDic['categoryList']

arrayList = []
for oneCategory in categoryList:
    listUrl = oneCategory['listUrl']
    name = oneCategory['title']
    result = testInterFaceTime(name,listUrl)
    print(result)




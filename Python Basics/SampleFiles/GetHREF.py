import urllib.request, urllib.parse, re, sys

def parseURL(url):
    req = urllib.request.Request(url)  # create a webrequest
    resp = urllib.request.urlopen(req)  # web request and capture the response
    respdata = resp.read()  # read the response data

    hyperlinks = re.findall(
        r'<a href="(.*?)"',
        str(respdata))  # regex to parse and capture all hyperlinks
    paragraph = re.findall(
        r'<p>(.*?)</p>', str(respdata))  # regex to parse and capture all paragraph

    for link in hyperlinks:
        print(link) # print first 10 hyperlinks

    #filename = url.replace('/','').replace('http:','')
    #print(filename)
    # print all hyperlinks captured
    #for link in hyperlinks:
    #    savefile = open('{0}.txt'.format(filename), 'a')  # mode =  'w' (WRITE)     
    #    savefile.write(link+'\n')      
    #    savefile.close()

#parseURL(sys.argv[1])
#print(paragraph[0:4]) # print first 4 paragraphs

print(ord('x'))


ord

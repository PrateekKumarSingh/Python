# this example focuses on error-handling around web requests and how to define headers in the request

import urllib.request

url = 'http://www.google.com/search?q=prateek'

try:
    response = urllib.request.urlopen(url)
    print(response.read())
except Exception as e:
    print(e)

print('''
you\'ll get an error in above example [HTTP Error 403: Forbidden]
because some websites like Google know that they are being accessed programatically (with Python)
so you need to customize the request header to not look like a program
''')


try:
    headers = {} # empty dictionary or called as hashtable in other languages
    # a header to look like its not a python program and just another user agent like, chrome or mozilla
    headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
    request = urllib.request.Request(url, headers=headers) # overridding the default headers with our custom header
    response = urllib.request.urlopen(request) 
    #print(str(response.read()))

    responsedata = response.read()
    stringresponsedata = responsedata.decode('utf-8')

    filename = '.\\samplefiles\\RequestWithHeader.txt'
    if len(responsedata)>0:
        print('writing the web response from the URL: {0} in file {1}'.format(url,filename))
        savefile = open(filename,'w')
        savefile.write(str( responsedata ) )
    else:
        print('no response!')        
    
except Exception as e:
    print(e)

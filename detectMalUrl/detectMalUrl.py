
# de constructing the url

def getTokens(input):
    tokensBySlash =str(input.encode('utf-8')).split('/')
    allTokens = []
    for i in tokensBySlash:
        tokens = str(i).split('-')
        tokensByDot =[]
        for j in range(0,len(tokens)):
            tempTokens = str(tokens[j]).split('.')
            tokensByDot = tokensByDot + tempTokens
        allTokens = allTokens + tokens + tokensByDot
        allTokens = list(set(allTokens))
        if 'com' in allTokens:
            allTokens.remove('com')
    return allTokens

# load the data and store it in a list
allurls = 'allurls.txt'




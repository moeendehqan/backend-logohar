
import config


def findTitleTypeColor(name):
    title = ''
    for i in config.categoryColor:
        if i['name'] == name:
            title = i['title']
            break
    return title
    

def findTitleTypeJob(nameList):
    titleList = []
    for j in nameList:
        for i in config.categoryJob:
            if i['name'] == j:
                titleList.append(i['title'])
                break
    return titleList
    

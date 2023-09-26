
import config


def findTitleTypeColor(name):
    title = ''
    for i in config.categoryColor:
        if i['name'] == name:
            title = i['title']
            break
    return title
    


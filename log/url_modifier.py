import re


def id_replacer(url):
    return re.sub(r'\d+', "{id}", url)

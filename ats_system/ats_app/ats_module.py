from pypdf import PdfReader
from django.conf import settings
from . import extensions
import os
def check_keywords(keywords_list: [str], file_content):
    txt = str(file_content).lower()
    dictionary = dict()
    total = True
    for kw in keywords_list:
        if kw.lower() in txt:
            dictionary[kw] = True
        else:
            total = False
            dictionary[kw] = False
    
    dictionary["total"] = total
    #print(dictionary)
    return dictionary
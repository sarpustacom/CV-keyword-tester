def check_file_pdf(filename):
    ext = filename.split(".")[-1].strip().lower()
    if ext == "pdf":
        return True
    else: 
        return False
    
class DictionaryItemSp():
    def __init__(self, key, value):
        self.key = key
        self.value = value

def dictionary_to_class(dictionary):
    items = []
    for k,v in dictionary.items():
        items.append(DictionaryItemSp(k,v))
    return items
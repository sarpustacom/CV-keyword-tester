from django.shortcuts import render
from . import extensions, ats_module
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import UploadedFile
# Create your views here.
def index(request):
    return render(request, "ats_app/index.html")

def form_view(request):
    return render(request, "ats_app/form.html")

def check_view(request):
    if request.method == "POST" and request.FILES["upload_file"]:
        file: UploadedFile = request.FILES["upload_file"]
        
        if extensions.check_file_pdf(file.name):
            kw_value = request.POST["keywords_text_area"]
            kws = kw_value.split(",")
            file_content = file.read()
            validation_data = ats_module.check_keywords(kws, file_content)
            

            item_dic = extensions.dictionary_to_class(validation_data)
            item_dic.pop()
            return render(request, "ats_app/check.html", context={"items":item_dic ,"total": validation_data["total"]})

        else:
            return render(request, "ats_app/form.html", context={"error":"Invalid file type, please upload just PDF!"})
        
    else:
        return render(request, "ats_app/form.html", context={"error":"Invalid request type, please fill the form."})


from django.shortcuts import render
from django.http import HttpResponse
from . import util
import numpy  
from numpy import random

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
def page(request, name):
    if request.method == "POST":
        if util.get_entry(name) != None:
            return render(request, "encyclopedia/page.html", {
            "markPage": util.get_entry(name), "markName": name
            })
        else:
            allEnteries = util.list_entries()
            resultSet = set()
            for entry in allEnteries:
                if len(name) < len(entry):
                    for i in range(0,len(entry)-len(name)):
                        if name == entry[i : i+len(name)]:
                            resultSet.add(entry)
            return render(request, "encyclopedia/sResults2.html", {"resultSet": resultSet, "allEnteries": allEnteries} )


    else:
        print("in page method")
        return render(request, "encyclopedia/page.html", {
        "markPage": util.get_entry(name), "markName": name
        })
def randPage(request):
    allEnteries = util.list_entries()
    x = random.randint(0,len(allEnteries)-1)
    print("in rand page")
    return render(request, "encyclopedia/page.html", {
    "markPage": util.get_entry(allEnteries[x]), "markName": allEnteries[x]
    })


    



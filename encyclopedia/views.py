from django.shortcuts import render
from django.http import HttpResponse
from . import util
import numpy  
from numpy import random
from django import forms


class NewTaskForm(forms.Form):
    task = forms.CharField(label= "someInput")

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

    if name == "random":
        allEnteries = util.list_entries()
        x = random.randint(0,len(allEnteries)-1)
        return render(request, "encyclopedia/page.html", {
        "markPage": util.get_entry(allEnteries[x]), "markName": allEnteries[x]
        })

    else:
        print("in page method")
        return render(request, "encyclopedia/page.html", {
        "markPage": util.get_entry(name), "markName": name
        })



    



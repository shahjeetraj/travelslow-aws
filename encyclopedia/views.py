import random
from markdown2 import Markdown
from django.shortcuts import render
from . import util

def convert_m2h(title):
    content = util.get_entry(title)
    markdowner = Markdown()
    if content == None:
        return None
    else:
        return markdowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    html_content = convert_m2h(title)
    if html_content == None:
        return render(request, "encyclopedia/404.html",{
            "message":"This page does not exist!"
        })
    else:
        return render(request, "encyclopedia/entry.html",{
            "title": title,
            "content": html_content
        })

def search(request):
    if request.method == "POST":
        entry_search = request.POST['q']
        html_content = convert_m2h(entry_search)
        if html_content is not None:
            return render(request, "encyclopedia/entry.html",{
            "title": entry_search,
            "content": html_content
        })
        else:
            allentries = util.list_entries()
            result = []
            for entry in allentries:
                if entry_search.lower() in entry.lower():
                    result.append(entry)
            return render(request, "encyclopedia/search.html",{
                    "result" : result
                })

def new_page(request):
    if request.method == "GET":
        return render(request, "encyclopedia/new.html")
    else:
        title = request.POST.get('title')
        content = request.POST.get('content')
        titleExist = util.get_entry(title)
        print(titleExist)
        if titleExist is not None:
            return render(request,"encyclopedia/error.html",{
                "message": "Page already Exists for the given title."
            })
        else:
            util.save_entry(title,content)
            html_content = convert_m2h(title)
            return render(request, "encyclopedia/entry.html",{
                'title': title,
                'content': html_content
            })

def edit(request):
    if request.method == 'POST':
        title = request.POST.get('entry_title')
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html",{
            "title" : title,
            "content" : content
        })

def save_edit(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        util.save_entry(title, content)
        html_content = convert_m2h(title)
        print(html_content)
        return render(request, "encyclopedia/entry.html",{
            "title" : title,
            "content" : html_content
        })
    
def rand_entry(request):
    allentries = util.list_entries()
    choice = random.choice(allentries)
    html_content = convert_m2h(choice)
    return render(request, "encyclopedia/entry.html", {
        "title": choice,
        "content": html_content
    })

def delete(request):
    if request.method == "POST":
        title = request.POST.get('entry_title')
        html_content = convert_m2h(title)
        return render(request, "encyclopedia/delete.html",{
            "title": title,
            "content" : html_content,
            "message1": "Delete Warning!",
            "message" : "Are you sure you want to delete this entry? It could lead to loss of data.!!",
        })

def del_final(request):
    if request.method == "POST":
        title = request.POST.get('entry_title')
        print(title)
        util.delete_entry(title)
        return render(request, "encyclopedia/index.html",{
            "entries": util.list_entries(),
            "message": title+" entry is deleted permanently!"
        })
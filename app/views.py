from django.shortcuts import render, HttpResponse, redirect
from .models import Show
# import locale
# locale.setlocale(locale.LC_ALL, 'es-ES')
from django.contrib import messages

def index(request):
    return redirect('/shows')


def shows(request):
    all_shows = Show.objects.all()
    if request.method == "GET":
        context= {
            "all_shows": all_shows,
        }
    return render(request,"shows.html", context)


def new_show(request):
    if request.method=='GET':
        return render(request,"new_show.html")


def create_show(request):
    if request.method=='POST':
        print(request.POST['release_date'])
        errors = Show.objects.add_show_val(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/shows/new')
        else:
                Show.objects.create(title=request.POST['title'], 
                                    network=request.POST['network'], 
                                    rel_date=request.POST['release_date'],
                                    desc= request.POST['description']
                )
                messages.success(request, "Show successfully created")
                print(request.POST['release_date'])
                return redirect('/shows')


def show_id(request, id):
    theshow = Show.objects.get(id=int(id))
    if request.method=='GET':
        context= {
            "id": theshow.id,
            "title": theshow.title,
            "network": theshow.network,
            "rel_date": theshow.rel_date,
            "desc": theshow.desc,
            "updated": theshow.updated_at,
        }
        return render(request,"tv_show.html", context)


def show_edit(request, id):
    edit_show = Show.objects.get(id=int(id))
    if request.method =="GET":
        context= {
            "id": edit_show.id,
            "title": edit_show.title,
            "network": edit_show.network,
            "rel_date": edit_show.rel_date,
            "desc": edit_show.desc,
            "updated": edit_show.updated_at,
        }
        return render(request,"edit_show.html", context)


def show_update(request, id):
    errors = Show.objects.add_show_val(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/'+str(show_to_update.id)+'/edit')
    else:
        show_to_update = Show.objects.get(id=int(id))
        if request.method=="POST":
            show_to_update.title=request.POST['title']
            show_to_update.network=request.POST['network']
            show_to_update.desc= request.POST['description']
            show_to_update.rel_date= request.POST['release_date']
            show_to_update.save()
            #esta parte no funciona a decir verdad
            return redirect('/shows/'+str(show_to_update.id)+'/edit')
            # return redirect("/shows/"+str(this_show_update.id)) # Recuerda : Son objetos... merme



def show_destroy(request, id):
    destroy_show = Show.objects.get(id=int(id))
    destroy_show.delete()
    return redirect('/shows')





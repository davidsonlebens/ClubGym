from django.shortcuts import render
from .models import Abonnement

def home(request):
    list_abonnements=Abonnement.objects.all()
    context={"liste_abonnements":list_abonnements}
    return render(request, "index.html", context)

def detail(request, id_abonnement):
    abonnement=Abonnement.objects.get(id=id_abonnement)
    category=abonnement.category
    abonnements_en_relation=Abonnement.objects.filter(category=category)[:5]
    return render(request, 'detail.html', {"abonnement":abonnement, "aer":abonnements_en_relation})

def search(request):
    query=request.GET["abonnement"]
    liste_abonnement= Abonnement.objects.filter(title__icontains=query)
    return render(request, "search.html", {"liste_abonnement":liste_abonnement})


def sms(request):
    message=request.GET['body']
    message_splited=message.split("-")
    title=message_splited[0]
    desc=message_splited[1]

    etud_category=Category.objects.get(id=2)
    abonnement= Abonnement(title=title, category=etud_category, desc=desc, image="http://default")
    abonnement.save()
    print('data saved successfully')
    return HttpResponse("data saved successfully")


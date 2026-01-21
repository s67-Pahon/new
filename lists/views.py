from django.shortcuts import redirect , render
from django.http import HttpResponse
from lists.models import Item , List
from django.db.models import Case, When, Value, IntegerField

# Create your views here.

def home_page(request):
    
    return render(request, "home.html")

def about_page(request) :
    return render(request , "about.html")

def new_list(request):
    nulist = List.objects.create()
    Item.objects.create(
        text=request.POST["item_text"],
        list=nulist,
        priority=request.POST.get("priority", Item.PRIORITY_MEDIUM),
    )
    return redirect(f"/lists/{nulist.id}/")

def view_list(request, list_id):
    our_list = List.objects.get(id=list_id)

    items = our_list.item_set.all()
    is_sorted = False

    if request.GET.get("sort") == "priority":
        is_sorted = True
        items = items.annotate(
            priority_rank=Case(
                When(priority="H", then=Value(1)),
                When(priority="M", then=Value(2)),
                When(priority="L", then=Value(3)),
                default=Value(99),
                output_field=IntegerField(),
            )
        ).order_by("priority_rank", "id")

    return render(
        request,
        "list.html",
        {
            "list": our_list,
            "items": items,
            "is_sorted": is_sorted,
        },
    )



def add_item(request, list_id):
    pass

def add_item(request, list_id):
    our_list = List.objects.get(id=list_id)
    Item.objects.create(
        text=request.POST["item_text"],
        list=our_list,
        priority=request.POST.get("priority", Item.PRIORITY_MEDIUM),
    )
    return redirect(f"/lists/{our_list.id}/")

    

    
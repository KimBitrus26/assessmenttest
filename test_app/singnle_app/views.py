from django.shortcuts import render, redirect
from .models import Item, ItemQuantity
from django.contrib import messages
from .forms import ItemForm

# Create your views here.


def home(request):
    item_data = Item.objects.all().order_by("-date_created")
    
    context = {
        "item_data": item_data
    }
    return render(request, 'home.html', context )


def add_item(request):
     
    item = ''
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        
        if form.is_valid():

            item_data = Item.objects.all()
            if item_data:
                # loop if item is found in db
                for item in item_data:       
                #check items cannot be added more than 10
                    if item.item_quantity.quantity <= 10:   
                        items = Item.objects.create(
                            title=form.cleaned_data["title"],
                            price=form.cleaned_data["price"],
                            description=form.cleaned_data["description"],
                            item_quantity=form.cleaned_data["item_quantity"],

                                )
                
                        items.save()
                        #increase qty by 1 for each item added
                        item.item_quantity.quantity += 1
                        item.item_quantity.save()
                        messages.success(request, 'Item added successfully')
                        return redirect("/")   
                    else:
                        messages.info(request, "You cannot add more than 10 items, delete some..")
                        return redirect("/")
            else:
                #if item is not in db, this will create item
                items = Item.objects.create(
                            title=form.cleaned_data["title"],
                            price=form.cleaned_data["price"],
                            description=form.cleaned_data["description"],
                            item_quantity=form.cleaned_data["item_quantity"],

                                )
                item_qty=ItemQuantity.objects.create(quantity=1)
                item_qty.save()
                
                items.save()
                messages.success(request, "Item added successfully")
                return redirect("/")
    return render(request, 'add_item.html', {"form":form})
    
    
def edit_item(request, pk):
    item_data = Item.objects.get(id=pk)
    form = EditItemForm(instance=item_data)
    if request.method == "POST":
        #pre-field form data of single item to be updated
        form = ItemForm(request.POST, instance=item_data)
        if form.is_valid():
    
            form.save()
            messages.success(request, 'Item updated successfully')
            return redirect("/")
          
    context={
        'form':form,
        "item-data": item_data
    }
    return render(request, 'edit_item.html', context)
            
def delete_item(request, pk):
    
        #query database for the item
    item_data = Item.objects.get(id=pk)
         
    item_data.delete() 
    #decrease qty by 1 for each item deleted  
    item_data.item_quantity.quantity -= 1
    item_data.item_quantity.save()    
            
    messages.success(request, 'Item deleted')
    return redirect("/")
            
            
    
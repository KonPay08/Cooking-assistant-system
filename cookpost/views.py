from django.shortcuts import redirect, render
from .models import CookingName,CategoryChoices,Tag

def listview(request):
  object_category = CategoryChoices.objects.all()
  object_list = CookingName.objects.all()
  object5 = object_list.count()
  for i in range(object5):
    object = CookingName.objects.all().get(id=i+1)
    object1 = object.tags.all()
    object2 = object1.filter(count=0).count()
    if object2 == 0:
      if object.count == 0:
        object.count += 1
        object.save()
      else:
        object.count += 0
        object.save()
    else:
      if object.count == 0:
        object.count += 0
        object.save()
      else:
        object.count -= 1
        object.save()
    object_list1 = object_list.filter(count=1)
  if request.method=='POST':
    key_name = request.POST['key_word']
    if key_name == '全て':
      return render(request,'list.html',{'object_list':object_list1,'object_category':object_category,})
    else:
      key = CategoryChoices.objects.get(category_name=key_name)
      object_list = object_list1.filter(category=key)
      return render(request,'list.html',{'object_list':object_list,'object_category':object_category,})
  else:
    return render(request,'list.html',{'object_list':object_list1,'object_category':object_category})

def detailview(request,pk):
  object = CookingName.objects.get(pk=pk)  
  return render(request,'detail.html',{'object':object})

def tagview(request):
  tag = Tag.objects.all()
  if request.method=='POST':
    if 'on' in request.POST:
      category = request.POST['on']
      object = tag.get(name=category)
      object.count += 1
      object.save()
    elif 'off' in request.POST:
      category = request.POST['off']
      object = tag.get(name=category)
      if object.count == 0:
       object.count -= 0
       object.save()
      else:
       object.count -= 1
       object.save()
    return render(request,'tag.html',{'tag':tag})
  else:
    tag = Tag.objects.all()
    return render(request,'tag.html',{'tag':tag})

def tableview(request):
  tag = Tag.objects.all()
  tag1 = tag.exclude(count=0)
  return render(request,'table.html',{'tag':tag1})
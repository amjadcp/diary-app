from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
import datetime
from home.models import Diary
from datetime import datetime

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    user = request.user
    diary = Diary.objects.filter(user=request.user)
    cyear = datetime.now().year
    cmonth = datetime.now().month
    if cmonth<10:
        cmonth = '0'+str(cmonth)
    thisyear = 0
    thismonth = 0
    for entry in diary:
        year = str(entry.date).split('-')[0]
        month = str(entry.date).split('-')[1]
        if str(cyear) == year:
            thisyear += 1
        if str(cyear) == year and str(cmonth) == month:
            thismonth += 1

    context = {
        'user' : user,
        'totalentries' : len(diary),
        'thisyear' : thisyear,
        'thismonth' : thismonth,
        'diary' : diary,
    }
    return render(request, 'dashboard.html', context=context)

@login_required
def calendar(request):
    date = request.POST['date']
    date = date.split('/')
    if int(date[0])<10:
        date[0] = '0'+date[0]
    if int(date[1])<10:
        date[1] = '0'+date[1]
    date = f'{date[2]}-{date[1]}-{date[0]}'
    diary = Diary.objects.filter(user=request.user)
    for endry in diary:
        if str(endry.date) == date:
            return JsonResponse({
                'message':'0',
                'title' : endry.title,
                'body' : endry.body,
                'date' : endry.date
                })
        
    return JsonResponse({'message':'1'})

@login_required
def create_diary(request):
    print(request.POST)
    date = request.POST['date']
    if '/' in date:
        date = date.split('/')
        if int(date[0])<10:
            date[0] = '0'+date[0]
        if int(date[1])<10:
            date[1] = '0'+date[1]
        date = f'{date[2]}-{date[1]}-{date[0]}'

    title = request.POST['title']
    body = request.POST['text']
    try:
        diary = Diary.objects.get(date=date)
        diary.title = title
        diary.body = body
        diary.save()
    except:
        Diary.objects.create(
            user = request.user,
            date = date,
            title = title,
            body = body
        )
    return JsonResponse({'message':'1'})

@login_required
def edit_diary(request):
    if request.method == 'POST':
        id = request.POST['id']
        diary = Diary.objects.get(id=id)
        return JsonResponse({'date':diary.date,'title':diary.title,'body':diary.body})

@login_required
def del_diary(request):
    if request.method == 'POST':
        id = request.POST['id']
        diary = Diary.objects.get(id=id)
        diary.delete()
        return JsonResponse({'message':'1'})


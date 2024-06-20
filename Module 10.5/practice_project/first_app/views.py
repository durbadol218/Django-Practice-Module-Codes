from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    return render(request,"home.html")

def about(request):
    return render(request, 'first_app/about.html')

def context(request):
    dict = {'name':'Lionel King Messi','nationality' : 'Argentina', 'position': 'Right-Wing','clubs' : ['Barcelona', 'Paris Saint Germein','Inter Miami'],'number_list':[1,2,3], 'name_list':['Jadu','Rahim','Karim'],'single_name':"I'm Durbadol",'string':"Python is great!",'birthday':datetime.datetime.now(),'publish_date':datetime.datetime.now(),'comment_date':datetime.datetime.now(),'time':datetime.datetime.now(),'default_value':" ",'members':[
        {
            'name': 'Durbadol',
            'district': 'Rangpur',
        },
        {
            'name': 'Tamim',
            'district': 'Sylhet',
        },
        {
            'name': 'Sharif',
            'district': 'Netrakona',
        },
        {
            'name': 'Amin',
            'district': 'Kurigram',
        },
        {
            'name': 'Rahim',
            'district': 'Chandpur',
        }
    ]}
    return render(request, 'first_app/context.html',dict)
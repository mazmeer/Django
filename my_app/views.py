from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def sample_view(request):
    return render(request,'my_app/example.html')


def variable_view(request):

    my_var ={'first_name':'Khan','last_name':'Pathan',
                'list':[1,2,3],'dictionary':{'dict_in_dict':'Bohut Zada Complicated Hogaya Ye To'},
                'user_logged_in': True 
    
    }


    return render(request,'my_app/variable.html',context=my_var)


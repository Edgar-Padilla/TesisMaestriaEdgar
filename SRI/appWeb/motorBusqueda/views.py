from django.shortcuts import render, redirect
from django.http import HttpResponse
import re
from  motorBusqueda.MSRI.busqueda import busqueda
from motorBusqueda.MSRI.busquedaAvanzada import busquedaAvanzada
from motorBusqueda.globals import postingList, sinonimosDic, bigramDic, synonymsOperators

def about(request):
    return redirect(request, 'about')

def index(request):
    return render(request,'index.html')

def tipo(entrada):
    for key in synonymsOperators:
        if re.search(key,entrada):
            return False
    expresion_regular = r"[*]|NOT|AND|OR"
    if re.search(expresion_regular, entrada):
        return False
    else:
        return True
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if tipo(search):
            print("busqueda normal")
            b=busqueda(postingList, sinonimosDic, bigramDic)
            final_result =b.identificar(search)
        else:
            print("busqueda avanzada")
            b=busquedaAvanzada(postingList, synonymsOperators)
            final_result =b.identificar(search)
        context = {
            'final_result': final_result
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'index.html')
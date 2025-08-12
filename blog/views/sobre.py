from django.shortcuts import render 

def sobre_view(request):
    context={
        'mensagem':'Essa é a pagina sobre'
    }
    return render(request,'blog/sobre.html',context)
from django.shortcuts import get_object_or_404, redirect, render
from .models import ArCondicionado
from django.http import HttpResponse
# Create your views here.
def criar_ar_condicionado(request):
    if request.method == 'GET':
        
        ar_condicionado= ArCondicionado.objects.all()
        
        return render(request, 'criar_ar_condicionado.html', {'ar_condicionado': ar_condicionado})
    
    elif request.method == 'POST':
         nome = request.POST.get('nome')
         sala = request.POST.get('sala') 
         
         
         
         ar_condicionado = ArCondicionado(
             nome = nome,
             sala = sala,
         )
         
         ar_condicionado.save()
         
         return redirect('criar_ar_condicionado')
    
def deletar_ar_condicionado(request, id):
    ar_condicionado = get_object_or_404(ArCondicionado,id=id)
    ar_condicionado.delete()
    return redirect('criar_ar_condicionado')
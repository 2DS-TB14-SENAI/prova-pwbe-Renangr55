from django.shortcuts import render,redirect,get_list_or_404
from .models import Medico, Consulta
from .form import ConsultaForm
from rest_framework import status
from .fliters import MedicoFilter



# Create your views here.
def listar_medicos(request):
    
    medico = Medico.objects.all()
    filtro = MedicoFilter(request.get, queryset=medico)
    if filtro:
        return render(request, 'clinica/listar_medicos.html', {'filter' : filtro})

    return render(request, "clinica/listar_medicos.html", {"medico" : medico})


def criar_consulta(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = ConsultaForm()

    return render(request, 'clinica/form_consulta.html',{'form' : form})


def detalhes_consulta(request,pk):
    detalhes = get_list_or_404(Consulta, pk=pk)
    return render(request,"clinica/form_consulta.html", {"detalhes": detalhes})
from django.shortcuts import render

# Create your views here.

def listar_tarefas(request):
    nome_tarefa = "Jackson é um bom programar se pah"
    return render(request, 'tarefas/listar_tarefas.html', {'nome_tarefa': nome_tarefa})
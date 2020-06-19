from ..models import Tarefa


def cadastrar_tarefa(tarefa):
    Tarefa.objects.create (titulo = tarefa.titulo,
                            data_expiracao = tarefa.data_expiracao,
                            descricao = tarefa.descricao,
                            prioridade = tarefa.prioridade)

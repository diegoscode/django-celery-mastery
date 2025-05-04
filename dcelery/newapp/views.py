from django.http import HttpResponse
from .tasks import process_data

def trigger_task_view(request):
    name = request.GET.get("name", "Usuário Anônimo")
    process_data.delay(name)
    return HttpResponse(f"Tarefa enviada para processar o nome: {name}")

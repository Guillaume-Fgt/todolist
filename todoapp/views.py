from django.http import HttpRequest
from todoapp.models import Task
from django.template.response import TemplateResponse
from django.db.models.query import QuerySet


def get_tasks(order_by_field: str) -> QuerySet:
    return Task.objects.all().order_by(order_by_field)


def index(request: HttpRequest) -> TemplateResponse:
    tasks = get_tasks("priority")
    return TemplateResponse(request, "index.html", {"tasks": tasks})


def add_task(request: HttpRequest) -> TemplateResponse:
    if request.method == "POST":
        task_name = request.POST.get("task")
        task_priority = request.POST.get("priority")
        task = Task.objects.create(name=task_name, priority=task_priority)
        task.save()
    tasks = get_tasks("priority")
    return TemplateResponse(request, "partials/table_row.html", {"tasks": tasks})


def delete_task(request: HttpRequest, pk: int) -> TemplateResponse:
    Task.objects.filter(id=pk).delete()
    tasks = get_tasks("priority")
    return TemplateResponse(request, "partials/table_row.html", {"tasks": tasks})

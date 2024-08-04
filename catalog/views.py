from django.views import generic
from django.urls import reverse_lazy
from django.views.generic import View

from catalog.models import Task, Tag
from catalog.forms import TaskForm
from django.shortcuts import get_object_or_404, redirect


class HomePageView(generic.ListView):
    model = Task
    template_name = "home.html"
    context_object_name = "tasks_list"
    paginate_by = 7

    def get_queryset(self):
        return Task.objects.order_by("is_done", "-created_at")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tags.html"
    context_object_name = "tags_list"
    paginate_by = 7


class AddTask(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "add-update-task.html"
    success_url = reverse_lazy("home")


class ChangeStatus(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, id=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect("home")


class UpdateTask(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "add-update-task.html"
    success_url = reverse_lazy("home")


class DeleteTask(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("home")


class AddTag(generic.CreateView):
    model = Tag
    template_name = "add-update-tag.html"
    success_url = reverse_lazy("tags")
    fields = "__all__"


class UpdateTag(generic.UpdateView):
    model = Tag
    template_name = "add-update-tag.html"
    success_url = reverse_lazy("tags")
    fields = "__all__"


class DeleteTag(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("tags")

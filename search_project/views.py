from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Project
from .forms import ProjectForm


# Create your views here.

@login_required
def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            project.custom_tag_set.add(*project.tag_parser())
            messages.success(request, "새 프로젝트를 생성했습니다.")
            return redirect(project) # TODO: get_absolute_url 활용해볼것
    else:
        form = ProjectForm()

    return render(request, "search_project/project_form.html", {
        "form":form
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'search_project/project_detail.html',{
        "project" : project,
    })
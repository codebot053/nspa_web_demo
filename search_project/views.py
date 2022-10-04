from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from django.contrib import messages
# Create your views here.

@login_required
def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.author = request.user
            project.save()
            messages.success(request, "새 프로젝트를 생성했습니다.")
            return redirect('/') # TODO: get_absolute_url 활용해볼것
    else:
        form = ProjectForm()

    return render(request, "search_project/project_form.html", {
        "form":form
    })
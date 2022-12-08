from django.shortcuts import render
from django.views import generic
from django.http import FileResponse, HttpResponse

from pathlib import Path

from .models import PortfolioProject, SkillsBar, SiteInfo



def index_view(request):
    all_project = PortfolioProject.objects.all()
    filters = set([project.data_filter for project in all_project])
    skills = SkillsBar.objects.all()
    site_info = SiteInfo.objects.get(main_page=True)
    # Делим навыки на две части, чтобы разделить их на две соседние таблицы
    first_skills = skills[:len(skills) // 2 + 1]
    second_skills = skills[len(skills) // 2 + 1::]
    return render(request, 'index.html', {'all_project': all_project, 'filters': filters, 'first_skills': first_skills,
                                          'second_skills': second_skills, 'info': site_info, })


def download_view(request):
    site_info = SiteInfo.objects.get(main_page=True)
    # Передаётся адрес файла без первого символа,
    # потому что путь файла "/media/resume.pdf" не считывается
    path_to_file = Path().cwd() / site_info.resume_file.url[1:]
    return FileResponse(path_to_file.open('rb'))

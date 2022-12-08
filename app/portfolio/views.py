from django.shortcuts import render
from .models import PortfolioProject, SkillsBar, SiteInfo
import math


def index_view(request):
    all_project = PortfolioProject.objects.all()
    filters = set([project.data_filter for project in all_project])
    skills = SkillsBar.objects.all()
    site_info = SiteInfo.objects.get(main_page=True)
    # Делим навыки на две части, чтобы разделить их на две соседние таблицы
    first_skills = skills[:math.ceil(len(skills) / 2)]
    second_skills = skills[math.ceil(len(skills) / 2) + 1::]
    return render(request, 'index.html', {'all_project': all_project, 'filters': filters, 'first_skills': first_skills,
                                          'second_skills': second_skills, 'info': site_info, })


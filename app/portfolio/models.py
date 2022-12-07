from django.db import models
from django.core.exceptions import ValidationError


# Модель данных о проекте в портфолио
class PortfolioProject(models.Model):
    title = models.CharField(max_length=50, unique=True)
    image = models.ImageField(null=False)
    about_project = models.TextField(blank=True, max_length=100)
    github_link = models.URLField(blank=True)
    data_filter = models.CharField(max_length=20, null=False)


# Проверка того, что прогресс находиться в пределах от 10 до 100
def validate_progress(value):
    if value not in range(10, 101, 10):
        raise ValidationError(f'{value} is not in range 10 and 100')


# Модель с данными о навыках
class SkillsBar(models.Model):
    title = models.CharField(max_length=50, unique=True, null=False)
    progress = models.IntegerField(validators=[validate_progress],
                                   help_text='Number from 10 to 100 in increments of 10')

    class Meta:
        ordering = ['-progress']


# Модель со всей информацией главной страницы
class SiteInfo(models.Model):
    # Hero Section
    name = models.CharField(null=False, max_length=50)
    profession = models.CharField(max_length=50)
    telegram_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    linkedin_link = models.URLField(blank=True)
    # About Section
    my_photo = models.ImageField(blank=True)
    about_me = models.TextField(blank=True, max_length=500)
    about_profession = models.TextField(blank=True, max_length=500)
    website = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    city = models.CharField(blank=True, max_length=50)
    resume_file = models.FileField(blank=True)
    # Skills Section
    about_skills = models.TextField(max_length=500)
    # Portfolio Section
    about_portfolio = models.TextField(max_length=500)






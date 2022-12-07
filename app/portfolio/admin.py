from django.contrib import admin
from .models import PortfolioProject, SkillsBar, SiteInfo


@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'data_filter']


@admin.register(SkillsBar)
class SkillsBarAdmin(admin.ModelAdmin):
    list_display = ['title', 'progress']


@admin.register(SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Hero Section',
         {
             'fields': ['name', 'profession', 'telegram_link',
                        'github_link', 'linkedin_link']
         }),
        ('About Section',
         {
             'fields': ['my_photo', 'about_me', 'about_profession',
                        'website', 'email', 'city', 'resume_file']
         }),
        ('Skills Section',
         {
             'fields': ['about_skills']
         }),
        ('Portfolio Section',
         {
             'fields': ['about_portfolio']
         }),
    ]
    list_display = ['name', 'profession']


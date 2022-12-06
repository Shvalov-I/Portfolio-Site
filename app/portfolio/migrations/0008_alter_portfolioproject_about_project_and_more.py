# Generated by Django 4.0.5 on 2022-10-27 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_siteinfo_alter_skillsbar_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolioproject',
            name='about_project',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='about_me',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='about_portfolio',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='about_profession',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='about_skills',
            field=models.TextField(max_length=500),
        ),
    ]

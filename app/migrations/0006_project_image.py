# Generated by Django 4.0.5 on 2022-06-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(null=True, upload_to='project_img'),
        ),
    ]

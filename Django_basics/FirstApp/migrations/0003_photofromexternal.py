# Generated by Django 5.1.1 on 2024-12-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0002_studentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoFromExternal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
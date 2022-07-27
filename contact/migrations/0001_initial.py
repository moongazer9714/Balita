# Generated by Django 4.0.6 on 2022-07-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=222)),
                ('phone', models.CharField(blank=True, max_length=222)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True)),
                ('is_solved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
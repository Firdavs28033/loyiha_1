# Generated by Django 5.0.1 on 2024-02-27 10:32

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fakultet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Kafedra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fakultet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kafedra', to='blog.fakultet')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('kafedra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='blog.kafedra')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(max_length=50)),
                ('audio', models.FileField(blank=True, null=True, upload_to='musics/')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/%y')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('fakultet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='blog.fakultet')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='blog.teacher')),
            ],
        ),
    ]

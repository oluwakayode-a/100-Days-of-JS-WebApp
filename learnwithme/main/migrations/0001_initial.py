# Generated by Django 2.1.7 on 2019-05-29 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('body', models.TextField()),
                ('article_img', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('snippet_1', models.TextField()),
                ('snippet_2', models.TextField(blank=True, null=True)),
                ('snippet_3', models.TextField(blank=True, null=True)),
                ('timestamp', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'get_latest_by': 'id',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=120)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Article')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_reply', models.CharField(max_length=400)),
                ('text_reply', models.TextField()),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
                ('comment_reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='main.Comment')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-06-29 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_category_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='description',
        ),
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

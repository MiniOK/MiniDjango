# Generated by Django 2.2 on 2019-04-10 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_text',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
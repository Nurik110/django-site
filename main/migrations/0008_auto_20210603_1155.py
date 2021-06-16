# Generated by Django 3.2.3 on 2021-06-03 05:55

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210603_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(choices=[('tank', 'tank'), ('support', 'support'), ('fighter', 'fighter'), ('shooter', 'shooter'), ('magician', 'magician'), ('assassin', 'assassin')], default='fighter', max_length=20, verbose_name='Группа')),
            ],
            managers=[
                ('odjects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.RemoveField(
            model_name='heroes',
            name='group',
        ),
    ]

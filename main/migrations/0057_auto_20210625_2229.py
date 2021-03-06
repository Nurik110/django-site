# Generated by Django 3.2.3 on 2021-06-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0056_auto_20210625_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='classs',
            field=models.CharField(choices=[('magatt', 'magatt'), ('deff', 'deff'), ('physatt', 'physatt')], default='magatt', max_length=25, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('tank', 'tank'), ('fighter', 'fighter'), ('shooter', 'shooter'), ('magician', 'magician'), ('assassin', 'assassin'), ('support', 'support')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]

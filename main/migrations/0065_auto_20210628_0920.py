# Generated by Django 3.2.3 on 2021-06-28 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0064_auto_20210628_0914'),
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
            field=models.CharField(choices=[('support', 'support'), ('magician', 'magician'), ('shooter', 'shooter'), ('tank', 'tank'), ('fighter', 'fighter'), ('assassin', 'assassin')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]
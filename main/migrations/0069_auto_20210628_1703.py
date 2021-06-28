# Generated by Django 3.2.3 on 2021-06-28 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_auto_20210628_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='classs',
            field=models.CharField(choices=[('physatt', 'physatt'), ('deff', 'deff'), ('magatt', 'magatt')], default='magatt', max_length=25, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('fighter', 'fighter'), ('support', 'support'), ('magician', 'magician'), ('assassin', 'assassin'), ('shooter', 'shooter'), ('tank', 'tank')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]

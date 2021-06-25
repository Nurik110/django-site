# Generated by Django 3.2.3 on 2021-06-25 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0052_auto_20210625_2225'),
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
            field=models.CharField(choices=[('shooter', 'shooter'), ('magician', 'magician'), ('assassin', 'assassin'), ('fighter', 'fighter'), ('support', 'support'), ('tank', 'tank')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]

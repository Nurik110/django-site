# Generated by Django 3.2.3 on 2021-06-15 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_auto_20210615_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='classs',
            field=models.CharField(choices=[('magatt', 'magatt'), ('physatt', 'physatt'), ('deff', 'deff')], default='magatt', max_length=25, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('tank', 'tank'), ('assassin', 'assassin'), ('support', 'support'), ('fighter', 'fighter'), ('magician', 'magician'), ('shooter', 'shooter')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-12 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0042_auto_20210612_1257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='classs',
        ),
        migrations.AlterField(
            model_name='heroes',
            name='group',
            field=models.CharField(choices=[('magician', 'magician'), ('tank', 'tank'), ('fighter', 'fighter'), ('assassin', 'assassin'), ('support', 'support'), ('shooter', 'shooter')], default='fighter', max_length=20, verbose_name='Группа'),
        ),
    ]

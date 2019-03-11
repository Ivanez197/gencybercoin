# Generated by Django 2.1.2 on 2019-03-10 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0075_auto_20190215_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coderedeemer',
            name='code',
        ),
        migrations.RemoveField(
            model_name='coderedeemer',
            name='username',
        ),
        migrations.AddField(
            model_name='coderedeemer',
            name='code_temp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Code'),
        ),
        migrations.AddField(
            model_name='coderedeemer',
            name='user_data',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.UserData'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# Generated by Django 4.1.2 on 2022-10-11 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_issue_status_remove_issue_type_issue_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='deleted_at',
            field=models.DateTimeField(default=None, null=True, verbose_name='Date of delete'),
        ),
        migrations.AddField(
            model_name='issue',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Delete'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='issue', to='webapp.status', verbose_name='Status'),
        ),
    ]

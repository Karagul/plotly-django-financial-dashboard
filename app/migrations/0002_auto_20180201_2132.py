# Generated by Django 2.0.1 on 2018-02-01 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name='created at')),
                ('updated', models.DateTimeField(verbose_name='updated at')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort_week', models.DateField(verbose_name='week')),
                ('activity_week', models.DateField(verbose_name='act week')),
                ('users', models.IntegerField(verbose_name='customers')),
                ('revenue', models.FloatField(verbose_name='revenue')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Company')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
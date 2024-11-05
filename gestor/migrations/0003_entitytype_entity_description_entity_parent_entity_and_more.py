# Generated by Django 5.0.2 on 2024-11-04 21:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0002_casetype_jurisdiction_alter_case_case_type_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='entity',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='parent_entity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_entities', to='gestor.entity'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='entity_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestor.entitytype'),
        ),
    ]
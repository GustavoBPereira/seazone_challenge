# Generated by Django 4.1.3 on 2022-11-15 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('imovel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=255)),
                ('platform_fee', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('imovel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imovel.imovel')),
            ],
        ),
    ]
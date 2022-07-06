# Generated by Django 4.0.5 on 2022-07-05 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CambioEstadoRT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoraDesde', models.DateTimeField(null=True)),
                ('fechaHoraHasta', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'CambiosEstadosRT',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('descripcion', models.CharField(max_length=500)),
                ('ambito', models.CharField(default='', max_length=50)),
                ('esCancelable', models.BooleanField(default=False)),
                ('esReservable', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recurso.marca')),
            ],
            options={
                'verbose_name_plural': 'Modelos',
            },
        ),
        migrations.CreateModel(
            name='TipoRecursoTecnologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'TipoRecursoTecnologico',
            },
        ),
        migrations.CreateModel(
            name='RecursoTecnologico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroRT', models.IntegerField()),
                ('fechaAlta', models.DateTimeField(auto_now_add=True)),
                ('actual', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='actual', to='recurso.cambioestadort')),
                ('cambioEstadoRT', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cambioEstadoRT', to='recurso.cambioestadort')),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='recurso.modelo')),
                ('tipoRecurso', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='tipo_recurso', to='recurso.tiporecursotecnologico')),
            ],
            options={
                'verbose_name_plural': 'RecursosTecnologicos',
            },
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='imagenes/')),
                ('rt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='recurso.recursotecnologico')),
            ],
        ),
        migrations.AddField(
            model_name='cambioestadort',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recurso.estado'),
        ),
    ]

# Generated by Django 4.0.5 on 2022-07-07 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recurso', '0001_initial'),
        ('mantenimiento', '0002_turno_asignacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='CambioEstadoTurno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaHoraDesde', models.DateTimeField(null=True)),
                ('fechaHoraHasta', models.DateTimeField(blank=True, null=True)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recurso.estado')),
            ],
            options={
                'verbose_name_plural': 'CambiosEstadosTurno',
            },
        ),
        migrations.AlterField(
            model_name='turno',
            name='actual',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='estado_turno_actual', to='mantenimiento.cambioestadoturno'),
        ),
        migrations.AlterField(
            model_name='turno',
            name='cambioEstadoTurno',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='cambio_estado_Turno', to='mantenimiento.cambioestadoturno'),
        ),
    ]

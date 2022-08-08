# Generated by Django 4.1 on 2022-08-08 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=200)),
                ('yazi', models.TextField()),
                ('yaratilis_tarihi', models.DateTimeField(default=django.utils.timezone.now)),
                ('yayinlanma_tarihi', models.DateTimeField(blank=True, null=True)),
                ('yazar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

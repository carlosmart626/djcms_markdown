from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CMSMarkdownPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(
                    primary_key=True,
                    serialize=False,
                    auto_created=True,
                    related_name='djcms_markdown_cmsmarkdownplugin',
                    parent_link=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    to='cms.cmsplugin',
                )),
                ('markdown_text', models.TextField(max_length=80000)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

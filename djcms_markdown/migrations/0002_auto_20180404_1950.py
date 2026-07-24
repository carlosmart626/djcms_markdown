from django.db import migrations
import easymde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('djcms_markdown', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsmarkdownplugin',
            name='markdown_text',
            field=easymde.fields.EasyMDEField(verbose_name='mardown content'),
        ),
    ]

# Generated by Django 4.2.7 on 2024-04-03 12:58

from django.db import migrations
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.contrib.typed_table_block.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtailmarkdown.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpageauthor_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(icon='title')), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock(icon='image', template='includes/imageblock.html')), ('markdown', wagtailmarkdown.blocks.MarkdownBlock(icon='code')), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='code')), ('raw_html', wagtail.blocks.RawHTMLBlock(icon='placeholder')), ('table', wagtail.contrib.table_block.blocks.TableBlock(table_options={'renderer': 'html'}, template='includes/tableblock.html')), ('typed_table', wagtail.contrib.typed_table_block.blocks.TypedTableBlock([('text', wagtail.blocks.CharBlock(required=False)), ('numeric', wagtail.blocks.FloatBlock(required=False)), ('rich_text', wagtail.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('note_well', wagtail.blocks.StructBlock([], icon='placeholder', label='Note Well Text'))], use_json_field=True),
        ),
    ]

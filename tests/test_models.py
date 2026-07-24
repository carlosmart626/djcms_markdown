from django.test import TestCase

from djcms_markdown.models import CMSMarkdownPlugin


class CMSMarkdownPluginTestCase(TestCase):

    def test_models(self):
        markdown = CMSMarkdownPlugin.objects.create(markdown_text='# Test')
        assert markdown.markdown_text == '# Test'

    def test_str_short(self):
        markdown = CMSMarkdownPlugin(markdown_text='# Test')
        assert str(markdown) == '# Test'

    def test_str_truncated(self):
        text = 'x' * 100
        markdown = CMSMarkdownPlugin(markdown_text=text)
        assert str(markdown) == 'x' * 50 + '...'

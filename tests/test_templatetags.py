from django.template import Context, Template
from django.test import SimpleTestCase

from djcms_markdown.templatetags.markdownify import markdown


class MarkdownFilterTestCase(SimpleTestCase):

    def test_heading(self):
        assert '<h1>Hello</h1>' in markdown('# Hello')

    def test_plain_code_block(self):
        result = markdown('```\nfoo\n```')
        assert '<pre><code>' in result
        assert 'highlight' not in result

    def test_highlighted_code_block(self):
        result = markdown('```python\ndef hello():\n    return 1\n```')
        assert 'class="highlight"' in result
        assert '<span class="k">def</span>' in result
        assert '```' not in result

    def test_unknown_language_falls_back(self):
        result = markdown('```notalanguage\nfoo\n```')
        assert '<pre><code>' in result

    def test_template_filter(self):
        tpl = Template('{% load markdownify %}{{ text|markdown|safe }}')
        out = tpl.render(Context({'text': '# Hi'}))
        assert '<h1>Hi</h1>' in out

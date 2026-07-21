from cms.api import add_plugin, create_page
from django.test import TestCase

MARKDOWN = """# Hello World

Some *text* here.

```python
def hello():
    return 1
```
"""


class DJMarkdownCMSPluginTestCase(TestCase):

    def _build_page(self):
        page = create_page(
            title='Home',
            template='base.html',
            language='en',
            slug='home',
            in_navigation=True,
        )
        page.set_as_homepage()
        content = page.get_content_obj('en')
        placeholder = content.get_placeholders().get(slot='content')
        add_plugin(placeholder, 'DJMarkdownCMSPlugin', 'en', markdown_text=MARKDOWN)
        return page

    def test_plugin_renders_markdown_on_page(self):
        self._build_page()
        response = self.client.get('/en/')
        self.assertEqual(response.status_code, 200)
        html = response.content.decode()

        # markdown converted, not raw
        self.assertIn('<h1>Hello World</h1>', html)
        self.assertIn('<em>text</em>', html)
        self.assertNotIn('# Hello World', html)
        self.assertNotIn('```', html)

        # pygments syntax highlighting present
        self.assertIn('class="highlight"', html)
        self.assertIn('<span class="k">def</span>', html)

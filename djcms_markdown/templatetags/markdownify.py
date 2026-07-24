import mistune
from django import template
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from pygments.util import ClassNotFound

register = template.Library()


class HighlightRenderer(mistune.HTMLRenderer):
    def block_code(self, code, info=None):
        lang = info.strip().split(None, 1)[0] if info else None
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        try:
            lexer = get_lexer_by_name(lang, stripall=True)
        except ClassNotFound:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)


@register.filter
def markdown(value):
    renderer = HighlightRenderer()
    markdown_parser = mistune.create_markdown(renderer=renderer)
    return markdown_parser(value)

from cms.models import CMSPlugin
from easymde.fields import EasyMDEField


class CMSMarkdownPlugin(CMSPlugin):
    markdown_text = EasyMDEField(verbose_name='mardown content')

    def __str__(self):
        text = self.markdown_text
        return (text[:50] + '...') if len(text) > 53 else text

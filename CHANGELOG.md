# Changelog

## 0.3.0 (unreleased)

### Breaking changes

* **Raw HTML embedded in markdown is now escaped by default.**
  The renderer was migrated from `mistune` 0.8 to `mistune` 3.x. Mistune 0.8's
  `Renderer` defaulted to `escape=False`, so any raw HTML written inside a
  markdown plugin (iframes, video embeds, custom `<div>`s, script tags, ...)
  was passed straight through to the page. Mistune 3's `HTMLRenderer` defaults
  to `escape=True`, which is what this release ships.

  As a result, existing content containing raw HTML now renders as literal,
  visible text (`&lt;iframe ...&gt;`) instead of being interpreted as markup.

  This is a **deliberate security improvement**: markdown authored by CMS
  editors is rendered with `|safe` in the plugin template, so unescaped raw
  HTML meant any user who could edit a markdown plugin could inject arbitrary
  HTML/JavaScript into the page.

  **Migration:** review existing `CMSMarkdownPlugin` content for embedded raw
  HTML before upgrading, and move that markup into a dedicated template or
  another CMS plugin (e.g. an HTML/video plugin) rather than the markdown body.

### Changed

* Support matrix updated to Python 3.10 - 3.14, Django 5.2 LTS and
  django-cms 5.1.
* Editor migrated to `django-easymde`.
* Added a `pytest-django` test suite and GitHub Actions CI.
* `packaging` is now declared as an explicit runtime dependency.
* README: syntax highlighting instructions now describe Pygments stylesheets
  (the actual server-side output) instead of highlight.js.

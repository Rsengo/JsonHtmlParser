from yattag import Doc
from src.json_html_parser.css_parser import parse_css_selector


class HtmlTag:
    def __init__(self, selector):
        parsed_selector = parse_css_selector(selector)
        self._tag = parsed_selector.tag
        self._identity = parsed_selector.identity
        self._classes = parsed_selector.classes

    def get_html(self, content, escape=True):
        doc, tag, text = Doc().tagtext()
        with tag(self._tag):
            text(content) if escape else doc.asis(content)
            if self._identity:
                doc.attr(id=self._identity)
            if self._classes:
                doc.attr(klass=self._classes)
        return doc.getvalue()


class ListHtmlTag(HtmlTag):
    def __init__(self):
        super().__init__('ul')


class ListItemHtmlTag(HtmlTag):
    def __init__(self):
        super().__init__('li')

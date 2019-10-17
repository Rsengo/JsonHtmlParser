from yattag import Doc


class HtmlTag:
    def __init__(self, selector):
        self._tag = selector

    def get_html(self, content, escape=True):
        doc, tag, text = Doc().tagtext()
        with tag(self._tag):
            text(content) if escape else doc.asis(content)
        return doc.getvalue()


class ListHtmlTag(HtmlTag):
    def __init__(self):
        super().__init__('ul')


class ListItemHtmlTag(HtmlTag):
    def __init__(self):
        super().__init__('li')

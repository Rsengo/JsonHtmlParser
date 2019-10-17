from yattag import Doc


class HtmlTag:
    def __init__(self, selector):
        self._tag = selector

    def get_html(self, content):
        doc, tag, text = Doc().tagtext()
        with tag(self._tag):
            text(content)
        return doc.getvalue()

from yattag import Doc

JSON_TO_HTML_TAG_DICT = {
    'body': 'p',
    'title': 'h1'
}


class HtmlTag:
    def __init__(self, selector):
        if selector not in JSON_TO_HTML_TAG_DICT:
            raise KeyError('HTML-тэг не найден')

        self._tag = JSON_TO_HTML_TAG_DICT[selector]

    def get_html(self, content):
        doc, tag, text = Doc().tagtext()
        with tag(self._tag):
            text(content)
        return doc.getvalue()

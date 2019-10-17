from src.json_html_parser.html_tags import HtmlTag


HTML_TAG_SEPARATOR = ''


def parse_dict(node_info):
    elements = [
        HtmlTag(tag).get_html(content)
        for (tag, content)
        in node_info.items()
    ]

    return HTML_TAG_SEPARATOR.join(elements)


def parse_array(json_data):
    nodes = [parse_json_to_html(i) for i in json_data]

    return HTML_TAG_SEPARATOR.join(nodes)


def parse_json_to_html(json_data):
    if isinstance(json_data, list):
        return parse_array(json_data)

    if isinstance(json_data, dict):
        return parse_dict(json_data)

    raise ValueError('Неверный JSON')

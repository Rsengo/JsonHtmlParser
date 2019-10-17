from src.json_html_parser.html_tags import *

HTML_TAG_SEPARATOR = ''


def parse_node(tag, content):
    data = None
    escape = False

    if isinstance(content, list):
        data = parse_array(content)

    if isinstance(content, dict):
        data = parse_dict(content)

    if isinstance(content, str):
        data = content
        escape = True

    if data is None:
        raise ValueError('Неверный JSON')

    return HtmlTag(tag).get_html(data, escape=escape)


def parse_dict(node_info, in_list=False):
    elements = [
        parse_node(tag, content)
        for (tag, content)
        in node_info.items()
    ]
    html_part = HTML_TAG_SEPARATOR.join(elements)

    return ListItemHtmlTag().get_html(html_part, escape=False) if in_list else html_part


def parse_array(json_data, in_list=False):
    nodes = [parse_json_to_html(i, in_list=True) for i in json_data]
    html_part = HTML_TAG_SEPARATOR.join(nodes)
    list_html_part = ListHtmlTag().get_html(html_part, escape=False)
    return ListItemHtmlTag().get_html(list_html_part, escape=False) if in_list else list_html_part


def parse_json_to_html(json_data, in_list=False):
    if isinstance(json_data, list):
        return parse_array(json_data, in_list)

    if isinstance(json_data, dict):
        return parse_dict(json_data, in_list)

    raise ValueError('Неверный JSON')

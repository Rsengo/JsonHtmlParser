import tinycss2
from src.json_html_parser.css_selector import CssSelector


CSS_EMPTY_RULE_POSTFIX = '{}'
CSS_CLASS_SEPARATOR = ' '

HASH_TYPE = 'hash'
IDENT_TYPE = 'ident'


def parse_css_selector(selector):
    rules = tinycss2.parse_one_rule(f'{selector} {CSS_EMPTY_RULE_POSTFIX}')
    tokens = rules.prelude

    tag_token, *tokens = tokens
    tag = tag_token.value

    identity_tokens = [i for i in tokens if i.type == HASH_TYPE]
    identity = identity_tokens[0].value if identity_tokens else None

    class_tokens = [i for i in tokens if i.type == IDENT_TYPE]
    classes = CSS_CLASS_SEPARATOR.join([i.value for i in class_tokens]) if class_tokens else None

    return CssSelector(tag, identity, classes)

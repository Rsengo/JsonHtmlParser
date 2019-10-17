from src.json_html_parser.parser import parse_json_to_html
from src.json_html_parser.json_reader import deserialize

if __name__ == '__main__':
    json = deserialize('source.json')
    html = parse_json_to_html(json)

    print(html)

import unittest
from src.json_html_parser.parser import parse_json_to_html


class JsonToHtmlParsingTests(unittest.TestCase):
    def test_array_parsing(self):
        json_data = [
            {
                "h3": "Title #1",
                "div": "Hello, World 1!"
            },
            {
                "h3": "Title #2",
                "div": "Hello, World 2!"
            }
        ]
        html = '<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li><li><h3>Title #2</h3><div>Hello, ' \
               'World 2!</div></li></ul>'

        parsed = parse_json_to_html(json_data)

        self.assertEqual(parsed, html)

    def test_dict_parsing(self):
        json_data = {
            "h3": "Title #1",
            "div": "Hello, World 1!"
        }
        html = '<h3>Title #1</h3><div>Hello, World 1!</div>'

        parsed = parse_json_to_html(json_data)

        self.assertEqual(parsed, html)


if __name__ == '__main__':
    unittest.main()

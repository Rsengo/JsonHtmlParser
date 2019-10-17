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
                "h1": "Title #2",
                "span": "Hello, World 2!"
            },
        ]
        html = '<h3>Title #1</h3><div>Hello, World 1!</div><h1>Title #2</h1><span>Hello, World 2!</span>'

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

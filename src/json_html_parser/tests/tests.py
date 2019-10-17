import unittest
from src.json_html_parser.parser import parse_json_to_html


class JsonToHtmlParsingTests(unittest.TestCase):
    def test_array_parsing(self):
        json_data = [
            {
                "title": "Title #1",
                "body": "Hello, World 1!"
            },
            {
                "title": "Title #2",
                "body": "Hello, World 2!"
            }
        ]
        html = '<h1>Title #1</h1><p>Hello, World 1!</p><h1>Title #2</h1><p>Hello, World 2!</p>'

        parsed = parse_json_to_html(json_data)

        self.assertEqual(parsed, html)

    def test_dict_parsing(self):
        json_data = {
            "title": "Title #1",
            "body": "Hello, World 1!"
        }
        html = '<h1>Title #1</h1><p>Hello, World 1!</p>'

        parsed = parse_json_to_html(json_data)

        self.assertEqual(parsed, html)


if __name__ == '__main__':
    unittest.main()

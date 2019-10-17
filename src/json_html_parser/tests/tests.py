import unittest
from src.json_html_parser.parser import parse_json_to_html


class JsonToHtmlParsingTests(unittest.TestCase):
    def test_array_parsing(self):
        json_data = [
            {
                "span": "Title #1",
                "content": [
                    {
                        "p": "Example 1",
                        "header": "header 1"
                    }
                ]
            },
            {
                "div": "div 1"
            }
        ]

        html = '<ul><li><span>Title #1</span><content><ul><li><p>Example 1</p><header>header ' \
               '1</header></li></ul></content></li><li><div>div 1</div></li></ul>'

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

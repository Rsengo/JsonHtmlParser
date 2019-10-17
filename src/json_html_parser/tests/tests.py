import unittest
from src.json_html_parser.parser import parse_json_to_html


class JsonToHtmlParsingTests(unittest.TestCase):
    def test_array_parsing(self):
        json_data = [
            {
                "p.my-class#my-id": "hello",
                "p.my-class1.my-class2": "example<a>asd</a>"
            }
        ]

        html = '<ul><li><p id="my-id" class="my-class">hello</p><p class="my-class1 ' \
               'my-class2">example&lt;a&gt;asd&lt;/a&gt;</p></li></ul>'

        parsed = parse_json_to_html(json_data)

        self.assertEqual(parsed, html)

    def test_dict_parsing(self):
        json_data = {
            "p.my-class#my-id": "hello",
            "p.my-class1.my-class2": "example<a>asd</a>"
        }
        html = '<p id="my-id" class="my-class">hello</p><p class="my-class1 ' \
               'my-class2">example&lt;a&gt;asd&lt;/a&gt;</p>'

        parsed = parse_json_to_html(json_data)

        self.assertEqual(parsed, html)


if __name__ == '__main__':
    unittest.main()

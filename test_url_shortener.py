import unittest
from url_shortener import UrlShortener

class TestUrlShortener(unittest.TestCase):
    def test_url_shorten(self):
        myUrlShortener = UrlShortener()
        input_url = "www.ashna.com/jamal/anchal/kurishinmukku"
        base_url = "www.ashna.com/"
        counter = 1
        short_code = UrlShortener.url_shorten(myUrlShortener, input_url, counter)
        self.assertEqual(len(base_url)+1, len(short_code))

    def test_url_decode(self):
        myUrlShortener = UrlShortener()
        input_url = "www.ashna.com/jamal/anchal/kurishinmukku"
        counter = 1
        short_url = myUrlShortener.url_shorten(input_url, counter)
        decoded_url = myUrlShortener.url_decoder(short_url)
        self.assertEqual(decoded_url, input_url)

if __name__ == "__main__":
    unittest.main()
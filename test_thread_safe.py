import unittest
import threading
from thread_safe_url_shortener import UrlShortener

class TestUrlShortener(unittest.TestCase):
    def setUp(self):
        self.url_shortener = UrlShortener()

    def test_single_thread_shorten_and_decode(self):
        url = "www.example.com/page/1"
        counter = 1
        shortened_url = self.url_shortener.url_shorten(url, counter)
        self.assertEqual(shortened_url, "www.example.com/1")

        decoded_url = self.url_shortener.url_decoder(shortened_url)
        self.assertEqual(decoded_url, url)

    def test_multiple_threads(self):
        def shorten_urls():
            for i in range(5):
                url = f"www.example.com/page/{i}"
                shortened_url = self.url_shortener.url_shorten(url, i)
                self.assertTrue(shortened_url.startswith("www.example.com/"))

        def decode_urls():
            for i in range(5):
                url = f"www.example.com/{i}"
                decoded_url = self.url_shortener.url_decoder(url)
                if decoded_url:
                    self.assertTrue(decoded_url.startswith("www.example.com/page/"))

        threads = []
        threads.append(threading.Thread(target=shorten_urls))
        threads.append(threading.Thread(target=decode_urls))

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    def test_collision_handling(self):
        url1 = "www.example.com/page/1"
        url2 = "www.example.com/page/11"
        self.url_shortener.url_shorten(url1, 1)
        with self.assertRaises(ValueError):
            self.url_shortener.url_shorten(url2, 11)

    def test_invalid_url_format_shorten(self):
        with self.assertRaises(ValueError):
            self.url_shortener.url_shorten("invalid-url", 1)

    def test_invalid_url_format_decode(self):
        with self.assertRaises(ValueError):
            self.url_shortener.url_decoder("invalid-short-url")

if __name__ == "__main__":
    unittest.main()


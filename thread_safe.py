import threading

class UrlShortener:
    """A thread-safe URL shortener class."""

    def __init__(self):
        """Initialize the hashtable and lock."""
        self.hash_map = {}
        self.lock = threading.Lock()  # Lock for thread safety

    def url_shorten(self, url, counter):
        """Shorten the given URL."""
        with self.lock:  # Lock to synchronize access
            ind = url.index("/")
            base_url = url[:ind + 1]
            if url in self.hash_map.values():
                for key, value in self.hash_map.items():
                    if value == url:
                        wanted_key = key
                        print(self.hash_map)
                        return base_url + str(wanted_key)
            short_code = counter % 10
            self.hash_map[short_code] = url
            print(self.hash_map)
            return base_url + str(short_code)

    def url_decoder(self, url):
        """Decode the shortened URL."""
        with self.lock:  # Lock to synchronize access
            a = self.hash_map.get(int(url[-1]))
            return a


def main():
    """Main function to run the URL shortener."""
    my_url_shortener = UrlShortener()
    counter = 1

    def shorten_urls():
        nonlocal counter
        for _ in range(5):  # Simulate multiple shorten calls
            url = "www.example.com/page/" + str(counter)
            shortened_url = my_url_shortener.url_shorten(url, counter)
            counter += 10
            print(f"Shortened: {shortened_url}")

    def decode_urls():
        for short_code in range(5):  # Simulate multiple decode calls
            url = f"www.example.com/{short_code}"
            decoded_url = my_url_shortener.url_decoder(url)
            print(f"Decoded: {decoded_url}")

    # Create threads for shortening and decoding URLs
    threads = []
    threads.append(threading.Thread(target=shorten_urls))
    threads.append(threading.Thread(target=decode_urls))

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for threads to complete
    for thread in threads:
        thread.join()


if __name__ == "__main__":
    main()

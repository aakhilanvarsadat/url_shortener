#Assume hashtable length = 10/100/1000/infinite
#"www.ashna.com/jamal/anchal/kurishinmukku"

"""Docstring"""
class UrlShortener:
    """Docstring"""

    def __init__(self):
        """Docstring"""
        self.hash_map = {}

    def url_shorten(self, url, counter):
        """Docstring"""
        
        ind = url.index("/")
        base_url = url[:ind+1]
        if url in self.hash_map.values():
            for key, value in self.hash_map.items():
                if value == url:
                    wanted_key = key
                    print(self.hash_map)
                    return base_url+str(wanted_key)
        short_code = counter % 10
        self.hash_map[short_code] = url
        print(self.hash_map)
        return base_url+str(short_code)

    def url_decoder(self, url):
        """Docstring"""
        a = self.hash_map.get(int(url[-1]))
        return a

def main():
    """Docstring"""

    my_url_shortener = UrlShortener()
    counter = 1
    while True:
        print("Select an operation")
        user_input = int(input("Enter 1: Shorten, 2:Decode"))
        if user_input == 1:
            url = input("Enter the url")
            shortened_url = my_url_shortener.url_shorten(url, counter)
            counter = counter  + 10
            print(shortened_url)
        if user_input == 2:
            url = input("Enter the url")
            counter = url[-1]
            decoded_url = my_url_shortener.url_decoder(url)
            print(decoded_url)

if __name__ == "__main__":
    main()

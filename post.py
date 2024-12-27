import psycopg2

class UrlShortener:
    """URL Shortener with PostgreSQL"""

    def __init__(self):
        """Initialize the database connection"""
        self.connection = psycopg2.connect(
            dbname="url_shortener",
            user="your_username",   # Replace with your PostgreSQL username
            password="your_password",   # Replace with your PostgreSQL password
            host="localhost",
            port="5432"
        )
        self.cursor = self.connection.cursor()

    def url_shorten(self, url, counter):
        """Shorten the URL and store it in the database"""
        
        ind = url.index("/")
        base_url = url[:ind+1]

        # Check if the URL is already stored
        self.cursor.execute("SELECT short_code FROM urls WHERE original_url = %s", (url,))
        result = self.cursor.fetchone()

        if result:
            # If URL already exists, return the existing short code
            print("URL already shortened:", result)
            return base_url + str(result[0])

        # Generate a new short code
        short_code = counter % 10

        # Store the new short code and URL in the database
        self.cursor.execute("INSERT INTO urls (short_code, original_url) VALUES (%s, %s)", (short_code, url))
        self.connection.commit()

        print(f"Shortened URL stored: {short_code} -> {url}")
        return base_url + str(short_code)

    def url_decoder(self, url):
        """Decode the shortened URL to get the original URL"""
        short_code = int(url[-1])
        self.cursor.execute("SELECT original_url FROM urls WHERE short_code = %s", (short_code,))
        result = self.cursor.fetchone()

        if result:
            return result[0]
        else:
            return "Short code not found!"

    def close_connection(self):
        """Close the database connection"""
        self.cursor.close()
        self.connection.close()

def main():
    """Main Function"""
    my_url_shortener = UrlShortener()
    counter = 1

    try:
        while True:
            print("Select an operation")
            user_input = int(input("Enter 1: Shorten, 2: Decode"))
            if user_input == 1:
                url = input("Enter the URL: ")
                shortened_url = my_url_shortener.url_shorten(url, counter)
                counter += 10
                print("Shortened URL:", shortened_url)
            elif user_input == 2:
                url = input("Enter the shortened URL: ")
                decoded_url = my_url_shortener.url_decoder(url)
                print("Original URL:", decoded_url)
            else:
                print("Invalid input!")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        my_url_shortener.close_connection()

if __name__ == "__main__":
    main()

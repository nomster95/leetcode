class Codec:
    def __init__ (self):
        self.url = {}
        self.counter = 1
        self.base_url = "http://tinyurl.com/"



    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        key = str(self.counter)
        self.url[key] = longUrl
        self.counter+=1

        return self.base_url + key
        

        
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.split("/")[-1]

        return self.url[key]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
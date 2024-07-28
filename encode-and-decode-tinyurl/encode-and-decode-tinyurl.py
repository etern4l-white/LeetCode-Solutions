import base64

class Codec:

    def encode(self, longUrl: str) -> str:
        return '/'.join(longUrl.split('/')[:-1]) + '/' + base64.b64encode(longUrl.split('/')[-1].encode()).decode().replace('/', '###')
    

    def decode(self, shortUrl: str) -> str:
        return '/'.join(shortUrl.split('/')[:-1]) + '/' + base64.b64decode(shortUrl.split('/')[-1].replace('###', '/').encode()).decode()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

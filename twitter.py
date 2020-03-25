import twitter

class Twitter():
    def __init__(self):
        self.api = twitter.Api(consumer_key='your_consumer_key',
                            consumer_secret='your_consumer_secret',
                            access_token_key='your_access_token_key',
                            access_token_secret='your_access_token_secret')

    def post_msg(self):
        response = self.api.PostUpdate("Teste Post")


    if __name__ == "__main__":                
        tw.post_msg()
tw = Twitter()
    
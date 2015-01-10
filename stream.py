__author__ = 'meisami'
import oauth2 as oauth
import urllib2 as urllib
# You need to create an application on Twitter to be given the required credentials
access_token_key = "1663795490-ABOsHcTINlA9MfbJydHORLPFmXE3TR85FkdlQ5B"
access_token_secret = "q6pWjZ9zGjPbrm90WWmAnHsnmkmphLFrU1QkxqVW7LLeX"

consumer_key = "FwqKoAirjZxQccgaQ48HFcrCW"
consumer_secret = "8MH5UPOEfk3EhnShYHKR8Wp1paCozB0u166p9UVlgF4HOnmuMq"

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()

http_method = "GET"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url,
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url()

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url, encoded_post_data)

  return response

def getsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  parameters = []
  response = twitterreq(url, "GET", parameters)
  file = open('samples.txt', 'w')
  for line in response:
    file.write(line.strip())
    file.write('\n')

if __name__ == '__main__':
  getsamples()

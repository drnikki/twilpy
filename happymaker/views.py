import foursquare


from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)



## this works aaahhmaaazingly.  woofy.
def foursquare_connect(request):

  client = foursquare.Foursquare(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
  venue = client.venues('4a7af3e6f964a520afe91fe3')
  html = "<html><body>wah wah %s. </body></html>" % venue
  return HttpResponse(html)
  
  
def twil_test(requet):
  from twilio.rest import TwilioRestClient


  client = TwilioRestClient(account, token)
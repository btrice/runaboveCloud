from runabove import Runabove

application_key = '52tSKhS9sdpKJjWS'
application_secret = 'jILFGpLpOnVY3eYb3CMYkCbJzjiqSplP'

# Create an instance of Runabove SDK interface
run = Runabove(application_key, application_secret)

# Request an URL to securely authenticate the user
print "You should login here: %s" % run.get_login_url()
raw_input("When you are logged, press Enter")

# Show the consumer key
print "Your consumer key is: %s" % run.get_consumer_key()


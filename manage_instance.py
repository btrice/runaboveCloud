#avant tout installer python-runabove
#pip install python-runabove
from runabove import Runabove

application_key = '52tSKhS9sdpKJjWS'
application_secret = 'jILFGpLpOnVY3eYb3CMYkCbJzjiqSplP'
consumer_key = 'nekNTiHtcDaznSMzbskh2V2O8GyXGag9'

# Create the Runabove SDK interface

run = Runabove(application_key,
               application_secret,
               consumer_key=consumer_key)
account = run.account

print("get", account.get())
print("email", account.get().email)
print("account_id", account.get().account_id)
print("last name", account.get().last_name)

region = run.regions
print region.list() #la liste de region est vide vu que le compte n'est pas lié à mode de paiement ou à un bon de réduction, le bon sur le site runAbove n'est pas valide sur 
#on ne peut pas donc créer une instance
'''region = run.regions.list().pop()
print("region:", region)

# Get a region, flavor and image
flavor = run.flavors.list_by_region(region).pop()
image = run.images.list_by_region(region).pop()

# Launch a new instance
instance = run.instances.create(region, 'My instance', flavor, image)

# List instances
print 'Instances:'
for i in run.instances.list():
    print ' - %s (%s)' % (i.name, i.image.name)

# Delete the newly created instance
instance.delete()
print '%s deleted' % instance.name'''

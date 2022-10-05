# Import the LaunchDarkly client.
import ldclient
from ldclient.config import Config

# Create a helper function for rendering messages.
def show_message(s):
  print("*** %s" % s)
  print()

# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
  ldclient.set_config(Config("sdk-8caaff9f-652f-431f-b42e-2d4ce679beab"))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
  show_message("SDK successfully initialized!")
else:
  show_message("SDK failed to initialize")
  exit()

# Set up the user properties. This user should appear on your LaunchDarkly users dashboard
# soon after you run the demo.
customer_list = [{'name' : 'Manjeet', 'email' : 'manjeet@gmail.com'}, 
             {'name' : 'Akshat',  'email' : 'akshat@yahoo.com'},
             {'name' : 'Nikhil', 'email' : 'nikhil@aol.com'}]
for customer in customer_list:
	user = {
        "key": "customers",
  	"name": customer['name'],
        "email": customer['email']
	}
	print(customer)
# Call LaunchDarkly with the feature flag key you want to evaluate.
	flag_value = ldclient.get().variation("background", user, False)

	show_message("Feature flag 'background' is %s for this user "  % (flag_value))

# Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
# events to LaunchDarkly before the program exits. If analytics events are not delivered,
# the user properties and flag usage statistics will not appear on your dashboard. In a
# normal long-running application, the SDK would continue running and events would be
# delivered automatically in the background.
ldclient.get().close()
a483e7b4a30a:launchDarkly prikau$ cat test.py 
# Import the LaunchDarkly client.
import ldclient
from ldclient.config import Config

# Create a helper function for rendering messages.
def show_message(s):
  print("*** %s" % s)
  print()

# Initialize the ldclient with your environment-specific SDK key.
if __name__ == "__main__":
  ldclient.set_config(Config("xx-xxxx-xxxxx-xxxxx))

# The SDK starts up the first time ldclient.get() is called.
if ldclient.get().is_initialized():
  show_message("SDK successfully initialized!")
else:
  show_message("SDK failed to initialize")
  exit()

# Set up the user properties. This user should appear on your LaunchDarkly users dashboard
# soon after you run the demo.
customer_list = [{'name' : 'Manjeet', 'email' : 'manjeet@gmail.com'}, 
             {'name' : 'Akshat',  'email' : 'akshat@yahoo.com'},
             {'name' : 'Nikhil', 'email' : 'nikhil@aol.com'}]
for customer in customer_list:
	  user = {
        "key": "customers",
  	    "name": customer['name'],
        "email": customer['email']
	      }
	  print(customer)
    # Call LaunchDarkly with the feature flag key you want to evaluate.
	  flag_value = ldclient.get().variation("background", user, False)
	  show_message("Feature flag 'background' is %s for this user "  % (flag_value))
# Here we ensure that the SDK shuts down cleanly and has a chance to deliver analytics
# events to LaunchDarkly before the program exits. If analytics events are not delivered,
# the user properties and flag usage statistics will not appear on your dashboard. In a
# normal long-running application, the SDK would continue running and events would be
# delivered automatically in the background.
ldclient.get().close()

**Feature flags is a software technique that enables teams to make changes without additional code. In this example we will use LaunchDarkly to enable feature based on email address of users** 

We will use feature flag based on defined rules. In this example, I am using feature flag "background"  with two possible values , Blue and Red.

**Pre-Requistie**

* Clone repo 
```
git clone <repourl>

cd into ld-demo
```
* Install launchdarkly SDK for  Python 

```
pip3 install requirements.txt
````
* Edit demo.py at line 12 to add your API keys from your launchDarkly account. API key can be accessed on your launcDarkly dashboard from 'Account Settings > Projects> Click project Name> Copy the valye of SDK key  key from corresponding environment .

![Screenshot](api-key.png)


* Following screenshot is an  example of using feature flag  based on target rules. This sample configuration which enables you to configure condition like "contains", "ends with" or operators. Upon recieving user attributes sent by SDK , it returns either a matching variations or you can define default rule below.
![Screenshot](feature-flag.png)

* The above Feature flags implements 2 targetting rules and one default rules based on the email address.

* Refer to line No. 26 which is a sample list of customer/users with attributes like name and email which we are sending to SDK to check flag variations.
  customer_list = [{'name' : 'Manjeet', 'email' : 'manjeet@gmail.com'}, 
             {'name' : 'Akshat',  'email' : 'akshat@yahoo.com'},
             {'name' : 'Nikhil', 'email' : 'nikhil@aol.com'}]
             
* Run following command 
```
python3 demo.py
```
* When you run this as it is following the rule targets as shown in picture below, the sample out put will show case background "Blue" or "Red" depending on the email address match . Sample output like given below.

*** SDK successfully initialized!

{'name': 'Manjeet', 'email': 'manjeet@gmail.com'}
*** Feature flag 'background' is RED for this user 

{'name': 'Akshat', 'email': 'akshat@yahoo.com'}
*** Feature flag 'background' is BLUE for this user 

{'name': 'Nikhil', 'email': 'nikhil@aol.com'}
*** Feature flag 'background' is BLUE for this user 


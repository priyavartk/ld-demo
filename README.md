# ld-demo
This a simple example of how to use feature flag based on defined rules 

pre-Requistie
* Edit demo.py at line 12 to add your API keys from your laundDarkly account.
![Screenshot](apik-key.png)
* Following screenshot is an  example of using feature flag on based on target rulessers. 
![Screenshot](feature-flag.png)
* The above Feature flags implements 2 targetting rules and one default rules based on the email address.
* When you run this as it is following the rule targets as shown in picture below, the sample out put will show case background "Blue" or "Red" depending on the email address match.

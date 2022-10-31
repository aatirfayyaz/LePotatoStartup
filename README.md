This is a simple script that greps the IP for the LePotato or RaspberryPi and sends it to your email so you can use a headless software (like Putty) to remote into it. This is useful if you're using the Columbia University WiFi since it will assign a new IP to your device every time. 

The script is at https://github.com/aatirfayyaz/LePotatoStartup

You can git clone it to your desired directory by simply:

git clone https://github.com/aatirfayyaz/LePotatoStartup
Once you have the file cloned, there are a few things that need to be done to configure it properly.

You will need to change some variables in the code to your desired parameters. You can do this simply by:

nano LePotatoStartup/startup_email.py
Once the file opens, change the following as described below:

to = 'YOUREMAIL@gmail.com'
gmail_user = 'SENDEREMAIL@gmail.com'
gmail_password = 'PASSWORDFROMAPP'

The "to" variable is who you want the email to go to. This could be your primary email address. For "gmail_user", you can use a secondary gmail email address. I suggest creating a new email address to keep the whole process cleaner but any email would do. It is necessary to use a gmail email address if you don't want to change any other parameters.

The "gmail_password" needs to be extracted from the google account settings page. Sign in to your account and click your name on the top right and go to account settings.

![alt text](https://github.com/aatirfayyaz/LePotatoStartup/blob/main/Manage.png?raw=true)


Turn on 2-step verification under security by following all required steps. I configured it for text message to my phone as a secondary verification:


Once complete, you will have access to "App passwords" just below the 2-step verification option. Click on it and generate a new password by clicking on "Other" and adding your desired name to the app. I called it Python. 


Click generate, google will create a password for you. This will be 16 letters. This is what goes in the "gmail_password" variable. No spaces.

Once you have completed this step, you can save and exit nano. Press Ctrl+X, enter "y" when it asks you to 'Save Modified Buffer?' and press enter when it asks for the 'File Name to Write:'

To make sure you have execute permissions, run the following:

sudo chmod +x LePotatoStartup/startup_email.py
To check if the script works, type the following in your terminal window. Use python or python3 depending on your OS's requirement.

python3 LePotatoStartup/startup_email.py
If everything works perfectly, you will an output that has the IP addresses followed by a message saying:

****************************************
Mail Sent Successfully!
****************************************
You will also see that you received an email to your account (shown below). For your headless display, you need the inet address underlined in red.


After making sure that the script is working, the next step is for your potato to automatically send the email on startup.

For that you can add your script to /etc/rc.local by:

sudo nano /etc/rc.local
Enter the following line to the editor (replace the path to your path):

sudo python3 /path/to/github/directory/startup_email.py
Note that if /etc/rc.local did not exist for you OS (as is the case on Ubuntu), you will need to add a shebang line at the top of the file (e.g. #!/bin/bash), and ensure the file is executable:

sudo chmod a+x /etc/rc.local
After completion of all these steps, your LePotato should be configured to send you an email on startup which will contain the IP address so you can SSH into the device! 

Hope this is helpful to some.

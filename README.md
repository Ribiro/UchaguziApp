# Uchaguzi App
## Overview
Uchaguzi App is a web-based election results' transmission system. The development of this application was motivated by delay experienced in transmmitting in the recently conducted Kenya 2022 General Elections. The aim of this project is to ease the election transmission process, and make it as fast and as transparent as possible.

The admin of this application, who in this case is the chief returning officer, will have the previledge of adding candidates, polling stations and their respective presiding officers into the system. The presiding officers will conduct their tallying process as usual and submit the results through the systems. The end user of this system will get to view the cumulative results as they stream from various presiding officers.

**Language and Libraries Used:** Python, Django, Javascript

## Table of Contents
* [Admin](#admin)
* [Presiding Officer](#po)
* [End User](#end-user)
* [Setup](#setup)

<a name="admin"></a>
## Admin
The admin of this system does the majority of the work. They add the details of the various candidates, including their political parties.
They create the various existing various polling stations. The admin also creates accounts for the presiding officers and assigns them to their respective
polling stations. The relationship between a presiding officer and a polling station is one-to-one.


<a name="po"></a>
## Presiding Officer
Upon successful account creation, the presiding officer is able to log into the system and view the various candidates as added by the admin.
The role of the presiding officer is solely to add the results of each candidate as tallied in their polling station, and publish the results
for display to the end user.

<a name="end-user"></a>
## End User
The end user is presented with a well-designed user interface displaying the results as they stream from the presiding officers. The results keep changing as the presiding officers publish them.

Here is a <a href="https://uchaguziapp-production.up.railway.app/">Live Demo</a>

<a name="setup"></a>
## Setup
To run this project, clone it to your local machine and execute the following commands:

```angular2html
$ git clone https://github.com/Ribiro/UchaguziApp.git
$ cd UchaguziApp
$ pip install -r requirements.txt
$ python manage.py runserver
```

Authored by <a target=”_blank”  href="https://github.com/Ribiro">Denis Ribiro</a>

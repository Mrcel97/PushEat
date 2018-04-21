# Multiple Server Solution Schema

## Introduction

This is a document stating a proposal to deploy the solution using multiple servers in a nlayer
(web, application, database) proposal.

## Web aplication description

Our web application will be done with Django and we will be using a PostgreSQL Database to store app information. Therefore, to develop it, we will create a python virtual environment(venv) using djangostack  or  Pycharm IDE. 
To do virtual hosting of multiple servers (specified below), we may use nginx. 


### Number and function of servers.
1. Database server:  
Store web application information.
2. Web server:  
To handle the requests of our users.
3. Application server:  
Shares network-enabled versions of common application software and eliminates the need for software to be installed on each workstation
4. Communications server:  
Handles many common communications functions for the network, such as e-mail, fax, remote access, firewalls or Internet services
5. Domain server:  
Authenticates and authorises computers and users to access resources within the logical domain.
6. File server:  
Stores network users' data files.

### Connections and dependences amongst them.
1. Web server + database server:  
Web server will work with our database server to get data stored on it to handle the users requests.
2. Domain server + Database server:  
Our domain server will need to access to the database server to get the necessary data to authenticate our users correctly.
3. Application server + web server + database server + communications server + domain server + file server:  
Application server will work with our web server (host) and with the database server to store or extract information. Also with all the other servers, because the application will use all the server to work correctly and to achieve all the implemented functionalities. 
4. Database server + File server:   
File server will store temporal user generated information and the important information that user generates will be stored on the database server.

### State which are required and which are optional.

1. Database server (required)
2. Web server (required)
3. Application server (required)
4. Communication server (optional):  
Our server don’t require a communication system if we don’t implement the communication through users. Instead of that we can give their personal information (email, phone, fax, etc) and users will contact using 3rd applications.
5. Domain server (optional):  
Django can support this functionality.
6. File server (optional):  
Django can support this functionality.

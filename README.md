# Project-rate

## sign up
![image](https://user-images.githubusercontent.com/57414671/174163399-49615172-2701-4796-b55e-56141b0338e3.png)
## sign in
![image](https://user-images.githubusercontent.com/57414671/174164033-47f43d73-9bef-4bf5-b15a-8bf6327b57f3.png)
## home
![image](https://user-images.githubusercontent.com/57414671/174163896-681f4fb9-0e7d-4fa2-bffa-df9bcc94bc79.png)
 
 
A user can rate a project by clicking on the image to view more details about the proect i.e. description, url
As a user of the application I should be able to:
* Sign up and login
* Add a project and caption
* Rate a project once 
* Search for a project
* Logout


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
Install Python3 , any code editor e.g VScode

### Installing
 #### Cloning the repository:  
 ```bash 
https://github.com/JoyChristine/Project-rate.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations app
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py runserver 
```

## Running the tests

```bash 
 python manage.py test app
```

### Break down into end to end tests
The tests test for saving and deleting a profiles and projects

```
def test_save_profile(self):
        self.profile.save_profile()
        profile=Profile.objects.all()
        self.assertTrue(len(profile))

```

## Deployment

For deployment, I hosted my app on heroku. https://dashboard.heroku.com/


## Built With
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  
## Contributing

You can fork the repo then create a branch and contribute under that branch


## Authors

* **[Joy Christine](https://github.com/JoyChristine)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details 


<!--  # Project-rate

## sign up
![image](https://user-images.githubusercontent.com/57414671/174163399-49615172-2701-4796-b55e-56141b0338e3.png)
## sign in
![image](https://user-images.githubusercontent.com/57414671/174164033-47f43d73-9bef-4bf5-b15a-8bf6327b57f3.png)
## home
![image](https://user-images.githubusercontent.com/57414671/174163896-681f4fb9-0e7d-4fa2-bffa-df9bcc94bc79.png)
 -->

<!-- ## Description
A user can rate a project by clicking on the image to view more details about the proect i.e. description, url
As a user of the application I should be able to:

* Sign up and login
* Add a project and caption
* Rate a project once 
* Search for a project
* Logout


### Prerequisites

# Setup and Installation  
 -->
  
<!-- #### Cloning the repository:  
 ```bash 
https://github.com/JoyChristine/Project-rate.git
```
#### Navigate into the folder and install requirements  
 ```bash 
cd Picture-Globe pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations app
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py runserver 
```
The application opens up on `127.0.0.1:8000`. <br>
If you want to use new server run e.g 9000
```bash 
 python manage.py runserver 9000
```
##### Testing the application  
 ```bash 
 python manage.py test app
```
##### API EndPoints
```bash 
 Projects API - `127.0.0.1:8000/api/projects`
Profiles API - `127.0.0.1:8000/api/profiles`
```

  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 4.0.4](https://docs.djangoproject.com/en/4.0/)  
* [Heroku](https://heroku.com)  
  


## Authors

* **[Joy Christine](https://github.com/JoyChristine)** 



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details  -->

# Online Examination System

#### Main Features:

- Auto Submit Form as soon as timer runs out
- If student window goes out of focus for 5 times while appearing for an exam professor will receive an email
- Automatic calculation of marks once student submits Exam

#### Overview of project
![image](https://user-images.githubusercontent.com/47894634/117118618-9c1d1b00-adae-11eb-8b61-a6e87578f8da.png)

### Steps to run the project

#### First Clone the project

```
git clone https://github.com/Mohitkumar6122/Online-Examination-System.git
cd Exam-Portal
```

#### Now we will need a .env file for storing email credentials

#### create .env in the Exam-Portal directory

#### Contents of .env file

```
export EMAIL_HOST_PASSWORD=<PASSWORD_OF_EMAIL_ACCOUNT>
export EMAIL_HOST_USER=<EMAIL_ACCOUNT>
export EMAIL_HOST=<SMTP>
export DEFAULT_FROM_EMAIL=<EMAIL_ACCOUNT>
```

#### If on Windows

##### Create a env.bat file with following contents

```
set EMAIL_HOST_PASSWORD=<PASSWORD_OF_EMAIL_ACCOUNT>
set EMAIL_HOST_USER=<EMAIL_ACCOUNT>
set EMAIL_HOST=<SMTP>
set DEFAULT_FROM_EMAIL=<EMAIL_ACCOUNT>
```

#### After creating env file, run following commands:-

```
pip install pipenv
pip install django[argon2]
pipenv shell
pipenv install
```

#### Now if on linux run in cmd

```
source .env
```

#### If on windows

```
env.bat
```

#### After running commands as per OS run:

```
cd Exam
python manage.py migrate
python manage.py makemigrations
python manage.py migrate
```

#### Once done with that create a superuser account:

```
python manage.py createsuperuser
```

#### Once superuser account is created we can run the website

```
python manage.py runserver
```

#### If there are no errors website will be running on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) (default)

#### For creating accounts for professor's we will need a group called Professor

1. Go to [http://127.0.0.1:8000/admin/auth/group/add/](http://127.0.0.1:8000/admin/auth/group/add/)
2. Login with superuser account
3. Add two groups named Professor and Students

#### For Professor verification, admin will need to manually add professor to Professor group once they create a new account

#### Backend Part was developed by 
* [Mohit Kumar](https://github.com/Mohitkumar6122)
* [Harbhajan Singh](https://github.com/harbhajan2109)

#### Frontend Part was developed by 
* [Hritwik Bhardwaj](https://github.com/Hritwik-Bhardwaj)
* [Ahbishek Kapoor](https://github.com/abhishekkumar29)

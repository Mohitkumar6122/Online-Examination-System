# Online Examination System
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

#### The online examination system is a digital platform that evaluates students in a hassle-free way. The entire examination process is simplified and exams are taken from anywhere, anytime.
#### It is developed using Python, Django, CSS, HTML and JavaScript. Talking about the project, it contains an admin side from where a user can take and manage exams easily. The Admin plays an important role in the management of this system. In this project, there is separate interface for students, professors and Admin.

---------------------------------------------------------------------------------------------------------------------
#### Main Features:

- Auto Submit Form as soon as timer runs out
- If student window goes out of focus for 5 times while appearing for an exam professor will receive an email
- Automatic calculation of marks once student submits Exam
- Separate superuser account for account validations
- Two types of users. Professors and Normal (Student) Users
- Separate Control Panel for both admin and students
- Students can take MCQ exam, view score and see correct answers.
- Automatic calculation of results of exam

---------------------------------------------------------------------------------------------------------------------

#### Overview of project
![image](https://user-images.githubusercontent.com/47894634/117118618-9c1d1b00-adae-11eb-8b61-a6e87578f8da.png)

---------------------------------------------------------------------------------------------------------------------

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

---------------------------------------------------------------------------------------------------------------------

#### Backend Part was developed by 
* [Mohit Kumar](https://github.com/Mohitkumar6122)
* [Harbhajan Singh](https://github.com/harbhajan2109)

#### Frontend Part was developed by 
* [Hritwik Bhardwaj](https://github.com/Hritwik-Bhardwaj)
* [Abhishek Kumar](https://github.com/abhishekkumar29)

---------------------------------------------------------------------------------------------------------------------


## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/harbhajan2109"><img src="https://avatars.githubusercontent.com/u/56828657?v=4?s=100" width="100px;" alt=""/><br /><sub><b>harbhajan2109</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=harbhajan2109" title="Code">💻</a></td>

   <td align="center"><a href="https://github.com/Hritwik-Bhardwaj"><img src="https://avatars.githubusercontent.com/u/46474138?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Hritwik Bhardwaj</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=Hritwik-Bhardwaj" title="Code">💻</a></td>

   <td align="center"><a href="https://github.com/abhishekkumar29"><img src="https://avatars.githubusercontent.com/u/83762781?v=4?s=100" width="100px;" alt=""/><br /><sub><b>abhishekkumar29</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=abhishekkumar29" title="Code">💻</a></td>

  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

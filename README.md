# Online Examination System

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

## Introduction
The Online Examination System is a digital platform designed to simplify the examination process, allowing students to take exams from anywhere at any time. It is developed using Python, Django, CSS, HTML, and JavaScript. The system includes separate interfaces for students, professors, and administrators, ensuring a smooth and efficient exam management experience.

## Main Features
- **Auto-Submit Form**: Exams are automatically submitted when the timer runs out.
- **Focus Monitoring**: If a student’s window goes out of focus five times during an exam, the professor receives an email alert.
- **Automatic Mark Calculation**: Marks are calculated automatically once the student submits the exam.
- **User Types**: The system supports two types of users - Professors and Students.
- **Control Panels**: Separate control panels for administrators and students.
- **MCQ Exams**: Students can take multiple-choice exams, view their scores, and see the correct answers.
- **Superuser Account**: Separate superuser account for account validations.

## Project Overview
![Project Overview](https://user-images.githubusercontent.com/47894634/117118618-9c1d1b00-adae-11eb-8b61-a6e87578f8da.png)

## Installation Guide

### Prerequisites
- Python
- Django
- Pipenv

### Steps to Run the Project

1. **Clone the Project**
    ```bash
    git clone https://github.com/Mohitkumar6122/Online-Examination-System.git
    cd Exam-Portal
    ```

2. **Set Up Environment Variables**
    Create a `.env` file in the `Exam-Portal` directory with the following contents:
    ```bash
    export EMAIL_HOST_PASSWORD=<PASSWORD_OF_EMAIL_ACCOUNT>
    export EMAIL_HOST_USER=<EMAIL_ACCOUNT>
    export EMAIL_HOST=<SMTP>
    export DEFAULT_FROM_EMAIL=<EMAIL_ACCOUNT>
    ```

    For Windows, create a `env.bat` file:
    ```bash
    set EMAIL_HOST_PASSWORD=<PASSWORD_OF_EMAIL_ACCOUNT>
    set EMAIL_HOST_USER=<EMAIL_ACCOUNT>
    set EMAIL_HOST=<SMTP>
    set DEFAULT_FROM_EMAIL=<EMAIL_ACCOUNT>
    ```

3. **Install Dependencies**
    ```bash
    pip install pipenv
    pip install django[argon2]
    pipenv shell
    pipenv install
    ```

4. **Load Environment Variables**
    On Linux:
    ```bash
    source .env
    ```
    On Windows:
    ```bash
    env.bat
    ```

5. **Database Migrations**
    ```bash
    cd Exam
    python manage.py migrate
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Create a Superuser Account**
    ```bash
    python manage.py createsuperuser
    ```

7. **Run the Server**
    ```bash
    python manage.py runserver
    ```

    The website should now be running at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

8. **Set Up User Groups**
    - Go to [http://127.0.0.1:8000/admin/auth/group/add/](http://127.0.0.1:8000/admin/auth/group/add/)
    - Login with the superuser account.
    - Add two groups named "Professor" and "Students".

9. **Professor Verification**
    - Admins need to manually add professors to the "Professor" group once they create a new account.

## Contributors ✨

Thanks to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/harbhajan2109"><img src="https://avatars.githubusercontent.com/u/56828657?v=4?s=100" width="100px;" alt="harbhajan2109"/><br /><sub><b>harbhajan2109</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=harbhajan2109" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Hritwik-Bhardwaj"><img src="https://avatars.githubusercontent.com/u/46474138?v=4?s=100" width="100px;" alt="Hritwik Bhardwaj"/><br /><sub><b>Hritwik Bhardwaj</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=Hritwik-Bhardwaj" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/abhishekkumar29"><img src="https://avatars.githubusercontent.com/u/83762781?v=4?s=100" width="100px;" alt="abhishekkumar29"/><br /><sub><b>abhishekkumar29</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=abhishekkumar29" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com"><img src="https://avatars.githubusercontent.com/u/20371468?v=4?s=100" width="100px;" alt="Anthony Aniah Abuokwen"/><br /><sub><b>Anthony Aniah Abuokwen</b></sub></a><br /><a href="https://github.com/Mohitkumar6122/Online-Examination-System/commits?author=anthonyaniah" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>
<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind are welcome!

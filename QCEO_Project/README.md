



# The Beginning of QCEO Project

##### Implementing React to work in Django Templates makes the server structure simple, but there are many limitations to the use of React features.

##### Normally, Frontend(React) and Backend(Django) are implemented separately, and internal communication is implemented using the DRF(Django REST Framework).

##### This project was implemented in the same way.

&nbsp;

## Start Project (Setup)

```powershell
QCEO_Project> pip install virtualenv
QCEO_Project> virtualenv venv		// virtualenv 'name'
QCEO_Project> .\venv\Scripts\Activate
(venv) QCEO_Project> python -m pip install -r requirements.txt

// Initializing DB
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete
$ rm db.sqlite3

QCEO_Django> python manage.py makemigrations
QCEO_Django> python manage.py migrate
QCEO_Django> python manage.py createsuperuser
QCEO_Django> python manage.py runserver

qceo-frontend-react> yarn start
```

&nbsp;

## Django Basic Functional Architecture

## ![image](https://user-images.githubusercontent.com/41619898/79954230-00c54a80-84b8-11ea-8677-1421949bcc3d.png)

### *WSGI

The **Web Server Gateway Interface** (**WSGI**) is a simple calling convention for web servers to forward requests to web applications or frameworks written in the Python programming language

###### Web Framework Benchmarks : https://www.techempower.com/benchmarks/

&nbsp;

## REST API

A **REST API (Representational State Transfer Application Programming Interface)** is a standardized way to provide data to other applications.

Those applications can then use the data however they want.

Sometimes, APIs also offer a way for other applications to make changes to the data.

![image](https://user-images.githubusercontent.com/41619898/79954685-a24c9c00-84b8-11ea-9f62-d793fa800ad9.png)

&nbsp;

### There are a few key options for a REST API request:

- GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
- POST — Creates a new record that gets appended to the database
- PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
- DELETE — Deletes the record at the given URI
- PATCH — Update individual fields of a record

Typically, an API is a window into a database. The API backend handles querying the database and formatting the response. What you receive is a static response, usually in JSON format, of whatever resource you requested.

REST APIs are so commonplace in software development, it’s an essential skill for a developer to know how they work. APIs are how applications communicate with one another or even within themselves.

&nbsp;

### Testing API’s using Postman

![image](https://user-images.githubusercontent.com/41619898/79954973-18510300-84b9-11ea-9a3f-5f019e0dd927.png)

Postman is a great tool when trying to dissect RESTful API’s made by others or test ones you have made yourself.

It offers a sleek user interface with which to make HTML request, without the hassle of writing a bunch of code just to test an API’s functionality.

&nbsp;

![image](https://user-images.githubusercontent.com/41619898/79838633-461d4580-83ee-11ea-9cfe-22f345764bdb.png)

**A typical Django application that uses React as a front end.**

**It needs an API to allow React to consume data from the database.**

&nbsp;

## Django startapp

### #Redmine_Defects

- Implement real-time updates with DRF | Building Redmine API
  - http://project.lsware.co.kr/redmine/projects/omni-pis-qa/issues

![image](https://user-images.githubusercontent.com/41619898/78514741-d142ec80-77ed-11ea-87b9-fe2e8140bc95.png)

&nbsp;

### Automate login using authentication token & Crawling

- http://project.lsware.co.kr/redmine/

![image](https://user-images.githubusercontent.com/41619898/80166020-d9858f00-8617-11ea-8ecc-4b4a0ba011a4.png)

```python
import requests
from bs4 import BeautifulSoup as bs

# 로그인할 유저정보
LOGIN_INFO = {
    'username': '',
    'password': ''
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as session:
    first_page = session.get('http://project.lsware.co.kr/redmine')
    html = first_page.text
    soup = bs(html, 'html.parser')
    authenticity_token = soup.find('input', {'name': 'authenticity_token'})
    print(authenticity_token['value'])

    # {**dict1, **dict2} 으로 dict들을 unpacking
    LOGIN_INFO = {**LOGIN_INFO, **{'authenticity_token': authenticity_token['value']}}
    print(LOGIN_INFO)

    # 다시 로그인
    login_req = session.post('http://project.lsware.co.kr/redmine/login.do', data=LOGIN_INFO)
    print(login_req.status_code)    # 200 이면 성공
    login_req.raise_for_status()

    '''
    urls = [
        'http://project.lsware.co.kr/redmine/projects/omni-pis-qa/issues',
        'http://project.lsware.co.kr/redmine/projects/olis/issues',
        'http://project.lsware.co.kr/redmine/projects/test1',
        'http://project.lsware.co.kr/redmine/projects/test2/issues'
    ]
    '''
    url = 'http://project.lsware.co.kr/redmine/projects/olis/issues'
    res = session.get(url)
    res.raise_for_status()
    html = res.text
    soup = bs(html,'html.parser')
    print(soup)
    table = soup.find_all('div', class_="autoscroll")
    print(table)


```

&nbsp;

### #Redmine_TestSupport

- Implement real-time updates with DRF | Building Redmine API
  - http://project.lsware.co.kr/redmine/projects/olis/issues

&nbsp;

### #Redmine_QualityInspection

- Implement real-time updates with DRF | Building Redmine API
  - http://project.lsware.co.kr/redmine/projects/test1/issues

&nbsp;

### #Accounts / django-rest-knox

- Add Token-based Authentication with Django-rest-knox to an app built with Django and React/Redux

![image](https://user-images.githubusercontent.com/41619898/78620531-3b759300-78bb-11ea-8b02-60212d509d38.png)

| URL              | Detail                               |
| :--------------- | ------------------------------------ |
| api/auth/user    | Retrieve user information            |
| api/aut/register | Return token after user registration |
| api/auth/login   | User Login                           |
| api/auth/logout  | User Logout                          |

<br/>

> ### *Reference material for understanding Knox's certification system
>
> - Apache Knox REST API flow diagrams in Apache Hadoop Ecosystem
>
>   ![image](https://user-images.githubusercontent.com/41619898/80162848-69730b00-860f-11ea-8a47-b3bc9697cb7c.png)
>

&nbsp;

## Asynchronous Operations in React-Redux

### Understanding Synchronous vs Asynchronous

![image](https://user-images.githubusercontent.com/41619898/80166564-3e8db480-8619-11ea-9d3c-aac3ca408308.png)

---------

![image](https://user-images.githubusercontent.com/41619898/80166578-43526880-8619-11ea-98d3-486a21e9947c.png)

--------

![image](https://user-images.githubusercontent.com/41619898/80166779-b360ee80-8619-11ea-9b6c-0f9b9d3233e5.png)

Async/Await is one of the best things ever reaching the Javascript world.

It is a powerful and expressive way to express asynchronous operations.

With all this greatness, overusing it can hurt performance, readability and creates complexity - a complexity that it's just not worth the effort sometimes.

When creating functions, it is a good idea to **give back the control to the function's caller as fast as possible.**

&nbsp;

### JavaScript(React) Promises In Project Code

```javascript
import axios from "axios";

export async function signIn (username, password){
  // Headers
  const config = {
    headers: {
      'Content-Type': 'application/json'
    }
  };

  // Request Body
  const body = JSON.stringify(username, password);
  
  let user = await axios.post('http://localhost:8000/api/auth/login', body, config)
    .then((response) => {
      return response.data;
    })
    .catch((response) => {
      return response.data;
    });

...
```

![image](https://user-images.githubusercontent.com/41619898/79956028-8944ea80-84ba-11ea-9d1a-0751aff13971.png)

It is hard to conceptualize sending a request then waiting for a response without blocking.

Browsers can put the request behind a callback and continue code execution.

The React-Redux libraries do much of the work for you without compromising simplicity.

Think of React as the library that renders UI components in plain HTML.

Redux is the state management library with asynchronous capabilities.

&nbsp;

# Design

- Semantic UI : https://semantic-ui.com/

- Material-UI : https://material-ui.com/

<br/>

# Issues

- Warning: Invalid DOM property `class`. Did you mean `className`?
  - Since JSX is JavaScript, identifiers such as class and for are discouraged as XML attribute names. Instead, React DOM components expect DOM property names like className and htmlFor, respectively.






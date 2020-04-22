



# The beginning of QCEO project

##### Implementing React to work in Django Templates makes the server structure simple, but there are many limitations to the use of React features.

##### Normally, Frontend(React) and Backend(Django) are implemented separately, and internal communication is implemented using the DRF(Django REST Framework).

##### This project was implemented in the same way.

&nbsp;

## Start Project (Setup)

```powershell
QCEO_Project> pip install virtualenv
QCEO_Project> virtualenv venv		// virtualenv 'name'
QCEO_Project> python -m pip install -r requirements.txt

// Initializing DB
$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
$ find . -path "*/migrations/*.pyc" -delete
$ rm db.sqlite3

QCEO_Django> python manage.py makemigrations
QCEO_Django> python manage.py migrate
QCEO_Django> python manage.py runserver

qceo-frontend-react> yarn start
```

&nbsp;

### Django Basic Functional Architecture

![image](https://user-images.githubusercontent.com/41619898/79935731-99e06b00-8490-11ea-93c4-d655ce98e64b.png)

##### REST API | Representational State Transfer Application Programming Interface

A REST API is a standardized way to provide data to other applications. Those applications can then use the data however they want. Sometimes, APIs also offer a way for other applications to make changes to the data.

&nbsp;

##### There are a few key options for a REST API request:

- GET — The most common option, returns some data from the API based on the endpoint you visit and any parameters you provide
- POST — Creates a new record that gets appended to the database
- PUT — Looks for a record at the given URI you provide. If it exists, update the existing record. If not, create a new record
- DELETE — Deletes the record at the given URI
- PATCH — Update individual fields of a record

Typically, an API is a window into a database. The API backend handles querying the database and formatting the response. What you receive is a static response, usually in JSON format, of whatever resource you requested.

REST APIs are so commonplace in software development, it’s an essential skill for a developer to know how they work. APIs are how applications communicate with one another or even within themselves.

&nbsp;

##### A typical Django application that uses React as a front end. It needs an API to allow React to consume data from the database.

![image](https://user-images.githubusercontent.com/41619898/79838633-461d4580-83ee-11ea-9cfe-22f345764bdb.png)

&nbsp;

## Django startapp

### Redmine_Defects

- Implement real-time updates with DRF | Building Redmine API
  - http://project.lsware.co.kr/redmine/projects/omni-pis-qa/issues

![image](https://user-images.githubusercontent.com/41619898/78514741-d142ec80-77ed-11ea-87b9-fe2e8140bc95.png)

&nbsp;

### Redmine_TestSupport

- Implement real-time updates with DRF | Building Redmine API
  - http://project.lsware.co.kr/redmine/projects/olis/issues

&nbsp;

### Redmine_QualityInspection

- Implement real-time updates with DRF | Building Redmine API
  - http://project.lsware.co.kr/redmine/projects/test1/issues

&nbsp;

### Accounts / django-rest-knox

- Add Token-based Authentication with Django-rest-knox to an app built with Django and React/Redux

![image](https://user-images.githubusercontent.com/41619898/78620531-3b759300-78bb-11ea-8b02-60212d509d38.png)

| URL              | Detail                               |
| :--------------- | ------------------------------------ |
| api/auth/user    | Retrieve user information            |
| api/aut/register | Return token after user registration |
| api/auth/login   | User Login                           |
| api/auth/logout  | User Logout                          |

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
```

![image](https://user-images.githubusercontent.com/41619898/79927590-339d1d80-847b-11ea-8988-79c35b9ec019.png)






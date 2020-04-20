```powershell
> pip install virtualenv
> virtualenv venv		// virtualenv 'name'

> python -m pip install -r requirements.txt
```

-------

**GET**	/api/members

![image](https://user-images.githubusercontent.com/41619898/79725615-71d3f900-8324-11ea-8c29-376fb30aa0dd.png)



**POST**	/api/members/

```json
{
    "username": "kimmin",
    "email": "kimmin@example.com",
    "password": "1234"
}
```
# drf-auth Lab 33


> Runserver use `docker compose up` then go to `http://localhost:8000/api/v1/country/`

> Admin Panel use `http://localhost:8000/admin`

> Get access token `http://localhost:8000/api/token/` 

> refresh token `http://localhost:8000/api/token/refresh/`


> manually test using HTTP Client using postman

- get access token do the following:
- using POST request and provide the username and password inside the body
![image](assets/get_access_token.png)


- posting data using POST request and provide the access token inside the authorization box
![image](assets/provide_access.png)



- add data inside the body
![image](assets/test_postman_usingJWT.png)



- result after adding data 

![image](assets/result_adding_data_using_postman.png)


- update using PUT request 
![image](assets/update_using_postman.png)

- result after updating data 

![image](assets/reslut_after_updating.png)


- deleting data using DELETE request
![image](assets/delete_from_postman.png)

- result after deleting data

![image](assets/result_after_delete_from_postman.png)


> After Five minutes the access token will be expired. We need to refresh the token at `http://localhost:8000/api/token/refresh/`
- Do this in postman 
![image](assets/refresh_token.png)

### **NOTE!!**: **_The refresh token will be automatically expired in 24 hours from creation time_**
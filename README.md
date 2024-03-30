# Codemonk Backend Intern Assignment

👨‍💻 Codemonk Backend Intern Assignment  

For my Codemonk Backend Intern Assignment, I have developed a solution in both API and GUI formats. Additionally, I've included a complete step-by-step process to run the code.

[Click Here](#) For Video Solution Demonstration.

For my Codemonk Backend Intern Assignment, I have developed a solution in both API and GUI formats. Additionally, I've included a complete step-by-step process to run the code.

[RestFul API Solution](#restful-api-solution)  
[GUI Solution](#gui-solution)

## RestFul API Solution

1. Download the code and extract the ZIP folder of the backend solution.
2. Open the Backend solution in VS Code and run the following command to create the virtual environment:
   
   ```bash
   python -m venv env 
   ```
   
4. Activate the virtual environment:
   
   ```bash
   source env/bin/activate
   ```
   
6. Install Django and Django Rest Framework:
   
   ```bash
   pip install django
   pip install djangorestframework
   ```
   
8. Also, install PostgreSQL:
   
   ```bash
   pip install postgresql2
   ```
   
10. Open your PostgreSQL and change the database inputs according to your PostgreSQL information before running and migrating the code.
11. Navigate to the core directory and run the following commands for migrations:
    
   ```bash
   cd core 
   python manage.py makemigrations
   python manage.py migrate 
   ```

11. Create the superuser:
    
   ```bash
   python manage.py createsuperuser
   ```

11. Run the code using the following command:
    
   ```bash
   python manage.py runserver
   ```

11. For creating the authorization token, use the below command:
    
    ```bash
    python manage.py drf_token <email>
    ```
    
13. Copy the token and then open Postman and make a GET request with the URL:
    
    ```
    https://127.0.0.1/paragraph
    ```
    
15. We can't access the data initially. First, go to the header section, choose authorization as the key, and in the value section, write "Token <generated token>". Then we can access the data.
16. To add data, use the following URL and JSON data with a POST request:
    
    ```
    POST: https://127.0.0.1/paragraph
    ```
    
    ```json
    {
        "paragraph_name": "Codemonk",
        "paragraph_description": "Codemonk Gives me Assignment that for that",
        "user": 1
    }
    ```
    
18. Now the data is added. We can also search for a particular word using the below API URL:
    
    ```
    https://127.0.0.1/paragraph/?search=search_word_write_here
    ```
That is the complete step-by-step process to run the code. I hope it's understandable for you. Thank you.

## GUI Solution

1. For the GUI solution, simply extract the GUI solution folder and open VS Code.
2. Run the below command for the virtual environment:
   
   ```bash
   python -m venv env 
   ```
   
4. Then enter into the virtual environment:
   
   ```bash
   source env/bin/activate
   ```
   
6. Install Django:
   
   ```bash
   pip install django 
   ```
   
8. Change the database information to your PostgreSQL information and then install PostgreSQL:
   
   ```bash
   pip install postgresql2
   ```
   
10. Migrate the code using the following commands and create a superuser:
    
   ```bash
   python manage.py makemigrations
   python manage.py migrate 
   python manage.py createsuperuser
   ```

11. Then run the code using the below command:
    
   ```bash
   python manage.py runserver
   ```

Now the project is running successfully. I hope this also helps you for successfully run the code.

## Postman API Documentation

Authentication is required to access certain endpoints. To authenticate, obtain an authorization token by following the steps below:

1. Run the following command to create the authorization token:
   ```bash
   python manage.py drf_token <email>
   ```
2. Copy the generated token.

## Base URL

The base URL for all endpoints is `https://127.0.0.1/`.

## Endpoints

### Get All Paragraphs

- **URL**: `/paragraph`
- **Method**: `GET`
- **Authentication Required**: Yes
- **Headers**:
  - `Authorization`: `Token <generated token>`
- **Description**: Retrieves all paragraphs stored in the database.

### Search for Paragraphs

- **URL**: `/paragraph/?search=search_word_write_here`
- **Method**: `GET`
- **Authentication Required**: Yes
- **Headers**:
  - `Authorization`: `Token <generated token>`
- **Description**: Searches for paragraphs containing the specified search word.

### Add a Paragraph

- **URL**: `/paragraph`
- **Method**: `POST`
- **Authentication Required**: Yes
- **Headers**:
  - `Authorization`: `Token <generated token>`
- **Body**:
  ```json
  {
      "paragraph_name": "Codemonk",
      "paragraph_description": "Codemonk Backedn Intern Assignment.",
      "user": 1
  }
  ```
- **Description**: Added a new paragraph to the database.


## Error Handling

- The API returns appropriate error responses with corresponding status codes and error messages.

## Usage

Please ensure you have followed the steps for authentication before accessing the endpoints. You can use tools like Postman to interact with the API.

**Thank you for the opportunity.**

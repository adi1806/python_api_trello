# Automation Testing Framework

This repository contains  API automated tests using `pytest`

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- `pip` (Python package manager)
- pytest
- pytest-xdist  #pip install pytest-xdist ,  for parallel test execution
-pip install allure-pytest
-pytest-html
- Git >> https://github.com/adi1806/python_api_trello/

##Folder Structure 
# data 
      >testdata.ini >keeping all the data like (key,token,url..) This File fetch and update the data at run time 
      >poco.py >This class have all the method to insert and fetch the request and Reonse 
# report
      >using Allure report and this folder update the html report after completion of each run
      >under allure-result it store all the logs 
# tests
      >test_All_Api.py >> having all the test with post,get,put and delete method
      >in this file flow of testcase is that first i am creating trello board and checking if any exist board is present then first delete it and then Creating new board
      >Deleting the board first otherwise many boards will be created due to many run
      >Create board 
      >Create List under created board
      >created card under created list 
      >get the details of created card
      >Updte the created card
      >delete card> i am creating new card and deleting it 
      
# utils
      >apimethod urils> Define all the method against api method post put delete and get
      >parser utils> method to fetch data from testdata.ini file 
# pytest.ini
      >configuring allure report
      

### Running API Tests

    ```bash
    pytest  Python_API_Project/tests



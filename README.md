# Installation

Install python [python installation guide](https://www.python.org/downloads/)

Install selenium library [selenium installation files](https://pypi.org/project/selenium/): ```pip install selenium```

Add python path to enviroment variable

donwload browser drivers and put in python27 directory
[Guide for selenium installation](https://selenium-python.readthedocs.io/installation.html)

# Selenium_With_Python_Sample_Project
This is implementation of Selenium with python for sample project
Before executing test please install pytest module by command :pip install pytest

to execute tests give command: python -m pytest
to execute tests give command and get verbose results :py.test -v
once command given pytest will execute test having names starting with test from subordinate directory (ex. test_*.py)

## Skip/execute selective tests
### Skip test from execution

```
import pytest
@pytest.mark.skip(reason="I dont want to run test")
```

to see result with verbose and reason behind skip execute command: pytest -v -rxs

### Execute selective tests only
to execute selective tests only enter command: pytest -k <keyword>
It will execute all tests having <keyword> in test name
  
### Tag test cases 
add ```@pytest.mark.<tagName>``` code before test cases to tag
ex.
```
import pytest
@pytest.mark.<tagName>
def test_myTest1():
  print("my test")
```

### Execute tests of selected Tags only
enter below command to execute tests with given tag name
```pytest -m <tagName>```

### Exclude test of selective tags only
enter below command to execute tests not having tag as smoke
```
pytest -m "not smoke" -v
```

# Reporting Selenium Python
I have allure adapter to generate HTML reports. Please find steps to install and setup allure reproter in project:

__Step 1__.Install Allure adapter
```
pip install pytest-allure-adaptor
```

__Step 2__.download allure zip file in your system [donwload allure zip](https://bintray.com/qameta/generic/allure2/2.7.0#files/io%2Fqameta%2Fallure%2Fallure%2F2.7.0)

__Step 3__.extract downloaded zip file and add ```allure2.7.0/bin``` location to environment variable

__Step 4__.Verify pytest-allure-adapter is added in interpreter of pycharm

__Step 5__.create Report folder in project and run test case with below command
```
pytest --allure <path of report folder>
```

__Step 6__.After test is run xml files will be generated in reports folder. To create html report open command prompt and enter below command:
```
cd <path of report folder>
allure generate <path of report folder>
```
If you find any difficulty please refer [this youtube video](https://www.youtube.com/watch?v=gbEg0grSYSs)

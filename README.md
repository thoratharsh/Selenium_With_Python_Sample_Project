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
import pytest
@pytest.mark.<tagName>
def test_myTest1():
  print("my test")

### Execute tests of selected Tags only
enter below command to execute tests with given tag name
pytest -m <tagName>

### Exclude test of selective tags only
enter below command to execute tests not having tag as smoke
pytest -m "not smoke" -v

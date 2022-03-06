# Demo Playwright Project With Python and Behave
The project is created to demonstrate how to use Playwright with Python. 

This is not official tutorial - just for demo purposes.

## Links
- [Playwright - Python](https://playwright.dev/python/)
- [venv setup](https://docs.python.org/3/library/venv.html)

## How to run on local machine
1. Prepare  [virtual environment](https://docs.python.org/3/library/venv.html),
2. Install requirements.txt (_pip install -r requirements.txt_)
3. Setup playwright using command _playwright install_,
4. For running test use commands:
   - all tests: _python -m behave_
   - all test with raports: _python -m behave -f allure_behave.formatter:AllureFormatter -o res ./features_
5. Generate raports with command: _allure generate res --clean_.  


## Setup in IntelliJ IDEA:
Also, there is possibility to run single test using PyCharm or IntelliJ IDEA.
1. Open selected scenario,
2. Use double green arrow to run as behave scenario,
3. Go to Run/Debug Configuration and in **working directory** set path to **src** directory,


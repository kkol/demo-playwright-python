How to run: 

- python -m behave


How to run with reports:

- python -m behave -f allure_behave.formatter:AllureFormatter -o res ./features

- allure generate res --clean


Setup in inteliji:
- Edit configuration from test and add working directory <path_to_src>


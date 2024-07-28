# Selenium Framework with pytest and Allure

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:
    ```bash
    cd selenium_framework
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Update the configuration settings in `config.ini` as needed.

## Running Tests

To run the tests and generate reports:
```bash
pytest
```

To view the Allure report
```bash
allure serve allure_results
```

Generate the HTML report
```bash
pytest --html=report.html --self-contained-html
```

## Summary
- The framework reads data from an Excel sheet using `excel_utils.py`.
- Fetches the latest Chrome driver on runtime in `driver.py`.
- Configures the browser and headless mode using `config.py` and `config.ini`.
- Takes screenshots for each action using the `take_screenshot` function.
- Generates both pytest HTML and Allure reports.

With this setup, you have a complete framework for running Selenium tests using pytest and generating detailed reports with Allure.

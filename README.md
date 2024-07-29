# Simple and Best Selenium-Python Framework with Pytest and Allure Reporting

## Key Features:

- **Excel Data Integration:**
  - Seamlessly read data from Excel sheets using openpyxl.
  
- **Dynamic ChromeDriver Management:**
  - Automatically fetch and configure the latest ChromeDriver at runtime.

- **Action-Based Screenshot Capture:**
  - Capture screenshots for every action, ensuring comprehensive visual documentation.

- **Comprehensive Reporting:**
  - Generate detailed Pytest HTML reports.
  - Produce Allure reports with integrated screenshots for enhanced clarity and debugging.

- **Browser Selection:**
  - Feature to select the browser (Chrome or Firefox) from the config settings.

- **Headless Mode Execution:**
  - Execute tests in headless mode, configurable from the settings.

- **Data-Driven Framework:**
  - Test data is in Excel format.
  - Utilize pandas DataFrame to fetch and manipulate data from Excel.

## Demo Highlights:

1. **Launch Chrome Browser:**
   - Automatically start a new Chrome session.
   
2. **Navigate to Google:**
   - Open Google's homepage for search operations.
   
3. **Perform Search Query:**
   - Execute a search query, showcasing the framework's interaction capabilities.
   
4. **Validate Search Results:**
   - Ensure the search results are as expected, demonstrating validation steps.

5. **Close Browser:**
   - Properly close the browser to clean up the session.

## Benefits

- **Ease of Data Management:**
  - Effortlessly handle test data using Excel integration.

- **Up-to-Date Browser Testing:**
  - Always use the latest ChromeDriver, ensuring compatibility with the newest browser versions.

- **Enhanced Debugging:**
  - Visual documentation through screenshots for every step.

- **Detailed Analysis:**
  - Utilize comprehensive reports for in-depth test result analysis and tracking.

This framework is designed to streamline your test automation process, making it efficient, up-to-date, and easy to debug with rich reporting capabilities.

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/sagar-maru/Best-Selenium-Python-Framework.git
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
Command to Run Pytest and Generate Reports:
```bash
pytest --alluredir=result/allure-results --html=result/report.html --self-contained-html
```

To view the Allure report
```bash
allure serve allure_results
```

Generate the HTML report
```bash
pytest --html=report.html --self-contained-html
```

## Command to Generate Allure Report

After running the tests and generating the Allure results, you can generate the Allure report and place it in the result folder.
```bash
allure serve result/allure-results --output result/allure-report
```

Alternatively, if you want to generate the report without serving it:
```bash
allure generate result/allure-results --output result/allure-report
```

## Summary
- The framework reads data from an Excel sheet using `excel_utils.py`.
- Fetches the latest Chrome driver on runtime in `driver.py`.
- Configures the browser and headless mode using `config.py` and `config.ini`.
- Takes screenshots for each action using the `take_screenshot` function.
- Generates both pytest HTML and Allure reports.

With this setup, you have a complete framework for running Selenium tests using pytest and generating detailed reports with Allure.

import os
import subprocess

# Ensure the result directory exists
os.makedirs('result/allure-results', exist_ok=True)

# Run pytest and generate reports
subprocess.run([
    'pytest',
    '--alluredir=result/allure-results',
    '--html=result/report.html',
    '--self-contained-html'
])

# Generate Allure report
subprocess.run([
    'allure', 'generate',
    'result/allure-results',
    '--output', 'result/allure-report'
])

print("Reports have been generated in the 'result' directory.")

import os
import requests
import zipfile
import shutil
from pathlib import Path

CHROME_DRIVER_BASE_URL = "https://storage.googleapis.com/chrome-for-testing-public"


def get_latest_chrome_version():
    url = "https://googlechromelabs.github.io/chrome-for-testing/LATEST_RELEASE_STABLE"
    response = requests.get(url)
    response.raise_for_status()
    return response.text.strip()


def download_chrome_driver(version, download_path):
    platform = 'win64' if os.name == 'nt' else 'linux64' if os.name == 'posix' else 'mac64'
    download_url = f"{CHROME_DRIVER_BASE_URL}/{version}/{platform}/chromedriver-{platform}.zip"

    response = requests.get(download_url, stream=True)
    response.raise_for_status()

    zip_path = Path(download_path) / f"chromedriver-{platform}.zip"
    with open(zip_path, 'wb') as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return zip_path


def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    os.remove(zip_path)


def setup_chrome_driver():
    version = get_latest_chrome_version()
    project_root = Path(__file__).parent.parent.resolve()
    download_path = project_root / "drivers"

    if not download_path.exists():
        download_path.mkdir(parents=True, exist_ok=True)

    zip_path = download_chrome_driver(version, download_path)
    extract_zip(zip_path, download_path)

    platform = 'win64' if os.name == 'nt' else 'linux64' if os.name == 'posix' else 'mac64'
    chromedriver_path = os.path.join(os.path.join(download_path, f'chromedriver-{platform}'),'chromedriver.exe')

    return str(chromedriver_path)


# Example usage
if __name__ == "__main__":
    chromedriver_path = setup_chrome_driver()
    print(f"ChromeDriver is set up at: {chromedriver_path}")

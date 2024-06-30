# Selenium Python Add to Cart Framework

## Overview

This is a Selenium-based test automation framework written in Python. The framework is designed to automate the process of adding items to the cart on amazon website. It uses `pytest` for managing test cases .

## Features

- Cross-browser testing support (Chrome, Firefox, Edge)
- Detailed test reports with `allure-pytest`

## Installation

### Prerequisites

- Python 3.7 or above
- pip (Python package installer)

### Setup

1. **Clone the repository**:
    ```sh
    git clone https://github.com/Cleo95/SeleniumExercise.git
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Install the allure report for Windows**:
    ```sh
    scoop install allure
    ```

## Usage

### Running Tests

You can run the tests with different browsers by specifying the `--browser_name` option:

- **Chrome**:
    ```sh
    pytest --browser_name chrome
    ```

- **Firefox**:
    ```sh
    pytest --browser_name firefox
    ```

- **Edge**:
    ```sh
    pytest --browser_name edge
    ```

### Generating Allure Reports

To generate an allure report of the test results, use the `--alluredir` option:

```sh
pytest -s -v tests --browser_name chrome --alluredir reports/allure-results 

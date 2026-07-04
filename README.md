# E-Commerce Automation Framework (Selenium & Pytest)

This is a highly optimized test automation framework designed for end-to-end (E2E) validation of e-commerce platforms. Built using **Python**, **Selenium WebDriver**, and **Pytest**, this suite demonstrates modern automation best practices, including robust synchronization, parallel execution, and automated visual reporting tailored for enterprise delivery.

## 🚀 Key Framework Features

* **Optimized Architecture & Fixtures:** Structured utilizing scalable design patterns with a centralized `conftest.py` for seamless browser lifecycle management, clean dependency injection, and reusable test fixtures.
* **Parallel Test Execution:** Configured for high-speed parallel execution via `pytest-xdist`, drastically reducing CI/CD pipeline execution times.
* **Resilient DOM Synchronization:** Eliminated test flakiness in complex product cart interactions by transitioning from brittle sequential loops to dynamic XPath locators and conditional JavaScript-based clicks.
* **Headless & Headed Modes:** Built-in flexibility to execute tests seamlessly in headless mode (optimized for CI/CD pipelines) or headed mode (optimized for local debugging).
* **Rich HTML Reporting with Failure Screenshots:** Integrates automated HTML report generation that dynamically captures and attaches full-page screenshots directly to failed test logs for instant debugging.

## 📋 Prerequisites

Ensure you have the following installed locally:
* Python 3.8 or higher
* Google Chrome / Chromedriver (or your preferred browser driver matching your browser version)

## 🛠️ Installation & Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/emergabrillo/selenium-automation-with-pytest.git
    cd selenium-automation-with-pytest
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    # Windows
    python -m venv venv
    .\venv\Scripts\activate

    # macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    All required libraries are pinned and documented. Install them directly using:
    ```bash
    pip install -r requirements.txt
    ```

## 🧪 Running the Tests

The suite is designed to be highly configurable via command-line arguments, allowing you to seamlessly toggle UI visibility and choose how reports are structured.

### 1. Execution Modes (Headed vs. Headless)

* **Headed Mode (Default / Local Debugging):** Launches the visible browser window so you can visually inspect interactions, animations, and elements while developing tests.
    ```bash
    pytest
    ```
* **Headless Mode (CI/CD Pipelines / Performance):** Executes tests without opening a graphical user interface (GUI). This drastically saves system memory, prevents display server errors on remote runners, and accelerates pipeline speeds.
    ```bash
    pytest --headless
    ```

### 2. HTML Report Generation

This framework leverages `pytest-html` to capture system metrics, logs, and failure screenshots. You can generate reports in two distinct ways:

* **Option A: Self-Contained HTML Report (Recommended for sharing)**
    This compiles the HTML, CSS styles, images, and base64 failure screenshots into a single, monolithic `.html` file. It is incredibly convenient to attach to emails, slack messages, or upload directly to build artifacts because it requires zero external dependencies.
    ```bash
    pytest --html=reports/report.html --self-contained-html
    ```
* **Option B: Standard HTML Report (Separate Assets)**
    This generates a lean HTML file alongside a distinct directory containing external CSS styles, assets, and raw image files. This is preferred if you need to compress, host, or parse test screenshots independently from the main document.
    ```bash
    pytest --html=reports/report.html
    ```

### 3. Combining Advanced Options (Example)
To run your test suite at maximum speed in parallel across 3 CPU workers, entirely headlessly, and generate a self-contained report:
```bash
pytest -n 3 --headless --html=reports/report.html --self-contained-html
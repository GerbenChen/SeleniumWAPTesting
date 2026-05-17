# Twitch WAP Automation Framework (Selenium Version)

Mobile Web Automation Testing Framework for Twitch H5 using **Selenium + Pytest**.

---

# Overview

This project is a scalable and maintainable mobile web automation framework designed for Twitch WAP (H5) testing. It utilizes Selenium's Chrome Mobile Emulation to simulate real-world mobile browser behavior and implements advanced techniques to bypass bot detection.

The framework follows enterprise-level automation architecture practices including:

- **Page Object Model (POM)**
- **Config-Driven Framework**
- **Mobile Device Emulation** (via Chrome DevTools Protocol)
- **Stealth Mode** (Bypassing `navigator.webdriver` detection)
- **Centralized Artifact Management**
- **Structured Logging**
- **CI/CD Integration** (GitHub Actions)
- **Automatic Screenshotting** (Captures every test outcome: Passed/Failed)

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python 3.12+ | Programming Language |
| Pytest | Test Runner |
| Selenium 4.x | Browser Automation |
| Webdriver Manager | Automated Driver Management |
| JSON | Configuration Management |
| GitHub Actions | CI/CD |
| Chrome Mobile Emulator | Mobile Device Simulation |

---

# Features

## 📱 Automation Features
- **Mobile Emulation**: High-fidelity simulation using Chrome's `mobileEmulation` with custom device metrics and touch events.
- **Robust Locators**: Adaptive XPath and CSS strategies to handle Twitch's dynamic React rendering and multi-language UI (EN/ZH).
- **Stealth Execution**: Injected JavaScript to spoof `platform`, `maxTouchPoints`, and hide automation flags to bypass Twitch's anti-bot headers.
- **Smart Pop-up Handling**: Automatically identifies and dismisses consent banners and "Open App" overlays.

## 🔍 Debugging Features
- **Universal Screenshots**: Automatically captures the final state of every test case in the `screenshots/` directory.
- **Outcome Prefixing**: Files are named `PASSED_`, `FAILED_`, or `INTERRUPTED_` for instant identification.
- **Rich Logging**: Integrated logger providing step-by-step execution details and error stack traces.

## 🚀 CI/CD Features
- **GitHub Actions Ready**: Pre-configured for headless execution on `macos-latest` or `ubuntu-latest`.
- **Artifact Preservation**: Automatically uploads execution screenshots and JUnit XML reports to the GitHub Actions run.

---

# Project Structure

```text
project/
├── config/
│   └── config.json           # Environment & Browser settings
├── pages/
│   ├── base_page.py          # Selenium wrappers (wait, click, js_click)
│   ├── home_page.py          # Mobile landing page & Search navigation
│   ├── search_page.py        # Search results & Scroll logic
│   └── streamer_page.py      # Streamer profile & Video validation
├── screenshots/              # Auto-generated screenshots (PASSED/FAILED)
├── tests/
│   ├── conftest.py           # Driver initialization & Stealth scripts
│   └── test_twitch_flow.py   # Main test suites
├── utils/
│   ├── artifact_manager.py   # Screenshot & Log path management
│   ├── config_reader.py      # JSON Config loader
│   └── logger.py             # Formatted execution logs
├── .github/
│   └── workflows/
│       └── main.yml          # CI/CD Pipeline configuration
├── requirements.txt
├── pytest.ini
└── README.md

```

---

# Installation

## 1. Create Virtual Environment

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configuration

## config/config.yaml

```yaml
base_url: "https://m.twitch.tv"

browser:
  headless: false
  mobile_emulator: "iPhone 12 Pro"

timeout: 10
```

---

# Run Tests

## Run All Tests

```bash
pytest
```

---

## Run Specific Test

```bash
pytest tests/test_twitch_streamer_flow.py
```

#### Demo
![Demo Animation](./assets/demo.gif)
---

---

# Artifact Management

The framework automatically manages test output:

- Screenshots: Saved in /screenshots/ with format {OUTCOME}_{TEST_NAME}.png.

- Logs: Detailed execution history provided via standard output and formatted logs.

---

# GitHub Actions CI/CD

Automation tests run automatically on every push.

### Key CI Capabilities:

- Environment Support: Optimally configured for macOS/Ubuntu runners.
- Chrome Sandbox: Pre-configured with `--no-sandbox` for stable CI execution.
- Artifact Upload: Access all execution screenshots directly from the "Actions" tab.

---

# Example GitHub Actions Workflow
```yaml
name: Selenium Twitch WAP Testing

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]

jobs:
  test:
    runs-on: macos-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Set up Chrome
        uses: browser-actions/setup-chrome@v1
        with:
          chrome-version: stable

      - name: Run Pytest
        env:
          HEADLESS: "true"
        run: |
          mkdir -p reports screenshots
          pytest --junitxml=reports/result.xml

      - name: Upload All Screenshots
        if: always() 
        uses: actions/upload-artifact@v4
        with:
          name: all-test-screenshots
          path: screenshots/
          retention-days: 7

      - name: Upload Test Report
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: pytest-report
          path: reports/
```

---

# Current Framework Capabilities

| Capability | Status |
|---|---|
| Mobile Emulator | YES |
| Stealth Mode (Bot Bypass) |  YES |
| Multi-language Adaptability |  YES |
| POM Architecture |  YES |
| Screenshot All States |  YES |
| Structured Logging |  YES |
| GitHub Actions |  YES |
| CI/CD Ready |  YES |
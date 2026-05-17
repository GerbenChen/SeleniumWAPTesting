# Twitch WAP Automation Framework

Mobile Web Automation Testing Framework for Twitch H5 using Playwright + Pytest.

---

# Overview

This project is a scalable and maintainable mobile web automation framework designed for Twitch WAP (H5) testing.

The framework follows enterprise-level automation architecture practices including:

- Page Object Model (POM)
- Config-Driven Framework
- Centralized Artifact Management
- Structured Logging
- CI/CD Integration
- Screenshot on Failure
- Trace Viewer Integration
- Video Recording
- Mobile Emulator Testing

---

# Tech Stack

| Technology | Usage |
|---|---|
| Python 3.11+ | Programming Language |
| Pytest | Test Runner |
| Playwright | Browser Automation |
| Pytest HTML | HTML Report |
| YAML | Configuration Management |
| GitHub Actions | CI/CD |
| Google Chrome | Real Browser Testing |
| Chrome Mobile Emulator | Mobile Device Simulation |

---

# Features

## Automation Features

- Mobile Web Testing
- iPhone 12 Pro Emulator
- Real Google Chrome Testing
- Config-Driven Framework
- Page Object Model (POM)
- Retry Failed Tests
- Robust Locator Strategy

---

## Debugging Features

- Screenshot on Failure
- Trace Viewer on Failure
- Video Recording
- Console Logging
- Artifact Management
- Timestamp-based Reports

---

## CI/CD Features

- GitHub Actions Integration
- HTML Report Upload
- Trace Artifact Upload
- Video Artifact Upload
- Screenshot Artifact Upload
- CI-Friendly Structure

---

# Project Structure

```text
project/

├── config/
│   └── config.yaml
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   ├── search_page.py
│   └── streamer_page.py
│
├── reports/
│   ├── html/
│   ├── logs/
│   ├── screenshots/
│   ├── traces/
│   └── videos/
│
├── tests/
│   ├── conftest.py
│   └── test_twitch_streamer_flow.py
│
├── utils/
│   ├── artifact_manager.py
│   ├── config_reader.py
│   └── logger.py
│
├── .github/
│   └── workflows/
│       └── test.yml
│
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

## 3. Install Google Chrome for Playwright

This project uses the real Google Chrome browser.

Install Chrome browser for Playwright:

```bash
playwright install chrome
```

---

## Optional: Install All Playwright Browsers

```bash
playwright install
```

---

# Configuration

## config/config.yaml

```yaml
base_url: "https://m.twitch.tv"

search_name: "StarCraft II"

browser:
  headless: false
  device: "iPhone 12 Pro"
  channel: "chrome"

debug:
  video: true
  trace: true

timeout: 30000
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

## Run Smoke Tests

```bash
pytest -m smoke
```

---

# Generate HTML Report

```bash
pytest \
--html=reports/html/report.html \
--self-contained-html
```

---

# Playwright Trace Viewer

Trace files are generated only when tests fail.

## Open Trace Viewer

```bash
playwright show-trace reports/traces/<date>/<trace_file>.zip
```

Example:

```bash
playwright show-trace reports/traces/test_twitch_streamer_flow.zip
```

---

# Video Recording For Demo

Video recording can be enabled or disabled in:

```yaml
debug:
  video: true
```

Generated videos location:

```text
reports/videos/
```

---

# Screenshot on Failure

Screenshots are automatically captured when test cases fail.

Generated screenshots location:

```text
reports/screenshots/
```

---

# Logging

Execution logs are automatically generated.

Generated logs location:

```text
reports/logs/
```

Example log format:

```text
2026-05-16 12:02:46,184 | INFO | Starting Test: test_twitch_streamer_flow
2026-05-16 12:02:46,184 | INFO | Browser Channel: chrome
2026-05-16 12:02:46,184 | INFO | Headless Mode: False
2026-05-16 12:02:46,184 | INFO | Device: iPhone 12 Pro
2026-05-16 12:02:50,934 | INFO | Video Recording Enabled
2026-05-16 12:02:50,958 | INFO | Trace Recording Started
2026-05-16 12:03:25,482 | INFO | Test Failed: False
2026-05-16 12:03:25,488 | INFO | Trace Discarded (Test Passed)
2026-05-16 12:03:25,553 | INFO | Video Saved: /Users/gerbenc/Desktop/WAPTesting/reports/videos/ece5d99f3483225dcc6b54f5d34e20f0.webm
2026-05-16 12:03:25,700 | INFO | Finished Test: test_twitch_streamer_flow
```

---

# Artifact Management

The framework includes a centralized artifact manager.

Supported artifacts:

- Screenshots
- Trace Files
- Videos
- Logs
- HTML Reports

Features:

- Safe filename handling
- CI-friendly structure

---

# GitHub Actions CI/CD

Automation tests automatically run on:

- Push
- Pull Request
- Manual Workflow Dispatch

---

# GitHub Actions Features

- Python Environment Setup
- Google Chrome Installation
- Playwright Chrome Installation
- Mobile Emulator Execution
- HTML Report Upload
- Trace Upload
- Video Upload
- Screenshot Upload

---

# Example GitHub Actions Workflow

```yaml
name: Playwright Twitch WAP Test

on:

  push:
    branches:
      - main

  pull_request:
    branches:
      - main

jobs:

  test:

    runs-on: ubuntu-latest

    steps:

      - name: Checkout Repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install Google Chrome
        uses: browser-actions/setup-chrome@v1

      - name: Install Dependencies
        run: |
          pip install -r requirements.txt

      - name: Install Playwright Chrome
        run: |
          playwright install chrome

      - name: Run Tests
        run: |
          pytest \
          --html=reports/html/report.html \
          --self-contained-html

      - name: Upload Reports
        uses: actions/upload-artifact@v4
        with:
          name: reports
          path: reports/
```

---

# Current Framework Capabilities

| Capability | Status |
|---|---|
| Mobile Emulator | YES |
| Real Chrome Testing | YES |
| Playwright | YES |
| POM Architecture | YES |
| Trace Viewer | YES |
| Video Recording | YES |
| Screenshot on Failure | YES |
| Structured Logging | YES |
| HTML Report | YES |
| Retry Mechanism | YES |
| GitHub Actions | YES |
| CI/CD Ready | YES |

---

# Future Improvements

- Parallel Execution
- Docker Integration
- Browser Matrix Testing
- Allure Reporting
- Slack Notifications
- API + UI Hybrid Testing
- Multi-Environment Support
- Database Validation
- Visual Regression Testing

---
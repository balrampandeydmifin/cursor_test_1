# Python Installation Guide

This guide explains how to install Python on your machine.

## Prerequisites

- None (Python is cross-platform)

## 1) Download Python

Visit the official Python website: [python.org](https://www.python.org/)

Download the latest stable version for your operating system (Windows, macOS, or Linux).

## 2) Install Python

Run the installer you downloaded and follow the installation wizard.

**Important:** On Windows, make sure to check "Add Python to PATH" during installation.

On macOS and Linux, Python may already be installed. Check with:

```bash
python --version
```

or

```bash
python3 --version
```

## 3) Verify Installation

Open a terminal/command prompt and run:

```bash
python --version
```

or on some systems:

```bash
python3 --version
```

You should see the version number displayed.

## 4) Optional: Set Up Virtual Environment

It's recommended to use virtual environments for Python projects.

Create a virtual environment:

```bash
python -m venv myenv
```

Activate it:

- On Windows: `myenv\Scripts\activate`
- On macOS/Linux: `source myenv/bin/activate`

## 5) Install Packages (if needed)

If your project has a `requirements.txt` file, install dependencies:

```bash
pip install -r requirements.txt
```

## Troubleshooting

- If `python` command not found, try `python3`
- On Windows, ensure Python is added to PATH
- For more help, visit [python.org](https://www.python.org/)

## Troubleshooting

- If port 3000 is busy, React may suggest another port automatically.
- If dependencies fail to install, delete `node_modules` and `package-lock.json`, then run:

```bash
npm install
```

## Optional: Create App with TypeScript

```bash
npx create-react-app my-react-app --template typescript
```


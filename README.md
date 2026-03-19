# Printanan CLI API Client

Created by: Angelo M. Mahusay BSIT - 3A

A simple, local command-line interface and FastAPI backend for managing print orders (Printanan API).

## Overview

This project contains two main components:

1. **Backend Server** (`main.py`): A FastAPI application that provides RESTful endpoints to create, view, and update print orders.
2. **CLI Client** (`client.py`): A Python command-line tool that interacts with the backend to submit orders and perform other operations.

## Prerequisites

- Python 3.7 or higher installed on your system.

## Installation Guide

Follow these step-by-step instructions to set up the project on your local machine.

### 1. Set up a Virtual Environment (Optional but Recommended)

It is good practice to use a virtual environment to manage dependencies:

```bash
# Create the virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # On macOS/Linux
# venv\Scripts\activate   # On Windows
```

### 2. Install Required Packages

The project relies on `fastapi`, `uvicorn` (for the server), and `requests` (for the CLI client). Install them using pip:

```bash
pip install fastapi uvicorn requests
```

## Running the Application

### 1. Start the Backend Server

Before running any CLI commands, make sure your FastAPI backend is running in a separate terminal window:

```bash
uvicorn main:app --reload
```

The server will start running locally at `http://127.0.0.1:8000`.

### 2. Use the CLI Client

Open a new terminal window (activate your virtual environment if you used one) and run the client script to interact with the API.

To see the help menu (if implemented) or run a command:

```bash
python client.py
```

### Example Usage: Creating an Order

To create a new print order, use the `order` command followed by the client's name, print type (`black_and_white`, `colored`, `photo_paper`), number of pages, and optional notes.

```bash
# syntax: python client.py order <client_name> <print_type> <num_pages> [notes]
python client.py order John colored 5 "please print ASAP"
```

This will send a POST request to your local FastAPI server and confirm that the order has been created.

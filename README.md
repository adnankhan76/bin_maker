
![BIN Generator Logo](https://raw.githubusercontent.com/adnankhan76/bin_maker/main/logo.png)
# BIN Information Generator

This Python script generates BIN (Bank Identification Number) information by making requests to a BIN API. It allows you to specify the type (Visa or Mastercard) and the quantity of BINs to generate. The generated data is saved to a file with the current date and time.

## Features

- Generates BIN information based on user input (type and quantity).
- Makes API requests to retrieve additional information about the generated BINs ues  paid api for firee.
- Saves BIN information to a file with a timestamp in the filename.
- Colorful console output using the colorama library.

Certainly! You can provide specific instructions for installing the necessary dependencies on Windows, Linux, and Termux. Here's an example:

### Install

#### Windows

1. Install Python:
   - Download Python from the [official website](https://www.python.org/downloads/).
   - During installation, make sure to check the box that says "Add Python to PATH."

2. Open Command Prompt and navigate to the project directory:

   ```bash
   cd bin_maker
   ```

3. Install required libraries:

   ```bash
   pip install colorama requests
   ```
   ##### bin_maker.exe
   ###### SOON!

#### Linux

1. Install Python:

   ```bash
   sudo apt-get update
   sudo apt-get install python3
   ```

2. download  git
   ``` bash
      git clone https://github.com/adnankhan76/bin_maker.git
   ```

4. Open a terminal and navigate to the project directory:

   ```bash
   cd bin_maker
   ```

5. Install required libraries:

   ```bash
   pip3 install colorama requests
   ```

#### Termux

1. Install Termux from the [Google Play Store](https://play.google.com/store/apps/details?id=com.termux).

2. Open Termux and install Python:

   ```bash
   pkg update
   pkg upgrade
   pkg install python
   ```

2. download  git
   ``` bash
      git clone https://github.com/adnankhan76/bin_maker.git
   ```

3. Navigate to the project directory:
   

   ```bash
   cd bin_maker
   ```

4. Install required libraries:

   ```bash
   pip install colorama requests
   ```



Adjust the instructions based on your actual project structure and requirements.
## Prerequisites

- Python 3.x
- Install required libraries: `colorama`, `requests`

```bash
pip install colorama requests
'''

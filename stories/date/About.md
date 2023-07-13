# About

## Project Description

This directory `stories/date` contains scripts for processing and testing data files related to stories and their associated dates. The main goal of this project is to implement a pipeline process to transform the original 'pages' format data into a date format.

## File Structure

* **scripts**: This folder contains scripts for processing the data. The scripts include:
    * `autobiographies.py` - Processes the Autobiographies data and renders it into a date format.
    * `daybooks.py` - Processes the Daybooks data and renders it into a date format.
    * `journals.py` - Processes the Journals data and renders it into a date format.

* **test**: This folder contains the unit tests for the scripts in the `scripts` directory. The test files include:
    * `TestAuto.py` - Tests for `autobiographies.py`.
    * `TestDayBooks.py` - Tests for `daybooks.py`.
    * `TestJournal.py` - Tests for `journals.py`.

* **data**: This folder contains the processed data output from the scripts in the `scripts` directory, with the information now represented in a date format.

* `requirements.txt`: This file contains the Python dependencies required for this project.

## Instructions

To run the scripts, ensure that you have installed the necessary Python dependencies from `requirements.txt`. You can install these using pip:

```sh
pip install -r requirements.txt
```

Then, you can run the scripts as follows:

```sh
python scripts/autobiographies.py
python scripts/daybooks.py
python scripts/journals.py
```

You can run the tests as follows:

```sh
python -m unittest test/TestAuto.py
python -m unittest test/TestDayBooks.py
python -m unittest test/TestJournal.py

```

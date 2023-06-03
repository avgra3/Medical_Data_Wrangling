# Medical Data Wrangling

![Pytest](https://github.com/avgra3/Medical_Data_Wrangling/actions/workflows/python-package-conda.yml/badge.svg?event=push)

The goal of this project is to automate the loading of data into a MariaDB database with data validation.

## Setup

### Prepare Environment variables

Rename [EXAMPLE.env](.\DataWrangling\EXAMPLE.env) to [.env](.\DataWrangling\EXAMPLE.env) and update the data path with the path to your data as a string. Then, update the data types with a dictionary with the column names as keys and data types for values of the dictionary. Follow the example as below:

```env
DATA_PATH = './path/to/file'
DATA_TYPES = '{"column_name_1": dataType_1, "column_name_2": dataType_2}'
```

### Anaconda/Miniconda

#### Windows

From the command line or powershell, with Anaconda and [Chocolatey](https://chocolatey.org/install) installed, run the below

```powershell
choco install mariadb
conda env update --file environment.yml --name data_loading
conda activate data_loading
```

**Note** If you need to install Anaconda and already have Chocolatey installed, you can install miniconda by running:

```powershell
choco install anaconda3
```

#### Linux

##### Ubuntu

From your terminal run the below:

```bash
sudo apt-get install mariadb-server
```

Then, with Anaconda/Miniconda installed, run the below.

```bash
conda env update --file environment.yml --name data_loading
conda activate data_loading
```

##### Fedora

Run the below command, then follow the rest of the Ubuntu setup.

```bash
sudo dnf install mariadb-server
```

### Pip Method

You will need to verify that all packages are useable on your machine and installable using pip. Also, it is reccomendded that you use a virtual environment such as pyenv. As with the Anaconda/Miniconda method, make sure to have MariaDB C connector available on your machine.

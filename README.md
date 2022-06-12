# PCF
### A python notebook based program to keep track of your personal cashflows and predict your future savings!
PCF generates the total amount of cash at a certain time in the future, depending on your current cashflows.
The chart is interactive, with the ability to examine certain parts of your income/expenses structure to identify weakpoints in your personal finances and provide a framework of optimization for future incomes/expenses. 

Take a look:
![Example of a spreadsheet being used as input][examplesheet]
![Example of analysing sources of income and expenses in PCF][exampleuse]

## How to use PCF
PCF is a robust system where a user generates a hierarchy using two google sheets. The software then extrapolates the information and produces a simulation of the
users expected cashflows depending on the date range they selected. To setup and use PCF requires three general steps:

1. Creation of a Payment Hierarchy in google sheets
2. Define incomes/expenses, payment type, and range; also in google sheets. 
3. Validate the Payment Hierarchy.
4. Select the date-time of choice and determine the timeskip (min. 1 day)
5. Authenticate your account and authorize PCF to access your Google Sheet
6. Run the simulation and explore what your financial future holds in store!

To understand how to effectively use PCF, knowledge of how the library is structured is required. 
### How PCF Works
PCF requires two seperate google sheets to interact correctly:

![Showing the two tabs of google sheets, located bottom right corner of the GUI][sheets]


The sheets generate a hierarchy pictured here:

![example of the command CF.hierachy()][hierarchy]

With the occurrence of each payment being displayed next to the name. The hierarchy can be thought of as a rudimentary file system, with only the files at the 
very bottom (or leafs, in Computer Science terms) containing actual data. Selecting any of theses groups will show up as the collective sum of all its contents over time in the generated graph (see the examples at the beginning of the PCF). 

PCF uses the *epoch* as a starting date for the simulation (day 0). The current amount of cash in *savings* should be the current total as of the *epoch*. 

## Setting up PCF
*Moving foreward, any **ITALICIZED** variables should be copied exactly, or PCF WILL NOT RUN*. 
Initialize a new google sheet with your target account, and create the following sheets:

![Showing the two tabs of google sheets, located bottom right corner of the GUI][sheets]

The sheet labelled *IndexTree* should be formatted as follows:

![Empty IndexTree sheet][emptyindextree]

All top-level files must be parented by total. **Having disconnected nodes will cause PCF to fail**.
See the examples at the start of this README to see an example of a valid *IndexTree* sheet.

The sheet labelled *InputNodes* should be formatted as follows:

![Empty InputNodes sheet][emptyinputnodes]

All sections **MUST** have a parent. **Inputs without parents will cause PCF to ignore your calculations in the cumulative total**.
See the examples at the start of this README to see and example of a valid *InputNodes* sheet. 

All InputNodes have:
1. name
2. value
3. occurrence
4. startdate
5. enddate
6. parent
> Note that all inputs in PCF are **case-sensitive** and CANNOT contain spaces. 

The only mandatory variables are *savings* and *epoch*. The *startdate* and *enddate* variables should be the same date, and all 4 values should be the same date.
Reference the example formatting above. 
> All dates in PCF follow the following format
> MM:DD:YYYY = MMDDYYY

**NO entries should have dates BEFORE the epoch. PCF WILL THROW AN ERROR.**

PCF **ONLY** supports the following *occurrence* inputs:
- *once* -> one-time payment
- *daily* -> payment occurs everyday
- *weekly* -> payment occurs every 7 days
- *bi-weekly* -> payment occurs every 14 days
- *monthly* -> payment occurs every month on the day in *startdate* (eg.startdate = 01252022 -> 25), unless the number is >28 and the number falls out of range. In which case it becomes the last day of the current month.

### Authenticating with google sheets
After the the sheets have been setup, upload the PCF.ipynb to Collab and run the following block:

```python3
# authenticator
from google.colab import auth
auth.authenticate_user()

import gspread
from google.auth import default
creds, _ = default()

gc = gspread.authorize(creds)
```
A popup will direct you to login to the google account used to create the google sheet. After logged in, run the following block:

## Running your first simulation
```python3
gsheet = 'INSERT YOUR LINK TO THE GOOGLE SHEET HERE'
CF = CashFlow(gc, gsheet)
```
This will initialize the CashFlow object and allow you to run the simulation. The following commands are available to users:
1. ```CF.hierarchy()``` | Prints out the hierarchy extracted from the google sheet
2. ```CF.visualize_range(sections:list[str], startdate:str, enddate:str, timeskip:int)``` | Runs the simulation and generates the plot

> Note that PCF requires the following libraries:
> 1. pandas (TODO: version)
> 2. ploty.express (TODO: version)

For examples with further documentation, reference the docstring under each function. 
PCF uses ploty as the interactive graph of choice. Reference the ploty documentation for further use. 

### Disclaimer:
PCF (Personal CashFlow) is hosted in Google Collab and interfaces with Google Sheets to setup your incomes. Note that this software was intended solely for Google Collab, mileage on hosting locally or on other cloud-based notebook software is untested. 

[emptyindextree]: Media/emptyindextree.PNG
[emptyinputnodes]: Media/emptyinputnodes.PNG
[hierarchy]: Media/Hierarchy.PNG
[sheets]: Media/Sheets.PNG
[exampletree]: Media/IndexTree.PNG
[exampleuse]: Media/ExampleUse.gif
[examplesheet]: Media/InputNodes.PNG

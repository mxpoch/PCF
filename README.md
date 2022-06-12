# PCF
### A python notebook based program to keep track of your personal cashflows and predict your future savings!

Take a look:
![Example of a spreadsheet being used as input][examplesheet] ![Example of the inputree][exampletree] 
![Example of analysing sources of income and expenses in PCF][exampleuse]

## How to use PCF
PCF is a robust system where a user generates a hierarchy using two google sheets. The software then extrapolates the information and produces a simulation of the
users expected cashflows depending on the date range they selected. To setup and use PCF requires three general steps:

1. Creation of a Payment Hierarchy in google sheets
2. Define incomes/expenses, payment type, and range; also in google sheets. 
3. Validate the Payment Hierarchy.
4. Select the date-time of choice and determine the timeskip (min. 1 day)
5. Run the simulation and explore what your financial future holds in store!

To understand how to effectively use PCF, knowledge of how the library is structured is required. 
### How PCF Works
PCF requires two seperate google sheets:
![Showing the two tabs of google sheets, located bottom right corner of the GUI][sheets]
to interact correctly. *Moving foreward, any ITALICIZED variables should be copied exactly, or PCF WILL NOT RUN*.

### Disclaimer:
PCF (Personal CashFlow) is hosted in Google Collab and interfaces with Google Sheets to setup your incomes. Note that this software was intended solely for Google Collab, mileage on hosting locally or on other cloud-based notebook software is untested. 

[sheets]: 
[exampletree]: Media/IndexTree.PNG
[exampleuse]: Media/ExampleUse.gif
[examplesheet]: Media/InputNodes.PNG

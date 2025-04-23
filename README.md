# Health and Economic Indicators Analysis

This Jupyter Notebook is designed to gather and process data from multiple sources pertaining to health and 
economic indicators across U.S. states covering multiple years. The focus of this analysis is to find a 
correlation between rates of **diabetes/obesity** and **economic security** if it does exist, and to create
state health projections based on current trends

## Data Sources

### 1. **Diabetes Rates (2000-2022)**

Data obtained from [CDC Diabetes Atlas](https://gis.cdc.gov/grasp/diabetes/diabetesatlas-surveillance.html), 
representing the rates of diabetes per state from 2000 - 2022. These datasets can be found in the sub-directory 
`Diabetes_Rates` located in csv_files in the project root directory (`Diabetes_Project`).

### 2. **US Food Security Data (2019-2023)**

Data collected from [U.S. Census Bureau]
(https://www.census.gov/data/datasets/time-series/demo/cps/cps-supp_cps-repwgt/cps-food-security.html), 
representing data collected by the Census Bureau regarding employment, housing, and food security. These datasets and 
their corresponding documentation can be found in the sub-directory `Food_Security` located in csv_files in the 
project root directory (`Diabetes_Project`).

### 3. **Obesity Rates by State (2011-2022)**

Data collected from [TFAH Obesity Rates]
(https://www.tfah.org/wp-content/uploads/2023/09/BRFSS_adult_obesity_data_state2011_2022.pdf), 
representing the rates of obesity by state from 2011 - 2022. Data collected as text/table and converted into a more 
usable `.csv` format. `Obesity_Percent_by_State.csv` can be found in csv_files in the project root directory.

### 4. **Poverty Rates by State (2002-2010), (2015), (2019-2021)**

Data collected from [Self Poverty Rates](https://www.self.inc/info/poverty-rates-in-each-state/),
https://www.infoplease.com/business/poverty-income/percent-people-poverty-state-2002-2010, and
https://www.epi.org/blog/poverty-rates-decrease-states-2015/.  The data represents the 
rates of poverty by state from 2002 - 2010, 2015, and 2019 - 2021. Data collected as 
text/table and converted into a more usable `.csv` format. `Poverty_Percent_by_State.csv` 
can be found in csv_files in the project root directory.  Additional data collected from 
https://www.infoplease.com/business/poverty-income/percent-people-poverty-state-2002-2010

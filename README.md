# Moon Mineral Units Calculation

## Description

This program calculates the number of mineral units available based on the moon's utilization rate and the proportion of four different minerals. The user can input a CSV file containing the relevant data, and the program will output a new CSV file with the calculated monthly results.

### The main steps involved:
1. **Calculate mineral units per moon** based on the moon's utilization rate and the proportions of the minerals.
2. **Calculate the monthly units** for each mineral type.
3. **Validate input data** to ensure it is in the correct format and handle errors appropriately.
4. **Generate a result CSV file** containing the calculated monthly units for each mineral.

---

## Functions

### `calculate_units(moon_utilization_rate_percent, mineral1_proportion, mineral2_proportion, mineral3_proportion, mineral4_proportion)`
Calculates the number of mineral units of each type based on the moon's utilization rate and mineral proportions.

#### Parameters:
- `moon_utilization_rate_percent`: The percentage of the moon's utilization rate (float).
- `mineral1_proportion`: The proportion of mineral #1 (float).
- `mineral2_proportion`: The proportion of mineral #2 (float).
- `mineral3_proportion`: The proportion of mineral #3 (float).
- `mineral4_proportion`: The proportion of mineral #4 (float).

#### Returns:
- A dictionary with the calculated units for each mineral type: 
  - "Mineral #1"
  - "Mineral #2"
  - "Mineral #3"
  - "Mineral #4"

---

### `calculate_monthly_units(moon_utilization_rate_percent, mineral1_proportion, mineral2_proportion, mineral3_proportion, mineral4_proportion)`
Calculates the monthly units for each mineral type based on the moon's utilization rate and mineral proportions.

#### Parameters:
- `moon_utilization_rate_percent`: The percentage of the moon's utilization rate (float).
- `mineral1_proportion`: The proportion of mineral #1 (float).
- `mineral2_proportion`: The proportion of mineral #2 (float).
- `mineral3_proportion`: The proportion of mineral #3 (float).
- `mineral4_proportion`: The proportion of mineral #4 (float).

#### Returns:
- A dictionary with the monthly units for each mineral type: 
  - "Mineral #1"
  - "Mineral #2"
  - "Mineral #3"
  - "Mineral #4"

---

### `validate_input(value, allow_zero=False, integer=False)`
Validates and converts input values. If the value is invalid (missing, non-numeric, or out of bounds), an error is raised.

#### Parameters:
- `value`: The value to be validated.
- `allow_zero`: If `True`, the value `0` is considered valid (default is `False`).
- `integer`: If `True`, the value is expected to be an integer (default is `False`).

#### Returns:
- The validated and converted value (float or integer).

#### Raises:
- `ValueError` if the input value is invalid.

---

## Usage

1. Prepare a CSV file with the following columns:
   - **System**: The system name (string).
   - **Planet**: The planet number (integer).
   - **Moon**: The moon number (integer).
   - **Utilization Rate**: The moon's utilization rate (float).
   - **Mineral Name1**: The name of mineral #1 (string).
   - **Mineral Proportion1**: The proportion of mineral #1 (float).
   - **Mineral Name2**: The name of mineral #2 (string).
   - **Mineral Proportion2**: The proportion of mineral #2 (float).
   - **Mineral Name3**: The name of mineral #3 (string).
   - **Mineral Proportion3**: The proportion of mineral #3 (float).
   - **Mineral Name4**: The name of mineral #4 (string).
   - **Mineral Proportion4**: The proportion of mineral #4 (float).

2. Run the script:
   - Input the path to the CSV file.
   - The program will validate the file's columns and data.
   - The calculated results will be saved to a new CSV file called `results.csv`.

3. The output file will contain:
   - The system, planet, and moon numbers.
   - The names of the four minerals.
   - The calculated monthly result for each mineral.

---

## Error Handling

The program includes robust error handling to manage the following:
- **Missing or invalid data**: If any required value is missing or incorrectly formatted, the program will print an error message and skip that row.
- **File Not Found**: If the provided file path is incorrect or the file cannot be found, an error message will be displayed.
- **Invalid Input**: If the input values do not meet the expected format (e.g., non-numeric or out of range), a `ValueError` will be raised.

---

## Example

### Input CSV:

| System | Planet | Moon | Utilization Rate | Mineral Name1 | Mineral Proportion1 | Mineral Name2 | Mineral Proportion2 | Mineral Name3 | Mineral Proportion3 | Mineral Name4 | Mineral Proportion4 |
|--------|--------|------|------------------|---------------|---------------------|---------------|---------------------|---------------|---------------------|---------------|---------------------|
| Alpha  | 1      | 1    | 75               | Iron          | 40                  | Copper        | 30                  | Gold          | 20                  | Silver        | 10                  |
| Beta   | 2      | 3    | 50               | Aluminum      | 60                  | Titanium      | 25                  | Zinc          | 10                  | Lead          | 5                   |

### Output CSV:

| System | Planet | Moon | Mineral Name1 | Monthly Result Mineral1 | Mineral Name2 | Monthly Result Mineral2 | Mineral Name3 | Monthly Result Mineral3 | Mineral Name4 | Monthly Result Mineral4 |
|--------|--------|------|---------------|-------------------------|---------------|-------------------------|---------------|-------------------------|---------------|-------------------------|
| Alpha  | 1      | 1    | Iron          | 216000                  | Copper        | 162000                  | Gold          | 108000                  | Silver        | 54000                   |
| Beta   | 2      | 3    | Aluminum      | 432000                  | Titanium      | 180000                  | Zinc          | 75000                   | Lead          | 37500                   |

---

## Requirements

- **Python 3.x**
- **pandas library**

To install the required libraries, you can run:

```bash
pip install pandas

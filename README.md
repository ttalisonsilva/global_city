# Global City Populations - Population of the World's Largest Cities

This repository contains a Python script that displays and analyzes the population data of the world's largest cities.

## Dataset

The dataset includes the following columns:

- **City**: The name of the city.
- **Country**: The country where the city is located.
- **Population (Millions)**: The population of the city in millions.

### Example Data:

| City      | Country | Population (Millions) |
|----------|--------|------------------------|
| Tokyo    | Japan  | 37.4                   |
| Delhi    | India  | 31.0                   |
| Shanghai | China  | 27.1                   |
| São Paulo| Brazil | 22.0                   |
| Mumbai   | India  | 20.7                   |

## Python Script

The script `global_city_populations.py` performs the following tasks:

1. Loads a sample dataset of the world's largest cities and their populations.
2. Displays the data in a tabular format.
3. Identifies and displays the city with the largest population.
4. Saves the data to a CSV file named `global_city_populations.csv`.

## Requirements

- Python 3.x
- pandas library

To install the pandas library, use:
```bash
pip install pandas

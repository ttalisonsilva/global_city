# global_city_populations.py

import pandas as pd
import operator

# Sample data on the population of the world's largest cities

data = {
    "City": ["Tokyo", "Delhi", "Shanghai", "São Paulo", "Mumbai"],
    "Country": ["Japan", "India", "China", "Brazil", "India"],
    "Population (Millions)": [37.4, 31.0, 27.1, 22.0, 20.7]
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Function to display the city population data
def display_city_populations(df):
    print("\nGlobal City Populations:")
    print(df)

# Function to display the city with the largest population
def largest_city(df):
    largest = df.loc[df["Population (Millions)"].idxmax()]
    print(f"\nThe largest city by population is {largest['City']} ({largest['Country']}) with {largest['Population (Millions)']} million people.")

# Main function to run the script
def main():
    print("Welcome to the Global City Populations Analysis")

    # Display the data
    display_city_populations(df)
    
    # Find and display the largest city
    largest_city(df)

    # Save the result to a CSV file
    df.to_csv("global_city_populations.csv", index=False)
    print("\nData saved to 'global_city_populations.csv'.")

# Run the main function if executed directly
if __name__ == "__main__":
    main()

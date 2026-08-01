import pandas as pd

def analyze_squirrel_data():
    # Read the dataset
    data = pd.read_csv("Squirrel.csv")
    
    # Extract the column and drop NaN values to ensure clean data
    fur_colors = data["Primary Fur Color"].dropna()
    
    # Pandas vectorized aggregation - counts occurrences of each unique value
    fur_counts = fur_colors.value_counts()
    
    # Export the Series directly to a CSV file with clear headers
    fur_counts.to_csv("squirrel_count.csv", header=["Count"], index_label="Fur Color")
    
    print("Data analysis complete! Results saved to squirrel_count.csv.")
    print(fur_counts)

if __name__ == "__main__":
    analyze_squirrel_data()

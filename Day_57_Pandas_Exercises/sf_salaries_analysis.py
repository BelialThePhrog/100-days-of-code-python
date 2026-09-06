import pandas as pd

# Load data with handling for 'Not Provided' strings
sal = pd.read_csv("Salaries.csv", na_values='Not Provided')

print("--- DataFrame Info ---")
sal.info()

print("\n--- Salary Statistics ---")
print(f"Average BasePay: {sal['BasePay'].mean()}")
print(f"Highest OvertimePay: {sal['OvertimePay'].max()}")

print("\n--- Specific Employee Query (JOSEPH DRISCOLL) ---")
job_title = sal.loc[sal["EmployeeName"] == "JOSEPH DRISCOLL", "JobTitle"].values[0]
print(f"Job Title: {job_title}")
payment = sal.loc[sal["EmployeeName"] == "JOSEPH DRISCOLL", "TotalPayBenefits"].values[0]
print(f"Total Pay & Benefits: {payment}")

print("\n--- Compensation Extremes ---")
highest_paid = sal.loc[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].max(), "EmployeeName"].values[0]
print(f"Highest Paid Person: {highest_paid}")
lowest_paid = sal.loc[sal["TotalPayBenefits"] == sal["TotalPayBenefits"].min(), "EmployeeName"].values[0]
print(f"Lowest Paid Person: {lowest_paid}")

print("\n--- Historical Averages ---")
averages = sal.groupby('Year').mean(numeric_only=True)['BasePay']
print(averages)

print("\n--- Job Title Insights ---")
print(f"Unique Job Titles: {sal['JobTitle'].nunique()}")
print("Top 5 Most Common Jobs:\n", sal['JobTitle'].value_counts().head(5))

single_jobs_2013 = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)
print(f"Job Titles with only one occurrence in 2013: {single_jobs_2013}")

chiefs = sal['JobTitle'].str.contains(r'\bchief\b', case=False, na=False).sum()
print(f"People with 'Chief' in their job title: {chiefs}")

print("\n--- Correlation Analysis ---")
sal['title_len'] = sal['JobTitle'].apply(len)
salary_correlation = sal[['title_len', 'TotalPayBenefits']].corr()
print(salary_correlation)

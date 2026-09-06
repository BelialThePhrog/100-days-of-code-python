import pandas as pd

# Load data
ecom = pd.read_csv("Ecommerce Purchases")

print("--- DataFrame Info ---")
ecom.info()

print("\n--- Basic Statistics ---")
print(f"Average Purchase Price: {ecom['Purchase Price'].mean()}")
print(f"Highest Purchase Price: {ecom['Purchase Price'].max()}")
print(f"Lowest Purchase Price: {ecom['Purchase Price'].min()}")

print("\n--- Demographic & User Data ---")
print("Number of 'en' Language users:", ecom[ecom["Language"] == "en"].shape[0])
print("Number of Lawyers:", ecom[ecom["Job"] == "Lawyer"].shape[0])
print("AM vs PM Purchases:\n", ecom["AM or PM"].value_counts())
print("Top 5 Most Common Jobs:", ecom["Job"].value_counts().head(5).index.tolist())

print("\n--- Specific Queries ---")
purchase = ecom.loc[ecom["Lot"] == "90 WT", "Purchase Price"].values[0]
print(f"Purchase Price for Lot '90 WT': {purchase}")

pers = ecom.loc[ecom["Credit Card"] == 4926535242672853, "Email"].values[0]
print(f"Email for CC 4926535242672853: {pers}")

amex_high = len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)])
print(f"American Express users with purchases > $95: {amex_high}")

exp_2025 = sum(ecom['CC Exp Date'].apply(lambda x: x[3:]) == '25')
print(f"Credit cards expiring in 2025: {exp_2025}")

print("\n--- Top 5 Email Providers ---")
print(ecom['Email'].apply(lambda x: x.split('@')[1]).value_counts().head(5))

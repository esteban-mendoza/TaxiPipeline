# ANALYSIS WITH PANDAS

# Convert to pandas DataFrame
results_df = pd.DataFrame.from_records(results)

# Convert to correct data types
results_df["total_amount"] = pd.to_numeric(results_df["total_amount"])
results_df["tolls_amount"] = pd.to_numeric(results_df["tolls_amount"])
# Subsetting total_amount >= 0
results_df = results_df[results_df["total_amount"] >= 0]
# Transformations
results_df["revenue"] = results_df["total_amount"] - results_df["tolls_amount"]
# Mean revenue
mean_rev.append(results_df["revenue"].mean())
    
print(mean_rev)
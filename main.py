import pandas as pd

# Sample data (you can expand this or pull from an actual vulnerability scanner)
data = {
    'Vulnerability': ['Vuln A', 'Vuln B', 'Vuln C'],
    'CVSS Score': [9.8, 5.3, 7.5],
    'Exploitability': ['High', 'Low', 'High'],
    'Business Impact': ['Critical', 'Medium', 'High']
}

# Create DataFrame
df = pd.DataFrame(data)

# Define a function to calculate priority score
def calculate_priority(row):
    cvss = row['CVSS Score']
    exploitability = row['Exploitability']
    business_impact = row['Business Impact']

    # Assign weight based on exploitability and business impact
    exploitability_weight = 2 if exploitability == 'High' else 1
    impact_weight = 3 if business_impact == 'Critical' else 2 if business_impact == 'High' else 1

    return cvss * exploitability_weight * impact_weight

# Add a priority column to the DataFrame
df['Priority'] = df.apply(calculate_priority, axis=1)

# Sort vulnerabilities by priority score
df_sorted = df.sort_values(by='Priority', ascending=False)

print(df_sorted[['Vulnerability', 'Priority']])



import pandas as pd

# Path to the full metadata file inside Kaggle
file_path = "/kaggle/input/CORD-19-research-challenge/metadata.csv"

# Load only the first 100,000 rows (adjust if needed)
# Each 100k rows ~ 15–20 MB depending on column sizes
df = pd.read_csv(file_path, nrows=100000, low_memory=False)

# Save the sample file
df.to_csv("metadata_sample.csv", index=False)

print("Sample created:", df.shape)
print("File saved as metadata_sample.csv")

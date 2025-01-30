import kagglehub

# Download latest version
path = kagglehub.dataset_download("ankushpanday1/usa-statewise-daily-temperature-december-2024")

print("Path to dataset files:", path)

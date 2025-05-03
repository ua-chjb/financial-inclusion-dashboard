import pandas as pd

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
path = "s3://datakit-march-april-public/final_data/ridge_features_21_04_25_geo.csv"

india = pd.read_csv(path)
india = india.drop(["Unnamed: 0"], axis=1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
india_norm = india.copy()
for column in india_norm.drop(["state_ut"], axis=1).columns:
    india_norm[column] = ( (india_norm[column]-india_norm[column].min())/(india_norm[column].max()-india_norm[column].min()) ) + 0.1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
path1 = "s3://datakit-march-april-public/final_data/india_population.csv"

india_pop = pd.read_csv(path1)
india_pop = india_pop.drop(["Unnamed: 0"], axis=1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
path2 = "s3://datakit-march-april-public/final_data/descriptions.csv"
india_desc = pd.read_csv(path2)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
path_coef = "s3://datakit-march-april-public/final_data/final_coef_df.csv"
final_coef_df = pd.read_csv(path_coef).drop(["Unnamed: 0"], axis=1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
path_nfcoef = "s3://datakit-march-april-public/final_data/coef_df.csv"
coef_df = pd.read_csv(path_nfcoef)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # 
path_ys = "s3://datakit-march-april-public/final_data/ys.csv"
ys_df = pd.read_csv(path_ys)

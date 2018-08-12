# dimensionality reduction analysis

data = get_data()

# pca
results_pca = pca(data)
print(results_pca)

# isomap
results_iso = iso(data)
print(results_iso)

# local lin. embedding
results_lle = lle(data)
print(results_lle)


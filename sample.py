from dbscan import MyDBSCAN
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import DBSCAN

## Create a data set using data blobs function
def fit():
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(n_samples=100, centers=centers, cluster_std=0.4,random_state=0)
    #X = StandardScaler().fit_transform(X)
    return X

## Cluster classification using my implementation 
def predict():
    X = fit()
    labels = MyDBSCAN(X,eps=0.2,min_pts=3)
    return labels

labels = predict() # Labels created from my implementation 

# Run scikit implementation, 
db = DBSCAN(eps=0.2, min_samples=3).fit(fit())
skl_labels = db.labels_ # labels created by scikit 


for i in range(0, len(skl_labels)):
    if not skl_labels[i] == -1:
        skl_labels[i] += 1

num_disagree = 0
# Count the number of cluster ID's that don't match 
for i in range(0, len(skl_labels)):
    if not skl_labels[i] == labels[i]:
        num_disagree += 1

# If num_disagree = 0, we have a perfect match 
if num_disagree == 0:
    print ('PASS - All labels match!')
else:
    print ('FAIL -', num_disagree, 'labels don\'t match.')       





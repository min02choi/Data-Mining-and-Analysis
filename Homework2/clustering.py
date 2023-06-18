from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

X, _ = make_blobs(n_samples=100, centers=5,
                  n_features=2, random_state=0)

def student_info():
    print("\n[ Student ID: 2116309 ]")
    print("[ Name: 최민영 ]\n")

def show_menu():
    print("1. K-means")
    print("2. Hierarchical Clustering")
    print("3. DBSCAN")
    print("4. Quit")

    num = int(input())
    return num


def k_means(X):
    n_clus = int(input("n_clusters: " ))
    rand_state = int(input("random_state: "))
 
    kmeans = KMeans(n_clusters=n_clus, random_state=rand_state).fit(X)

    print("\n<Clustering Result>")
    print(kmeans.labels_)

def hierarchical_clustering(X):
    n_clus = int(input("n_clusters: " ))
    link = input("linkage: ")

    hier_clt = AgglomerativeClustering(n_clusters=n_clus, linkage=link).fit(X)
    print("\n<Clustering Result>")
    print(hier_clt.labels_)

def db_scan(X):
    input_eps = float(input("eps: "))
    min_samp = int(input("min_samples: "))

    dbscan = DBSCAN(eps=input_eps, min_samples=min_samp).fit(X)
    print("\n<Clustering Result>")
    print(dbscan.labels_)


n = 0
while(n != 4):
    student_info()
    n = show_menu()

    if (n == 1):
        k_means(X)
    elif(n == 2):
        hierarchical_clustering(X)
    elif(n == 3):
        db_scan(X)

import sys,os
import numpy as np
import pandas as pd
import multiprocessing as mp
import random
from functools import reduce
import time
import random
import matplotlib.pyplot as plt
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity


def loadData(fileName, labeled=True):
    mnist_data = pd.read_csv(fileName)
    if labeled:
        label = np.array(mnist_data["label"])
        data = np.array(mnist_data.iloc[:, 1:])
        return data, label
    else:
        return np.array(mnist_data.iloc[:, 1:])

def saveData(fileName, dataToCsv):
    pd.DataFrame(dataToCsv).to_csv(fileName)

def init_centroids(data):
    return random.sample(list(data), 10)


def sum_cluster(cluster):
    return reduce(lambda x, y: x + y, cluster)


def mean_cluster(cluster):
    return sum_cluster(cluster) / len(cluster)


def form_cluster(centroids, data):
    centroids_indices = range(len(centroids))
    clusters = {x: [] for x in centroids_indices}
    for xi in data:
        max_similarity = -1  # Initialize with a minimum value
        for cj_index in centroids_indices:
            cj = centroids[cj_index]
            similarity = cosine_similarity([xi], [cj])[0][0]
            if similarity > max_similarity:
                closest_centroid_index = cj_index
                max_similarity = similarity
        clusters[closest_centroid_index].append(xi)
    return clusters.values()



def move_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        cluster_array = np.array(cluster)
        if len(cluster_array) > 0:
            mean_vector = np.mean(cluster_array, axis=0)
            new_centroids.append(mean_vector)
    return new_centroids

    # return reduce(lambda x, y: x.append(mean_cluster(y)), clusters, [])


def repeat_until_convergence(data, clusters, centroids):
    pre_max_diff = 0
    while True:
        old_centroids = centroids
        centroids = move_centroids(clusters)
        clusters = form_cluster(centroids, data)
        differences = map(lambda x, y: np.linalg.norm(x - y), old_centroids, centroids)
        max_diff = max(differences)
        diff_change = abs((max_diff - pre_max_diff) / np.mean([pre_max_diff, max_diff])) * 100
        pre_max_diff = max_diff
        if np.isnan(diff_change):
            print("Stop worker process id: {0}".format(os.getpid()))
            break
    return clusters, centroids


def cluster(data):
    print("Start worker process id: {0}".format(os.getpid()))
    centroids = init_centroids(data)
    clusters = form_cluster(centroids, data)
    final_clusters, final_centroids = repeat_until_convergence(data, clusters, centroids)
    return final_centroids


def splitData(data, nparts):
    lenPerPart = int(len(data) / nparts)
    res = [data[i * lenPerPart : (i + 1) * lenPerPart] for i in range(nparts - 1)]
    res.append(data[(nparts - 1) * lenPerPart :])
    return res

def showDigit(digitsData, digitsLabel=None):
    plt.figure()
    for i in range(len(digitsData)):
        plt.subplot(8, 15, i + 1).set_title(str(digitsLabel[i]) if digitsLabel is not None else '')
        plt.imshow(digitsData[i].reshape(28, 28), interpolation='bicubic', cmap='Greys')
        plt.xticks([])
        plt.yticks([])

    plt.tight_layout()
    plt.show()


def showGeneral(label):
    num_stats = defaultdict(int)
    for num in label:
        num_stats[num] += 1
    x = sorted(num_stats)
    y = [num_stats[num] for num in x]
    plt.figure()
    plt.bar(x, height=y)
    plt.xticks(x)
    plt.xlabel("Image Content N= "+str(len(label)))
    plt.ylabel("Frequency")
    plt.title("Distribution of MNIST Images")
    plt.show()


def main():
    num_proc = 12
    print("Numbers of Proccess: {0}".format(num_proc))    
    start_time = time.time()

    data, label = loadData("mnist_train.csv")

    load_time = time.time()
    print("Loadtime: {0}s".format(load_time - start_time))

    dataSplit = splitData(data, num_proc)

    p = mp.Pool(processes=num_proc, maxtasksperchild=1)
    res_centroids_multi = p.map(cluster, dataSplit)
    
    combineCentroIds = reduce(lambda x, y: x + y, res_centroids_multi, [])
    res_centroids = cluster(combineCentroIds)
    res_clusters = list(form_cluster(res_centroids, data))

    end_time = time.time()
    print("Runtime: {0}s".format(end_time - load_time))

    print("Saving data to file...")
    for i in range(10):
        saveData(str(i) + ".csv", res_clusters[i])
    saveData("centroids.csv", res_centroids)
    print(" Kmeans Done! Showing cluster ")

    for i in range(10):
        data = loadData(str(i) + ".csv", False)
        showDigit(data[:120])

if __name__ == "__main__":
    main() 

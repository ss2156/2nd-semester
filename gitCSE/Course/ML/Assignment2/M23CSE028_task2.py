import numpy as np
import pandas as pd
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt
from collections import defaultdict

def loadData(fileName, labeled=True):
    mnist_data = pd.read_csv(fileName)
    if labeled:
        label = np.array(mnist_data["label"])
        data = np.array(mnist_data.iloc[:, 1:])
        return data, label
    else:
        return np.array(mnist_data.iloc[:, 1:])

def pca(X, num_components):
    # Center the data
    mean = np.mean(X, axis=0)
    centered_data = X - mean

    # Calculate the covariance matrix
    cov_matrix = np.cov(centered_data, rowvar=False)

    # Compute the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)

    # Sort eigenvectors and eigenvalues in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    eigenvalues = eigenvalues[sorted_indices]
    eigenvectors = eigenvectors[:, sorted_indices]

    # Select the top 'num_components' eigenvectors
    top_eigenvectors = eigenvectors[:, :num_components]

    # Project the data onto the top eigenvectors
    reduced_data = np.dot(centered_data, top_eigenvectors)

    return reduced_data

def gmm_clustering(data, num_clusters):
    gmm = GaussianMixture(n_components=num_clusters, random_state=0)
    gmm.fit(data)
    labels = gmm.predict(data)
    return labels

def showDigitInGrid(digitsData, digitsLabel=None, num_rows=None, num_cols=None):
    num_images = len(digitsData)
    
    if num_rows is None or num_cols is None:
        num_rows = int(np.sqrt(num_images))
        num_cols = int(np.ceil(num_images / num_rows))
    
    plt.figure(figsize=(12, 8))
    for i in range(num_images):
        plt.subplot(num_rows, num_cols, i + 1)
        plt.title(str(digitsLabel[i]) if digitsLabel is not None else '')
        plt.imshow(digitsData[i].reshape(28, 28), interpolation='bicubic', cmap='Greys')
        plt.xticks([])
        plt.yticks([])

    plt.tight_layout()

def main():
    num_components = [32, 64, 128]
    num_clusters = [10, 7, 4]

    data, _ = loadData("mnist_train.csv")
    
    plt.figure(figsize=(15, 10))
    plot_index = 1
    
    for n_components in num_components:
        reduced_data = pca(data, n_components)
        for n_clusters in num_clusters:
            cluster_labels = gmm_clustering(reduced_data, n_clusters)
            plt.subplot(len(num_components), len(num_clusters), plot_index)
            for cluster_id in range(n_clusters):
                cluster_indices = np.where(cluster_labels == cluster_id)[0]
                clustered_data = data[cluster_indices]
                showDigitInGrid(clustered_data[:25], cluster_labels[cluster_indices], num_rows=5, num_cols=5)
            plt.title(f'PCA {n_components}, GMM {n_clusters}')
            plot_index += 1

    plt.show()

if __name__ == "__main__":
    main()

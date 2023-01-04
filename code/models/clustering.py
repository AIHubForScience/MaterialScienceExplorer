import umap
import hdbscan
import pandas as pd

def get_cluster(self, V):
    umap_embeddings = umap.UMAP(n_neighbors=self.neighbours,
                                n_components=self.components,
                                metric='cosine').fit_transform(V)

    
    cluster = hdbscan.HDBSCAN(min_cluster_size=self.cluster_size,
                              metric='euclidean',
                              cluster_selection_method='eom').fit(umap_embeddings)
                              
    #visualisation with 2D UMAP
    umap_data = umap.UMAP(n_neighbors=self.neighbours, n_components=2,
                          min_dist=0.0, metric='cosine').fit_transform(V)
    result = pd.DataFrame(umap_data, columns=['x', 'y'])
    result['labels'] = cluster.labels_

    return result

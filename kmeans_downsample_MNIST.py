def main():

  filename = 'processed_MNIST/random_subsampling/MNIST_20x_random_subsample_0.txt'
  df = load_df_using_clustergrammer(filename)

  ds_df, mbk_labels = run_kmeans_mini_batch(df, 5, axis=1)

  print('K-means\n----------------')

  print(df.shape)
  print(ds_df.shape)


def run_kmeans_mini_batch(df, n_clusters, axis=0):
  from sklearn.cluster import MiniBatchKMeans
  import pandas as pd
  import numpy as np

  # downsample rows
  if axis == 0:
    X = df
  else:
    X = df.transpose()
  # kmeans is run with rows as data-points and columns as dimensions
  mbk = MiniBatchKMeans(init='k-means++', n_clusters=n_clusters,
                        max_no_improvement=10, verbose=0)

  # need to loop through each label (each k-means cluster) and count how many
  # points were given this label. This will give the population size of each label
  # For MNIST, I also need to get the digit breakdown of each cluster to see what
  # digits make up each cluster. Then I can work on overrepresentation examples.
  ################################################
  mbk.fit(X)
  mbk_labels = mbk.labels_
  mbk_clusters = mbk.cluster_centers_

  mbk_cluster_names, mbk_cluster_pop = np.unique(mbk_labels, return_counts=True)

  print('============================')
  print(mbk_cluster_names)
  print(mbk_cluster_pop)
  print('============================')
  print(mbk_labels)

  row_numbers = range(n_clusters)
  row_labels = [ 'cluster-' + str(i) for i in row_numbers]

  # # add number of points in each cluster
  # row_cats = []
  # for i in range(n_clusters):

  #   inst_name = 'cell-clusters: ' + row_labels[i]
  #   inst_count =  'number of cells: '+ str(mbk_cluster_pop[i])
  #   inst_tuple = ( inst_name, inst_count )
  #   row_cats.append(inst_tuple)

  ds = mbk_clusters

  cols = df.columns.tolist()

  # ds_df = pd.DataFrame(data=ds, columns = cols, index=row_cats)
  ds_df = pd.DataFrame(data=ds)

  # swap back for downsampled columns
  if axis == 1:
    ds_df = ds_df.transpose()

  return ds_df, mbk_labels

def load_df_using_clustergrammer(filename):
  from copy import deepcopy
  from clustergrammer import Network

  net = deepcopy(Network())
  net.load_file(filename)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  return df

main()
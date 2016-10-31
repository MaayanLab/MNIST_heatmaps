def main():

  inst_file = 'MNIST_20x_random_subsample_0.txt'
  dm_1 = get_dist_mat_from_file(inst_file)

  inst_file = 'MNIST_20x_random_subsample_1.txt'
  dm_2 = get_dist_mat_from_file(inst_file)

  print(len(dm_1))
  print(len(dm_2))

def get_dist_mat_from_file(inst_file):
  from scipy.spatial.distance import pdist, squareform
  import numpy as np
  from clustergrammer import Network
  from copy import deepcopy

  net = deepcopy(Network())
  net.load_file('processed_MNIST/random_subsampling/'+inst_file)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  mat = df.as_matrix()

  print(mat.shape)
  dist_type = 'euclidean'

  # try col first
  inst_dm = pdist(mat, metric=dist_type)

  return inst_dm

main()
def main():
  print('here')

  from scipy.spatial.distance import pdist, squareform
  import numpy as np
  from clustergrammer import Network

  inst_file = 'MNIST_20x_random_subsample_0.txt'

  net = Network()
  net.load_file('processed_MNIST/random_subsampling/'+inst_file)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  mat = df.as_matrix()

  print(mat.shape)
  dist_type = 'euclidean'

  # try col first
  inst_dm = pdist(mat, metric=dist_type)

  inst_dm = squareform(inst_dm)

  print(inst_dm)

  print(inst_dm.shape)

  print(np.sum(inst_dm))

  # if inst_rc == 'row':
  #   inst_dm = pdist(mat, metric=dist_type)
  # elif inst_rc == 'col':
  #   inst_dm = pdist(mat.transpose(), metric=dist_type)

  # inst_dm[inst_dm < 0] = float(0)

main()
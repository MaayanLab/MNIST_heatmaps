def main():

  # calc_pixel_dist_full_MNIST()

  compare_subsamples_to_full()

def compare_subsamples_to_full():
  from scipy.stats import pearsonr
  import pandas as pd

  import numpy as np
  from scipy.spatial.distance import pdist, squareform

  # making full distance matrix the same shape as the compared matrix
  df_full =  load_pixel_dist_full_MNIST()
  dm_full = df_full.as_matrix()
  dm_full = dm_full[:,0]

  sample_size = 20

  for sample_num_2 in range(5):

    inst_file = 'MNIST_'+str(sample_size)+'x_random_subsample_'+ \
                 str(sample_num_2)+'.txt'
    dm_sub = get_dist_mat_from_file(inst_file)

    pr_results = pearsonr(dm_full, dm_sub)
    print(pr_results)



def calc_pixel_dist_full_MNIST():
  '''
  Calculate the pixel-pixel distance matrix using the full MNIST datset. Use
  this to compare to subsampled and downsampled datasets.
  '''
  import pandas as pd
  from scipy.spatial.distance import pdist

  filename = 'processed_MNIST/large_files/MNIST_row_labels.txt'
  # filename = 'processed_MNIST/random_subsampling/MNIST_20x_random_subsample_0.txt'

  df = load_df_using_clustergrammer(filename)
  print('shape of full MNIST data')
  print(df.shape)

  # calculate distance matrix of full MNIST dataset
  #####################################################
  mat = df.as_matrix()
  inst_dm = pdist(mat, metric='euclidean')

  filename = 'processed_MNIST/pixel_distance_correlations/pixel-pixel_full_MNIST_dist-mat_eucl.txt'

  print('\nshape of calculated distance matrix')
  print(inst_dm.shape)

  # save distance matrix
  ###########################
  inst_df = pd.DataFrame(data=inst_dm)
  inst_df.to_csv(filename, sep='\t', index=False)

def load_pixel_dist_full_MNIST():
  import pandas as pd

  filename = 'processed_MNIST/pixel_distance_correlations/pixel-pixel_full_MNIST_dist-mat_eucl.txt'

  # read tsv to check size
  ##########################
  read_df = pd.read_csv(filename, sep='\t')

  print('\nsize of distance matrix read from file')
  print(read_df.shape)

  return read_df

def get_dist_mat_from_file(inst_file):
  from scipy.spatial.distance import pdist, squareform
  import numpy as np

  filename = 'processed_MNIST/random_subsampling/'+inst_file

  df = load_df_using_clustergrammer(filename)

  cols = df.columns.tolist()

  mat = df.as_matrix()

  dist_type = 'euclidean'

  # try col first
  inst_dm = pdist(mat, metric=dist_type)

  return inst_dm

def load_df_using_clustergrammer(filename):
  from copy import deepcopy
  from clustergrammer import Network

  net = deepcopy(Network())
  net.load_file(filename)
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  return df

main()
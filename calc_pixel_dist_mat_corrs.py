def main():

  calc_pixel_dist_full_MNIST()
  df =  load_pixel_dist_full_MNIST()

  # compare_subsamples()



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

def compare_subsamples():
  from scipy.stats import pearsonr
  import pandas as pd

  from scipy.spatial.distance import pdist, squareform

  sample_size = 1000

  for sample_num_2 in range(4):
    sample_num_1 = 0

    inst_file = 'MNIST_'+str(sample_size)+'x_random_subsample_'+ \
                 str(sample_num_1)+'.txt'

    dm_1 = get_dist_mat_from_file(inst_file)

    inst_file = 'MNIST_'+str(sample_size)+'x_random_subsample_'+ \
                 str(sample_num_2)+'.txt'
    dm_2 = get_dist_mat_from_file(inst_file)

    pr_results = pearsonr(dm_1, dm_2)
    print(pr_results)


def get_dist_mat_from_file(inst_file):
  from scipy.spatial.distance import pdist, squareform
  import numpy as np

  filename = 'processed_MNIST/random_subsampling/'+inst_file

  df = load_df_using_clustergrammer(filename)

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
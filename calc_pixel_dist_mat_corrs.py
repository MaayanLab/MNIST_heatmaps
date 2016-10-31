def main():

  compare_subsamples()

  calc_pixel_dist_full_MNIST()



def calc_pixel_dist_full_MNIST():
  import pandas as pd
  # filename = 'processed_MNIST/large_files/MNIST_row_labels.txt'
  filename = 'processed_MNIST/pixel_distance_correlations/tmp.txt'

  # df = pd.DataFrame()

  # df = load_df_using_clustergrammer(filename)

  # # tmp = squareform(dm_1)
  # tmp = dm_1
  # inst_df = pd.DataFrame(data=tmp)
  # inst_df.to_csv('processed_MNIST/pixel_distance_correlations/tmp.txt', sep='\t', index=False)

  df = pd.read_csv(filename, sep='\t')

  print(df.shape)


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
'''
Python 2.7
The clustergrammer python module can be installed using pip:
pip install clustergrammer

or by getting the code from the repo:
https://github.com/MaayanLab/clustergrammer-py
'''

from clustergrammer import Network
from copy import deepcopy
tmp_net = deepcopy(Network())

# load matrix tsv file
filename = 'processed_MNIST/kmeans_downsample/tmp.txt'
# filename = 'processed_MNIST/random_subsampling/MNIST_20x_random_subsample_0.txt'
# filename = 'processed_MNIST/equal_digit_sampling/MNIST_20_digits_original.txt'


# filter out pixels with 'low' ink levels
###########################################
tmp_net.load_file(filename)
tmp_df = tmp_net.dat_to_df()

tmp_df = tmp_df['mat']
tmp_df[tmp_df< 50] = 0

new_df = {}
new_df['mat'] = tmp_df
net = deepcopy(Network())
net.df_to_dat(new_df)



# optional filtering and normalization
##########################################
# net.filter_sum('row', threshold=20)
# net.normalize(axis='col', norm_type='zscore', keep_orig=True)
net.filter_N_top('row', 500, rank_type='sum')
# net.filter_threshold('row', threshold=3.0, num_occur=4)
# net.swap_nan_for_zero()

net.make_clust(dist_type='cos',views=['N_row_sum', 'N_row_var'] , dendro=True,
               sim_mat=True, filter_sim=0.7, calc_cat_pval=False)

# write jsons for front-end visualizations
net.write_json_to_file('viz', 'json/mult_view.json', 'indent')
net.write_json_to_file('sim_row', 'json/mult_view_sim_row.json', 'no-indent')
net.write_json_to_file('sim_col', 'json/mult_view_sim_col.json', 'no-indent')

def main():
  '''
  There are 70,000 digits
  Each digit is written in a 28x28 image = 784 pixels
  '''

  # subsample_MNIST()

  toy_subsample()

def toy_subsample():
  print('running toy subsampling on small dataset')

  from clustergrammer import Network
  import random

  net = Network()
  net.load_file('processed_MNIST/MNIST_30x_original.txt')
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  num_sample = 120
  random.seed(50)

  subsets = {}

  for i in range(2):

    subset_seed = int(10000*random.random())

    inst_sub = df.sample(n=num_sample, axis=1, random_state=subset_seed)

    sampled_cols = inst_sub.columns.tolist()

    subsets[i] = sampled_cols

    # remove already sampled columns
    all_cols = df.columns.tolist()
    keep_cols = list(set(all_cols) - set(sampled_cols))

    df = df[keep_cols]

  print(subsets[0])
  print(subsets[1])

  print(len(list(set(subsets[0]+subsets[1]))))

def subsample_MNIST():

  from clustergrammer import Network
  net = Network()
  net.load_file('processed_MNIST/large_files/MNIST_row_labels.txt')
  tmp_df = net.dat_to_df()
  df = tmp_df['mat']

  print(df.shape)

  label_dict = get_label_dict()

  num_sample = 30

  # only keep 20 instances of each numbers
  ###########################################
  keep_cols = []

  for inst_digit in label_dict:
    tmp_name = label_dict[inst_digit]

    # select 20 instances of each digit
    for i in range(num_sample):
      inst_name = tmp_name+'-'+str(i)
      keep_cols.append(inst_name)

  # grab subset of numbers
  df = df[keep_cols]

  # # add categories to columns
  # ###############################
  # new_col_labels = df.columns.tolist()

  # tuple_col_labels = []
  # for inst_label in new_col_labels:
  #   # add number name
  #   inst_name = 'Numbers: ' + inst_label
  #   # add category name
  #   inst_cat = 'Digit: ' + inst_label.split('-')[0]
  #   inst_tuple = ( inst_name, inst_cat )
  #   tuple_col_labels.append(inst_tuple)

  # df.columns = tuple_col_labels

  # # add row categories
  # ###############################
  # new_row_labels = df.index.tolist()
  # tuple_row_labels = []

  # max_radius = np.sqrt( np.square(28) + np.square(28) )

  # for inst_row in new_row_labels:

  #   # make name
  #   inst_name = 'Pixels: '+ inst_row

  #   # make radius category
  #   pos = inst_row.split('pos_')[1]
  #   inst_x = int(pos.split('-')[0])
  #   inst_y = int(pos.split('-')[1])
  #   inst_radius = max_radius - np.sqrt( np.square(inst_x) + np.square(inst_y) )
  #   inst_cat = 'Center: '+ str(inst_radius)

  #   inst_tuple = ( inst_name, inst_cat )

  #   tuple_row_labels.append(inst_tuple)

  # df.index = tuple_row_labels

  print('shape after processing')
  print(df.shape)

  df.to_csv('processed_MNIST/MNIST_'+str(num_sample)+'x_original.txt',sep='\t')





def download_mnist_from_server():
  from sklearn.datasets import fetch_mldata

  mnist = fetch_mldata('MNIST original', data_home='custom_data_home')

  print(mnist.shape)

def get_label_dict():
  label_dict = {}
  label_dict[0] = 'Zero'
  label_dict[1] = 'One'
  label_dict[2] = 'Two'
  label_dict[3] = 'Three'
  label_dict[4] = 'Four'
  label_dict[5] = 'Five'
  label_dict[6] = 'Six'
  label_dict[7] = 'Seven'
  label_dict[8] = 'Eight'
  label_dict[9] = 'Nine'

  return label_dict

main()
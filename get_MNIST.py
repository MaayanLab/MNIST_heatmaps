def main():
  '''
  There are 70,000 digits 
  Each digit is written in a 28x28 image = 784 pixels
  '''


  # overview_mnist_mat()

  # check_digit()

  make_clust()

  # tmp = range(28)
  # tmp = [i - 13.5 for i in tmp]
  # print(tmp)

def make_clust():
  from scipy.io import loadmat 
  import pandas as pd 

  mnist_obj = loadmat('custom_data_home/mldata/mnist-original.mat')

  digit_labels = mnist_obj['label']

  print(digit_labels)

  # write matrix to file 
  mat = mnist_obj['data']

  small_mat = mat[:,:100]

  print(small_mat.shape)

  num_zeros = 100

  num_pixels = 784


  col_labels = []
  for i in range(num_zeros):
    col_labels.append('Zero-'+str(i))

  row_labels = []
  for i in range(28):
    for j in range(28):
      row_labels.append('pos_'+str(i)+'_'+str(j))


  df = pd.DataFrame(data = small_mat, index=row_labels, columns=col_labels)


  df.to_csv('example_matrix.txt',sep='\t')


def check_digit():
  from scipy.io import loadmat 
  mnist_obj = loadmat('custom_data_home/mldata/mnist-original.mat')

  mat = mnist_obj['data']

  print(mat.shape)

  # 3: 20500
  digit = mat[:,20501]

  img_width = 28

  f = open('example_image.txt','w')

  for i in range(img_width):
    f.write('col-'+str(i)+'\t')

  f.write('\n')

  for inst_row in range(img_width):

    img_row =  digit[ inst_row*28: (inst_row+1)*28 ]

    f.write('row-'+str(inst_row))
    for i in range(len(img_row)):

      f.write( str( img_row[i] ) +'\t')

    f.write('\n')



  f.close()

def overview_mnist_mat():
  from scipy.io import loadmat 
  mat = loadmat('custom_data_home/mldata/mnist-original.mat')

  print(mat.keys())

  print(type(mat['data']))

  print(mat['data'].shape)

  print('\n\nml_data_descr_ordering')
  print(type(mat['mldata_descr_ordering']))
  print(mat['mldata_descr_ordering'].shape)
  print(mat['mldata_descr_ordering'])

  print('\n\nlabel')
  print(mat['label'].shape)

  print('\n\nglobals')
  print(mat['__globals__'])

def download_mnist_from_server():  
  from sklearn.datasets import fetch_mldata

  mnist = fetch_mldata('MNIST original', data_home='custom_data_home')

  print(mnist.shape)

main()
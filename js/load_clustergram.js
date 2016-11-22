
/*
Example files
*/
make_clust('mult_view.json');

function make_clust(inst_network){

    d3.json('json/'+inst_network, function(network_data){

      // define arguments object
      var args = {
        root: '#container-id-1',
        'network_data': network_data,
        'about':'Zoom, scroll, and click buttons to interact with the clustergram.',
        'row_tip_callback':show_pixel,
        'col_tip_callback':show_number,
        'tile_tip_callback':show_number_and_pixel,
        'sidebar_width':150,
        tile_colors: ['#2F4F4F', '#9370DB'],
        // value-cat colors
        cat_value_colors: ['#006400', '#FF0000']
      };

      resize_container(args);

      d3.select(window).on('resize',function(){
        resize_container(args);
        cgm.resize_viz();
      });

      cgm = Clustergrammer(args);

      d3.select(cgm.params.root + ' .wait_message').remove();

  });

}

function get_file_for_column(inst_column){
  var inst_number = inst_column;

  var col_type = inst_number.split('-')[0];

  var inst_digit = String(inst_number.split('-')[0]);

  if (col_type != 'cluster'){
    var inst_filename = 'img/MNIST_digits/'+inst_digit+'/'+
                        String(inst_number) + '.png';
  } else {
    var inst_filename = 'img/MNIST_kmeans_clusters/tmp/'+
                        String(inst_number) + '.png';
  }

  return inst_filename;
}

function show_number_and_pixel(tile_info){

  var inst_column = tile_info.col_name;
  var inst_pixel = tile_info.row_name.replace(' ','_');

  image_container = d3.selectAll('.tile_tip')
                      .append('div')
                      .classed('MNIST_container', true)
                      .style('margin-top', '10px')


  image_container
    .append('img')
    .attr('src', function(){
      var inst_filename = get_file_for_column(inst_column);
      return inst_filename;
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('display','block')
    .style('float','left');
    // .style('margin-left', '10px')
    // .style('opacity',0.1)

  image_container
    .append('img')
    .style('margin-left', '-100px')
    .attr('src', function(){

      pixel_image_name = 'img/pixel_images/' + inst_pixel + '.png'
      return pixel_image_name;
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('opacity', 0)
    .transition()
    .delay(100)
    .style('opacity', 1)

}


function show_number(col_data){
  var inst_column =  col_data.name;

  d3.selectAll('.col_tip')
    .append('img')
    .attr('src', function(){

      var inst_filename = get_file_for_column(inst_column);

      return inst_filename;
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('display','block')
    .style('margin-top', '10px');

  var number_info = d3.selectAll('.col_tip')
    .append('div')
    .classed('number_info', true);

  number_info
    .append('p')
    .text(col_data['cat-0'])
    .style('margin-top','5px');

  number_info
    .append('p')
    .text(col_data['cat-1'])
    .style('margin-top','5px');

  number_info
    .append('p')
    .text(col_data['cat-2'])
    .style('margin-top','5px');

}

function show_pixel(pixel_data){
  var inst_pixel = pixel_data.name;

  inst_pixel = inst_pixel.replace(' ','_');

  image_container = d3.selectAll('.row_tip')
                      .append('div')
                      .classed('MNIST_container', true)
                      .style('margin-top', '10px')


  image_container
    .append('img')
    .attr('src', 'img/pixel_images/background.png')
    .style('width', '100px')
    .style('height', '100px')
    .style('display','block')
    .style('float','left');
    // .style('margin-left', '10px')
    // .style('opacity',0.1)

  image_container
    .append('img')
    .style('margin-left', '-100px')
    .attr('src', function(){

      pixel_image_name = 'img/pixel_images/' + inst_pixel + '.png'
      return pixel_image_name;
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('opacity', 0)
    .style('opacity', 1)


}

function resize_container(args){

  var screen_width = window.innerWidth;
  var screen_height = window.innerHeight - 20;

  d3.select(args.root)
    .style('width', screen_width+'px')
    .style('height', screen_height+'px');
}


function show_two_numbers(inst_number){

  image_container = d3.selectAll('.col_tip')
                      .append('div')
                      .classed('MNIST_container', true)
                      .style('margin-top', '10px')



  image_container
    .append('img')
    .attr('src', function(){

      var inst_digit = String('One');
      var inst_filename = 'img/MNIST_digits/'+inst_digit+'/'+
                          String('One-1') + '.png';
      return inst_filename;
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('display','block')
    .style('float','left');

  image_container
    .append('img')
    .attr('src', function(){

      console.log('showing two numbers')

      var inst_digit = String(inst_number.split('-')[0]);
      var inst_filename = 'img/MNIST_digits/'+inst_digit+'/'+
                          String(inst_number) + '.png';
      return inst_filename;
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('display','block')
    .style('margin-left', '110px')

}
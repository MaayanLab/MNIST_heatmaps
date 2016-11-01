
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
        'col_tip_callback':show_number_and_pixel,
        'tile_tip_callback':test_tile_callback,
        'sidebar_width':150
      };

      resize_container(args);

      d3.select(window).on('resize',function(){
        resize_container(args);
        cgm.resize_viz();
      });

      cgm = Clustergrammer(args);

      d3.select(cgm.params.root + ' .wait_message').remove();

      // // Enrichr categories
      // //////////////////////
      // enr_obj = Enrichr_request(cgm);
      // enr_obj.enrichr_icon();

  });

}

function test_tile_callback(tile_info){
  console.log('\n\ntest_tile_callback')

  var row_name = tile_info.row_name;
  var col_name = tile_info.col_name;

  console.log('row_name: ' + row_name)
  console.log('col_name: ' + col_name)

}


function show_number_and_pixel(inst_number){

  image_container = d3.selectAll('.col_tip')
                      .append('div')
                      .classed('MNIST_container', true)
                      .style('margin-top', '10px')


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
    .style('float','left');
    // .style('margin-left', '10px')
    // .style('opacity',0.1)

  image_container
    .append('img')
    .style('margin-left', '-100px')
    .attr('src', function(){


      return 'tmp.png';
    })
    .style('width', '100px')
    .style('height', '100px')
    .style('opacity', 0)
    .transition()
    .delay(100)
    .style('opacity', 1)

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
    .style('display','block')
    .style('margin-left', '110px')

}

function show_number(inst_number){
  d3.selectAll('.col_tip')
    .append('img')
    .attr('src', function(){

      console.log(inst_number)

      var inst_digit = String(inst_number.split('-')[0]);
      // var inst_number = String(inst_number);
      var inst_filename = 'img/MNIST_digits/'+inst_digit+'/'+
                          String(inst_number) + '.png';

      return inst_filename;
    })
    .style('width', '100px')
    .style('display','block')
    .style('margin-top', '10px');
}

function resize_container(args){

  var screen_width = window.innerWidth;
  var screen_height = window.innerHeight - 20;

  d3.select(args.root)
    .style('width', screen_width+'px')
    .style('height', screen_height+'px');
}

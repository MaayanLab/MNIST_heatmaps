
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
        'col_tip_callback':show_number,
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

function show_two_numbers(inst_number){

  image_container = d3.selectAll('.col_tip')
                      .append('div')
                      .classed('MNIST_container', true)
                      .style('margin-top', '10px')



  image_container
    .append('img')
    .attr('src', function(){

      var inst_digit = String('One');
      // var inst_number = String(inst_number);
      var inst_filename = 'img/MNIST_digits/'+inst_digit+'/'+
                          String('One-1') + '.png';
      return inst_filename;
    })
    .style('width', '100px')
    .style('display','block')
    // .style('margin-top', '10px')
    .style('float','left');

  image_container
    .append('img')
    .attr('src', function(){

      console.log('showing two numbers')

      var inst_digit = String(inst_number.split('-')[0]);
      // var inst_number = String(inst_number);
      var inst_filename = 'img/MNIST_digits/'+inst_digit+'/'+
                          String(inst_number) + '.png';
      return inst_filename;
    })
    .style('width', '100px')
    .style('display','block')
    // .style('margin-top', '10px')
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

      inst_filename = 'tmp.png'
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

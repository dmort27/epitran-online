$(document).ready(function() {

    function update(e) {
      var textin = $('#textin').val();
      var lang = $('#language').val();
      $.ajax({
        url: '/gettrans',
        dataType: 'html',
        data: {
          textin: textin,
          lang: lang
        },
        success: function(data) {
          console.log(data);
          $('#textout').html(data);
        }
      });
    };

    $('#textin').on('input', update);
    $('#language').change(update);
//    $('#submit').clicked(update);

});

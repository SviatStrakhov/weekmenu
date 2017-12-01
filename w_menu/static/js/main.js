function initProduct() {
    $('.available-box input[type="checkbox"]').click(function(event){
        var box = $(this);
        $.ajax(box.data('url'), {
        'type': 'POST',
        'async': true,
        'dataType': 'json',
        'data': {
        	'pk': box.data('product-id'),
        	'present': box.is(':checked') ? '1': '',
        	'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        },
        'error': function(xhr, status, error){
        	alert(error);
        },
        'succes': function(data, status, xhr){
        	alert(data['key']);
        }
    });
  });
}

$(document).ready(function(){
    initProduct();
})


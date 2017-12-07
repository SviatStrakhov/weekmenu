function initProduct() {
    $('.available-box input[type="checkbox"]').click(function(event){
        var box = $(this);
        // var productToHide = box.parent().parent()
        // productToHide.hide()
        $.ajax(box.data('url'), {
	        'type': 'POST',
	        'async': true,
	        'dataType': 'json',
	        'data': {
	        	'pk': box.data('product-id'),
	        	'available': box.is(':checked') ? '1': '',
	        	'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
	        },
	        'error': function(xhr, status, error){
	        	alert('error');
	        },
	        'success': function(data, status, xhr){
	        	alert(data['key']);
	        }
    	});
  	});
}

$(document).ready(function(){
    initProduct();
})


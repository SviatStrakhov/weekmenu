
function finishProduct(){
	$('.available-box button[id="finish_product_btn"]').click(function(event){
		var box = $(this);
		var productToHide = box.parent().parent()
        productToHide.hide()
		$.ajax(box.data('url'), {
			type: 'POST',
			async: true,
			dataType: 'json',
			data: {
				'pk': box.data('product-id'),
				'submit': true,
				'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
			},
			error: function(xhr, status, error){
	        	alert('error');
	        },
		});
	});
}

$(document).ready(function(){
	finishProduct();
})

function initProduct() {
    $('.available-box input[type="checkbox"]').click(function(event){
        var box = $(this);
        var productToHide = box.parent().parent()
        productToHide.hide()
        $.ajax(box.data('url'), {
	        'type': 'POST',
	        'async': true,
	        'dataType': 'json',
	        'data': {
	        	'pk': box.data('product-id'),
	        	'available': box.is(':checked'),
	        	'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
	        },
	        'error': function(xhr, status, error){
	        	alert('error');
	        },
    	});
  	});
}

$(document).ready(function(){
    initProduct();
})




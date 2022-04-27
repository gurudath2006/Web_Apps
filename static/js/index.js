$(document).ready(function(){

    $('#provider-search').click(function(e){
        e.preventDefault();
        var search_name = $('#search-name').val().toLowerCase();
        var search_service = $('#search-service').val().toLowerCase();
        $('.card').each(function(){
            card_name = $(this).find('#card-provider-name').html().toLowerCase();
            card_service = $(this).find('#card-provider-service-category').html().toLowerCase();
            if((search_name == '' || card_name.indexOf(search_name) >= 0) && (search_service == 'all' || card_service.indexOf(search_service) >= 0))
            {
                $(this).show();
            }
            else
            {
                $(this).hide();
            }
        });
    });

	$('#patient-login').click(function(e){
        e.preventDefault();
        var username = $('#patient-email').val();
        var password = $('#patient-password').val();

        $.ajax({
            url: '/patient-login',
            data: {                
                username: username,
                password: password                 
            },
            type: 'POST',
            success: function(data) {
                if(data.error != '')
                { 
                    $('#patient-login-result').show();
                    $('#patient-login-result').html(data.error);
                }
                else
                {
                    window.location = data.location;
                }
            },
            error: function(error) {
                console.log(error);
            }
        });

        
    })
});


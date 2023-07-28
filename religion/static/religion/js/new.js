$(document).ready(function() {
    $('#new-button').click(function() {
        $('#new-button-p').slideUp(1000);
        $('#main-content').fadeOut(1000, function() {
            $('#new-content').fadeIn(1000, function() {
                $('body').css('background-color', '#212529');
            });
        });
    });
    $('#new-end-button').click(function() {
        $('#new-end-button-p').slideUp(1000);
        $('body').css('background-color', '#ffffff');
        $('#new-content').fadeOut(1000, function() {
            $('#main-content').fadeIn(1000)
        })
    })
})
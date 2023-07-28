$('#logout-next').attr('value', document.URL);
$('#logout-link').click(function() {
    $('#logout-form').submit();
});
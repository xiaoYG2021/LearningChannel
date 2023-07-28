$('#events-button').click(function() {
    let text=$('#events-button').attr('aria-expanded')=='true'?'关闭':'查看';
    $('#events-button').text(text);
})
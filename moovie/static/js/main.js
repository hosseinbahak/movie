$('#myTab a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
})
$('.movie-item__rate').each(function(rate){
            var rate = $(this).html();
            if($(this).hasClass('movie-item_rate--good')){$(this).removeClass('movie-item_rate--good');}
            if($(this).hasClass('movie-item_rate--normal')){$(this).removeClass('movie-item_rate--normal');}
            if($(this).hasClass('movie-item_rate--bad')){$(this).removeClass('movie-item_rate--bad');}
            if(parseFloat(rate) > 7){
                $(this).addClass('movie-item__rate--good');
            }
            else if(parseFloat(rate) > 5){
                $(this).addClass('movie-item__rate--normal');
            }
            else{
                $(this).addClass('movie-item__rate--bad');
            }
        });
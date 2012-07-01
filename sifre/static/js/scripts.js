function viewport(){
    e = window;
    a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    };
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
};


function pjax(){

    event.preventDefault();
    container = $(this).attr('rel'),
    target = $(this).attr('href');

    $.get(
        target,
        function(data){
            $(container).empty();
            $(container).append(data);
        }
    
    );
}
function collapsable(){
    container = $(this).attr('rel'),
    target = $(this).attr('href');

    $('.expanded').toggle('blind').toggleClass('expanded')
    $('.active').toggleClass('active');
    $(this).off('click');
    $(this).toggleClass('active');

    $(container).toggle('blind')
                .toggleClass('expanded');

    return false;
}
function setLayout(){
    console.log('Got called')
    vp = viewport();
    visible_height = (vp.height-($('header').height() + $('footer').height())-55);
    $('section').height(visible_height);
    $('#pages').height(visible_height);
    $('#display').css({
        height:visible_height-50,
        width:vp.width-$('#pages').width()-25,
        });
}
$(function(){
    vp = viewport();
    setLayout();
    $(window).resize(function(){setLayout()});
    window.setTimeout(function(){
        $('#messages').toggle('fade')
    }, 3000);

    $('body').on('ajaxComplete', function(){
        $(this).find('.tabs').tabs();//XXX: No debería hacer falta
    });                 
    $('.tabs').tabs();//FIXME: asignar a todos los elementos, incluso cuando 
                      //        se cargan con ajax

    $('body').on('click', '.control',function(){
        target = $(this).attr('href');
        $(this).toggleClass('active');
        $(target).toggle('fade', 300);
        return false;
        
    });
    $('body').on('click.pjax', '.pjax', pjax)
    $('body').on('click.collapsable','.collapsable', collapsable)

    $('.flex-slider').flexslider({
        animation: "slide",
        slideshow: false,
        controlNav: false,
        controlsContainer: ".flex-container",
        start: function(slider) {
            $('.current-slide').text(slider.currentSlide+1);
            $('.total-slides').text(slider.count);
            curPage = $('#pages li')[slider.currentSlide];
            $(curPage).toggleClass('current');
        },
        after: function(slider) {
            $('.current').toggleClass('current');
            $('.current-slide').text(slider.currentSlide+1);
            curPage = $('#pages li')[slider.currentSlide];
            $(curPage).toggleClass('current');
        }
    });
});

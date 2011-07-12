$(function(){
    getNextContent('main', '#content');
    
    $('.ticker').screenSlide({'visible' : 8000});
});

function getNextContent(region, container) {
    var $container = $(container);
    $.ajax({
        type : 'GET',
        url : '/ajax/',
        cache : false,
        data : {
            region : region,
            last : $container.data('currentcontent')
        },
        dataType : 'html',
        success: function(data, status, jqXHR) {
            var $data = $(data)
            var duration = $data.data('duration');
            $data.addClass('next');
            
            $container.children().hide('drop', {}, 1000, function(elem){
                $(this).remove();
                $data.removeClass('next');
            });
            $container.append($data);
            $container.data('currentcontent', $data.data('id'));
            
            var updateTimeout = window.setTimeout(getNextContent, 
                duration * 1000, region, container)
        }
    })
}

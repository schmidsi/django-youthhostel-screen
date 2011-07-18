$(function(){
    getNextContent('main', '#content');
    getNextContent('announcements', '#announcements');
    
    $('.ticker').screenSlide({'visible' : 8000});
    
    var weatherInterval = window.setInterval(function(){
        $('#weather').load('/ajax/weather/');
    }, 30*60*1000);
    
    var tickerInterval = window.setInterval(function(){
        $('#ticker').load('/ajax' + $('#container').data('path') + '?region=ticker&content=all', function(){
            $('.ticker').screenSlide({'visible' : 8000});
        });
    }, 30*60*1000);
});

function getNextContent(region, container) {
    var $container = $(container);
    $.ajax({
        type : 'GET',
        url : '/ajax' + $('#container').data('path'),
        cache : false,
        data : {
            region : region,
            last : $container.data('currentcontent'),
            content : 'random'
        },
        dataType : 'html',
        success: function(data, status, jqXHR) {
            var $data = $(data)
            var duration = $data.data('duration');
            var oldContent = $container.children().fadeOut(500);
            
            if (duration == undefined || duration < 1) {
                duration = 1;
            }
            
            $container.append($data);
            $data.hide().fadeIn(500);
            $container.data('currentcontent', $data.data('id'));
            
            window.setTimeout(function() { oldContent.remove() }, 5000);
            
            window.setTimeout(getNextContent, duration * 1000, region, container)
        },
        error: function(jqXHR, status, error) {
            /* silently retry to get content after 10 sec */
            var updateTimeout = window.setTimeout(getNextContent, 
                10 * 1000, region, container)
        }
    })
}

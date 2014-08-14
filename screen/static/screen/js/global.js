var timeouts = {};

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

            if ($data.hasClass('youtube')) {
                initYoutube($data, region, container);
            }

            $data.hide().fadeIn(500);
            $container.data('currentcontent', $data.data('id'));
            
            window.setTimeout(function() { oldContent.remove() }, 5000);
            
            timeouts[region] = window.setTimeout(getNextContent, duration * 1000, region, container)
        },
        error: function(jqXHR, status, error) {
            /* silently retry to get content after 10 sec */
            var updateTimeout = window.setTimeout(getNextContent, 
                10 * 1000, region, container)
        }
    })
}

function initYoutube($el, region, container) {
    var player = new YT.Player($el.get(0), {
        height: $el.height(),
        width: $el.width(),
        videoId: $el.data('youtubeid'),
        playerVars: { 'autoplay': 1, 'controls': 0 },
        events: {
            'onReady': function(event) {
                event.target.playVideo();
                event.target.mute();

                // emergency exit: if the video has 3 time longer than its
                // duration to play (due to network errors, etc), go to next content
                window.clearTimeout(timeouts[region]);
                timeouts[region] = window.setTimeout(
                    getNextContent,
                    event.target.getDuration() * 3000,
                    region,
                    container
                )
            },
            'onStateChange': function(event) {
                if (event.data == YT.PlayerState.ENDED) {
                    window.clearTimeout(timeouts[region]);
                    getNextContent(region, container);
                }
            }
        }
    });
}

function onYouTubeIframeAPIReady() {
    console.log('onYouTubeIframeAPIReady');
}
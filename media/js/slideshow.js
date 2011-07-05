(function($){
    $.fn.screenSlide = function(options) {
        var settings = {
            'visible' : 5000
        };
        
        if ( options ) { 
            $.extend( settings, options );
        }
        
        return this.each(function() {
            var $this = $(this);
            
            // initalisation
            if (!$this.data('screenSlide')) {
                $this.data('screenSlide', {
                    'items' : $this.children(),
                    'count' : $this.children().length,
                    'currentItem' : null,
                    'nextItem' : null
                });
            }
            
            var data = $this.data('screenSlide');
            if (data.count > 0) {
                data.currentItem = data.items.first();
                data.currentItem.addClass('show');
            }
            
            data.interval = setInterval(function(){
                data.nextItem = data.currentItem.next();
                if (data.nextItem.length==0) {
                    data.nextItem = data.items.first();
                }
                
                console.log(data.currentItem.css('backgroundImage'), 
                            data.nextItem.css('backgroundImage'));
                
                data.currentItem.removeClass('show');
                data.nextItem.addClass('show');
                data.currentItem = data.nextItem;
                
            }, settings.visible);
        });
    };
})(jQuery);

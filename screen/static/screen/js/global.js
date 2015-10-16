$(function() {
  var skycons = new Skycons({color: 'rgb(80, 145, 205)'})

  skycons.add('weather-icon', Skycons.PARTLY_CLOUDY_DAY)
  skycons.play()

  var url = 'https://maps.googleapis.com/maps/api/geocode/json';
  var options = {
    key: 'AIzaSyBfgQvdnxaPG86vH75V8HamSvyeUlURxT8',
    address: window.ScreenData.location
  }

  $.get(url, options, function(data, status, xhr) {
    console.log(data, status, xhr)
  });
})

/*
function getFacebookPost($el, region, container) {
    var user = $el.data('user'),
        url = 'https://graph.facebook.com/' + user + '/posts/?fields=type,message,object_id&filter=type:photo&access_token=159457810754902|UqvcQEszzDvlLlft85FtuP2LWYo';

    $.get(url, function(json) {
        var last5Posts = json.data.slice(0, 10),
            randomPost = last5Posts[parseInt(Math.random()*9)];

        console.log(randomPost);

        $el.find('.caption').text(randomPost.message);

        $.get('https://graph.facebook.com/' + randomPost.object_id + '?access_token=159457810754902|UqvcQEszzDvlLlft85FtuP2LWYo', function(json) {
            $el.css('background-image', 'url(' + json.images[0].source + ')');
        });

    });
}
*/

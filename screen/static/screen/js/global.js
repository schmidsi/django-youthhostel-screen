/* global $, Skycons */

$(function () {
  var skycons = new Skycons({color: 'rgb(80, 145, 205)'})

  skycons.add('weather-icon', Skycons.FOG)
  skycons.play()

  var url = 'https://maps.googleapis.com/maps/api/geocode/json'
  var options = {
    key: 'AIzaSyBfgQvdnxaPG86vH75V8HamSvyeUlURxT8',
    address: window.ScreenData.location
  }

  $.getJSON(url, options)
    .then(function (data, status, xhr) {
      if (!data.results || data.results.length === 0) {
        console.warn('GEOCODE failed', window.ScreenData.location, data, status, xhr)
        return false
      }

      window.ScreenData.latlng = data.results[0].geometry.location
      var url = 'https://api.forecast.io/forecast/d4c70212b090e44a4250da97aa6bb54f/'

      url = url + window.ScreenData.latlng.lat + ',' + window.ScreenData.latlng.lng

      return $.ajax({
        type: 'GET',
        url: url,
        jsonp: 'callback',
        dataType: 'jsonp',
        data: {
          units: 'si'
        }
      })

    // return $.getJSON(url)
    })
    .then(function (data, status, xhr) {
      skycons.set('weather-icon', data.currently.icon)
      $('[data-hook~=weather-temperature]').text(data.currently.temperature.toFixed() + '°C')
    })
    .then(null, function (err) {
      throw err
    })
})

/*
function getFacebookPost($el, region, container) {
    var user = $el.data('user'),
        url = 'https://graph.facebook.com/' + user + '/posts/?fields=type,message,object_id&filter=type:photo&access_token=159457810754902|UqvcQEszzDvlLlft85FtuP2LWYo'

    $.get(url, function(json) {
        var last5Posts = json.data.slice(0, 10),
            randomPost = last5Posts[parseInt(Math.random()*9)]

        console.log(randomPost)

        $el.find('.caption').text(randomPost.message)

        $.get('https://graph.facebook.com/' + randomPost.object_id + '?access_token=159457810754902|UqvcQEszzDvlLlft85FtuP2LWYo', function(json) {
            $el.css('background-image', 'url(' + json.images[0].source + ')')
        })

    })
}
*/

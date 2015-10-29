import $ from 'jquery'
import _ from 'underscore'

import PanelBaseView from './base-view'

export default class WeatherView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.template = _.template($('#weather-template').html())
  }

  attributes () {
    return {
      class: 'flex flex-center cover-parent'
    }
  }

  render () {
    if (this.data.location === '' && window.ScreenData.latlng) {
      this.renderWeather(window.ScreenData.latlng.lat, window.ScreenData.latlng.lon)
    } else {
      let url = 'https://maps.googleapis.com/maps/api/geocode/json'
      let options = {
        key: 'AIzaSyBfgQvdnxaPG86vH75V8HamSvyeUlURxT8',
        address: (this.data.location || window.ScreenData.location)
      }

      $.getJSON(url, options)
      .then((data, status, xhr) => {
        if (!data.results || data.results.length === 0) {
          console.warn('GEOCODE failed', (this.data.location || window.ScreenData.location), data, status, xhr)
          return false
        }

        let loc = data.results[0].geometry.location

        this.renderWeather(loc.lat, loc.lng)
      })
    }

    return this
  }

  renderWeather (lat, lon) {
    this.$el.html(this.template({ lat: lat, lon: lon }))
    this.$('iframe').on('load', () => this.trigger('loaded'))
  }

}

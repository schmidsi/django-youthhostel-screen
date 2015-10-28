import $ from 'jquery'
import _ from 'underscore'

import PanelBaseView from './base-view'

export default class MediaPanelView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.templateMeta = _.template($('#media-meta').html())
    this.loadAssets = true

    if (this.model.get('data').cover) {
      this.template = _.template($('#media-template-cover').html())
    } else {
      this.template = _.template($('#media-template-contain').html())
    }
  }

  attributes () {
    let attributes = super.attributes()
    let data = this.model.get('data')

    attributes.class = `mediafile mediatype-${ data.type } media-cover-${ data.cover }`

    return attributes
  }

  render () {
    let data = this.model.toJSON().data

    if (data.caption || data.description || data.copyright) {
      data.meta = this.templateMeta(data)
    } else {
      data.meta = ''
    }

    // HACK: wait for image to be loaded
    // via: http://stackoverflow.com/questions/5057990/how-can-i-check-if-a-background-image-is-loaded
    let self = this
    $('<img />').attr('src', data.url).load(function () {
      $(this).remove()

      let $target

      if (data.cover) {
        $target = self.$el
      } else {
        $target = self.$('[data-hook=bg-image]')
      }

      $target.css('background-image', `url(${ data.url })`)

      self.trigger('loaded')
    })

    this.$el.html(this.template(data))

    return this
  }
}

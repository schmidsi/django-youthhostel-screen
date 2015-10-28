import $ from 'jquery'
import _ from 'underscore'

import PanelBaseView from './base-view'

export default class TextPanelView extends PanelBaseView {
  constructor (options) {
    super(options)
    this.template = _.template($('#text-template').html())
  }

  attributes () {
    let attributes = super.attributes()

    attributes.class = `text text-size-${ this.model.get('data').size } flex flex-center flex-grow`

    return attributes
  }

  render () {
    let pspans = this.data.text.replace(/<p>/g, '').replace(/<\/p>/g, '')
    let lines = pspans.split(/\r\n|\r|\n/g)

    this.data.textWrapped = '<span>' + lines.join('</span><br><span>') + '</span>'
    this.$el.html(this.template(this.data))
    return this
  }
}

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
    let data = this.model.toJSON().data
    let pspans = data.text.replace(/<p>/g, '').replace(/<\/p>/g, '')
    let lines = pspans.split(/\r\n|\r|\n/g)

    data.textWrapped = '<span>' + lines.join('</span><br><span>') + '</span>'
    this.$el.html(this.template(data))
    return this
  }
}

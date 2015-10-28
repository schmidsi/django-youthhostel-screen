/* global playerjs */
import $ from 'jquery'
import _ from 'underscore'
import _playerjs from 'player.js' // eslint-disable-line

import PanelBaseView from './base-view'
import MediaPanelView from './media-view'
import { Panel } from './base-model'

export default class EmbedlyView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.loadAssets = true

    this.data = this.model.toJSON().data
  }

  attributes () {
    let attributes = super.attributes()
    let data = this.model.get('data')

    attributes.class = `embedly embedly-${ data.response.type } cover-parent`

    return attributes
  }

  render () {
    switch (this.data.response.type) {
      case 'video':
        return this.renderVideo()
      case 'photo':
        return this.renderPhoto()
      case 'rich':
        return this.renderRich()
      case 'link':
        return this.renderLink()
    }
  }

  renderVideo () {
    this.template = _.template($('#embedly-template').html())

    this.$el.html(this.template(this.data))

    this.player = new playerjs.Player(this.$('iframe.embedly-embed')[0])
    this.player.mute()

    this.player.on('ready', () => {
      this.trigger('loaded')

      this.player.getDuration((duration) => {
        console.log(duration)
      })
    })

    return this
  }

  renderPhoto () {
    this.template = _.template($('#embedly-template').html())

    let data = {
      url: this.data.response.url,
      cover: true,
      type: 'image',
      caption: this.data.response.title,
      description: this.data.response.description,
      copyright: ''
    }
    this.mediaView = new MediaPanelView({
      model: new Panel({ data: data })
    })
    this.mediaView.once('loaded', () => this.trigger('loaded'))

    this.$el.html(this.mediaView.render().el)

    return this
  }

  renderRich () {
    this.template = _.template($('#embedly-template').html())
    this.$el.html(this.template(this.data))
    this.$('iframe').on('load', () => this.trigger('loaded'))
    return this
  }

  renderLink () {
    this.template = _.template($('#embedly-template-link').html())
    this.$el.html(this.template(this.data))
    this.$('iframe').on('load', () => this.trigger('loaded'))
    return this
  }

  remove () {
    if (this.mediaView) this.mediaView.remove()
    super.remove()
  }
}

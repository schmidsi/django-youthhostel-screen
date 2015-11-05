import $ from 'jquery'
import _ from 'underscore'
import Backbone from 'backbone'
import ui from 'popmotion'

import PanelBaseView from './base-view'

const ITEM_INTERVAL = 10000
const ITEMS_PER_PANEL = 10
const FADE_DURATION = 2000

let NewsItemModel = Backbone.Model.extend({
  defaults: {
    title: '',
    body: '',
    source: '',
    timestamp: '',
    author: ''
  }
})

class NewsItemView extends Backbone.View {
  constructor (options) {
    super(options)

    this.template = _.template($('#news-template').html())
  }

  attributes () {
    return {
      class: 'flex flex-center cover-parent'
    }
  }

  render () {
    this.$el.html(this.template(this.model.toJSON()))

    this.actor = new ui.Actor({
      element: this.el,
      values: {
        opacity: 0,
        y: '-100px'
      }
    })

    this.actor.start(new ui.Tween({
      values: {
        opacity: 1,
        y: 0
      },
      duration: FADE_DURATION
    }))
    return this
  }

  remove (options) {
    options.animated = (options.animated || false)

    if (options.animated && this.actor) {
      this.actor.start(new ui.Tween({
        values: {
          opacity: 0,
          y: '5rem'
        },
        duration: FADE_DURATION
      })).then(() => super.remove())
    } else {
      super.remove()
    }
  }
}

export default class NewsView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.ticker = this.data.ticker.slice(0, ITEMS_PER_PANEL)
    this.remaining = ITEMS_PER_PANEL * (ITEM_INTERVAL / 1000)
    this.currentItemIndex = 0
    this.currentItemView = new NewsItemView()
    this.nextItemView = new NewsItemView()
  }

  attributes () {
    let attributes = super.attributes()

    attributes.class = `news`

    return attributes
  }

  renderNextItem () {
    this.nextItemView = new NewsItemView({
      model: new NewsItemModel(this.ticker[ this.currentItemIndex ])
    })

    this.$el.append(this.nextItemView.render().el)
    this.currentItemView.remove({ animated: true })
    this.currentItemView = this.nextItemView

    this.currentItemIndex++

    if (this.currentItemIndex >= this.ticker.length) {
      this.trigger('finished')
    }
  }

  render () {
    this.interval = window.setInterval(this.renderNextItem.bind(this), ITEM_INTERVAL)
    this.renderNextItem()
    this.trigger('loaded')
    return this
  }

  remove () {
    window.clearInterval(this.interval)
    super.remove()
  }

  updateProgress () {
    this.remaining--
    let progress = 1 - this.remaining / (ITEMS_PER_PANEL * (ITEM_INTERVAL / 1000))
    if (progress >= 1) this.trigger('finished')
    this.trigger('progress', progress)
  }
}

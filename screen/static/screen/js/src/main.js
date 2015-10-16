import _ from 'underscore'
import $ from 'jquery'
import Backbone from 'backbone'

window.jQuery = window.$ = $

let Panel = Backbone.Model.extend({
  defaults: {
    type: 'undefined',
    ordering: 0,
    priority: 0,
    morning: false,
    noon: false,
    afternoon: false,
    evening: false,
    night: false,
    data: {},
    duration: 0
  }
})

class Panels extends Backbone.Collection {
  constructor (options) {
    super(options)
    this.model = Panel
    this.comparator = 'ordering'
  }
}

class TextPanelView extends Backbone.View {
  constructor (options) {
    super(options)
    this.template = _.template($('#text-template').html())
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

class MediaPanelView extends Backbone.View {
  constructor (options) {
    super(options)
    this.template = _.template($('#media-template').html())
  }

  render () {
    let data = this.model.toJSON().data
    this.$el.html(this.template(data))
    return this
  }
}

class Router extends Backbone.Router {
  constructor (options) {
    super(options)

    this.routes = {
      ':panel': 'showPanel',
      '*path': 'default'
    }

    this.panels = options.panels
    this.panelIndex = 0

    this._bindRoutes()
  }

  default () {
    this.navigate('0', { trigger: true })
  }

  showPanel (panelIndex = 0) {
    this.panelIndex = parseInt(panelIndex, 10)

    let model = this.panels.at(panelIndex)
    let view = null // superscoping

    switch (model.get('type')) {
      case 'text':
        view = new TextPanelView({ model: model })
        break
      case 'mediendatei':
        view = new MediaPanelView({ model: model })
        break
      default:
        console.warn('no template defined for', this.model.get('type'))
        return this
    }

    $('[data-hook~=panel-hook').html(view.render().el)
  }

  next () {
    this.navigate((this.panelIndex + 1).toString(), { trigger: true })
  }

  prev () {
    this.navigate((this.panelIndex - 1).toString(), { trigger: true })
  }
}

// DOMLoaded
$(() => {
  let panels = new Panels()

  panels.reset(window.ScreenData.main)

  let router = new Router({ panels: panels })

  Backbone.history.start()

  $(window).on('keyup', (e) => {
    if (e.keyCode === 39) {
      router.next()
    } else if (e.keyCode === 37) {
      router.prev()
    }
  })
})

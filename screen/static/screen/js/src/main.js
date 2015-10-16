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

class PanelView extends Backbone.View {
  constructor (options) {
    super(options)

    switch (this.model.get('type')) {
      case 'text':
        this.template = _.template($('#text-template').html())
        break
      default:
        console.warn('no template defined for', this.model.get('type'))
    }
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

class Router extends Backbone.Router {
  constructor (options) {
    super(options)

    this.routes = {
      ':panel': 'showPanel',
      '*path': 'default'
    }

    this.panels = options.panels

    this._bindRoutes()
  }

  default () {
    this.navigate('0', { trigger: true })
  }

  showPanel (panel = 0) {
    $('[data-hook~=panel-hook').html(
      (new PanelView({ model: this.panels.at(panel) })).render().el
    )
  }
}

// DOMLoaded
$(() => {
  let panels = new Panels()

  panels.reset(window.ScreenData.main)

  let router = new Router({ panels: panels })

  Backbone.history.start()
})

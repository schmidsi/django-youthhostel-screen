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

class PanelBaseView extends Backbone.View {
  attributes () {
    return {
      'data-hook': 'panel-hook'
    }
  }
}

class TextPanelView extends PanelBaseView {
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

class MediaPanelView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.templateMeta = _.template($('#media-meta').html())

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

    if (data.cover) {
      attributes.style = `background-image: url(${ data.url })`
    }

    return attributes
  }

  render () {
    let data = this.model.toJSON().data

    if (data.caption || data.description || data.copyright) {
      data.meta = this.templateMeta(data)
    } else {
      data.meta = ''
    }

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
    this.panelIndex = parseInt(panelIndex, 10) % (this.panels.length)

    while (this.panelIndex < 0) {
      this.panelIndex = this.panels.length - panelIndex - 2
    }

    this.navigate(this.panelIndex.toString())

    let model = this.panels.at(this.panelIndex)
    let view = null // superscoping

    switch (model.get('type')) {
      case 'text':
        view = new TextPanelView({ model: model })
        break
      case 'mediendatei':
        view = new MediaPanelView({ model: model })
        break
      default:
        console.warn('no template defined for', model.get('type'))
        return this
    }

    $('[data-hook~=panel-hook]').replaceWith(view.render().el)
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

import _ from 'underscore'
import $ from 'jquery'
import Backbone from 'backbone'
import ui from 'popmotion'

window.jQuery = window.$ = $

const FADE_DURATION = 1000
const GALLERY_INTERVAL = 10000

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
  constructor (options) {
    super(options)

    // if true, it must fire a 'loaded' event after all assets are loaded
    this.loadAssets = false
  }

  attributes () {
    return {
      'data-hook': 'panel-hook'
    }
  }

  fixDimensions () {
    this.rect = this.el.getBoundingClientRect()
    this.rect.position = 'absolute'
    this.initialStyle = this.$el.attr('style')
    this.$el.css(this.rect)
  }

  releaseDimensions () {
    this.$el.attr('style', this.initialStyle)
    this.$el.css('opacity', 1)
  }

  hide () {
    this.$el.css('opacity', 0)
  }

  fadeRemove (onComplete = () => {}) {
    this.fixDimensions()

    let actor = new ui.Actor({
      element: this.el,
      values: {
        opacity: 1
      }
    })

    actor.start(new ui.Tween({
      values: {
        opacity: 0
      },
      duration: FADE_DURATION,
      onComplete: () => {
        this.remove()
        onComplete()
      }
    }))
  }

  fadeIn (onComplete = () => {}) {
    this.fixDimensions()

    let actor = new ui.Actor({
      element: this.el,
      values: {
        opacity: 0
      }
    })

    actor.start(new ui.Tween({
      values: {
        opacity: 1
      },
      duration: FADE_DURATION,
      onComplete: () => {
        this.releaseDimensions()
        onComplete()
      }
    }))
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

class ImageGalleryView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.currentImageIndex = 0
    this.mediafiles = this.model.get('data').mediafiles
    this.subview = undefined
  }

  renderNextImage () {
    let subPanel = new Panel({ data: this.mediafiles[this.currentImageIndex] })

    if (this.subview) {
      this.subview.remove()
      delete this.subview
    }

    this.subView = new MediaPanelView({ model: subPanel })

    this.$el.html(this.subView.render().el)

    this.currentImageIndex = (this.currentImageIndex + 1) % this.mediafiles.length

    return this
  }

  render () {
    this.interval = window.setInterval(this.renderNextImage.bind(this), GALLERY_INTERVAL)

    return this.renderNextImage()
  }

  remove () {
    super.remove()

    window.clearInterval(this.interval)
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

    this.currentView = new PanelBaseView({ el: $('[data-hook~=panel-hook]').get() })
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
    let newView

    switch (model.get('type')) {
      case 'text':
        newView = new TextPanelView({ model: model })
        break
      case 'mediendatei':
        newView = new MediaPanelView({ model: model })
        break
      case 'simple image gallery':
        newView = new ImageGalleryView({ model: model })
        break
      default:
        console.warn('no template defined for', model.get('type'))
        return this
    }

    this.currentView.$el.after(newView.render().el)
    newView.hide()

    if (newView.loadAssets) {
      newView.once('loaded', () => newView.fadeIn())
    } else {
      newView.fadeIn()
    }
    this.currentView.fadeRemove()
    this.currentView = newView
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

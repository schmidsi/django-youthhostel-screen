import $ from 'jquery'
import Backbone from 'backbone'

import PanelBaseView from './panels/base-view'
import TextPanelView from './panels/text-view'
import MediaPanelView from './panels/media-view'
import ImageGalleryView from './panels/gallery-view'
import EmbedlyView from './panels/embedly-view'
import FacebookView from './panels/facebook-view'
import NewsView from './panels/news-view'

import ProgressView from './progress'

export default class Router extends Backbone.Router {
  constructor (options) {
    super(options)

    this.routes = {
      ':panel': 'showPanel',
      '*path': 'default'
    }

    this.panels = options.panels
    this.panelIndex = 0

    this._bindRoutes()

    this.$hook = $('[data-hook~=panel-hook]')
    this.currentView = new PanelBaseView()
    this.newView = new PanelBaseView()
    this.progress = new ProgressView({ el: $('[data-hook~=progress]').get() })

    this.started = true
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

    switch (model.get('type')) {
      case 'text':
        this.newView = new TextPanelView({ model: model })
        break
      case 'mediendatei':
        this.newView = new MediaPanelView({ model: model })
        break
      case 'simple image gallery':
        this.newView = new ImageGalleryView({ model: model })
        break
      case 'externer inhalt':
        this.newView = new EmbedlyView({ model: model })
        break
      case 'facebook image posts':
        this.newView = new FacebookView({ model: model })
        break
      case 'news panel':
        this.newView = new NewsView({ model: model })
        break
      default:
        console.warn('no template defined for', model.get('type'))
        return this
    }

    if (this.started) this.bindNewView()

    this.newView.once('loaded', () => {
      this.newView.fadeIn()
      this.currentView.fadeRemove()
      this.currentView = this.newView
    })

    this.$hook.append(this.newView.render().el)
    this.newView.hide()
  }

  bindNewView () {
    this.newView.on('progress', this.progress.update.bind(this.progress))
    this.newView.on('finished', this.next.bind(this))
    this.newView.on('loaded', this.progress.reset.bind(this.progress))
  }

  unbindNewView () {
    this.newView.off('progress')
    this.newView.off('finished')
    this.newView.off('loaded')
  }

  next () {
    this.navigate((this.panelIndex + 1).toString(), { trigger: true })
  }

  prev () {
    this.navigate((this.panelIndex - 1).toString(), { trigger: true })
  }

  startStop () {
    if (this.started) {
      this.progress.reset()
      this.started = false
      this.unbindNewView()
    } else {
      this.started = true
      this.bindNewView()
    }
  }
}


import $ from 'jquery'
import Backbone from 'backbone'

import PanelBaseView from './panels/base-view'
import TextPanelView from './panels/text-view'
import MediaPanelView from './panels/media-view'
import ImageGalleryView from './panels/gallery-view'
import EmbedlyView from './panels/embedly-view'

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
      case 'externer inhalt':
        newView = new EmbedlyView({ model: model })
        break
      default:
        console.warn('no template defined for', model.get('type'))
        return this
    }

    this.$hook.append(newView.render().el)
    newView.hide()

    if (newView.loadAssets) {
      newView.once('loaded', () => {
        newView.fadeIn()
        this.currentView.fadeRemove()
        this.currentView = newView
      })
    } else {
      newView.fadeIn()
      this.currentView.fadeRemove()
      this.currentView = newView
    }
  }

  next () {
    this.navigate((this.panelIndex + 1).toString(), { trigger: true })
  }

  prev () {
    this.navigate((this.panelIndex - 1).toString(), { trigger: true })
  }
}


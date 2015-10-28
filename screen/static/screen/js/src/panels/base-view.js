import Backbone from 'backbone'
import ui from 'popmotion'

const FADE_DURATION = 2000

export default class PanelBaseView extends Backbone.View {
  constructor (options) {
    super(options)

    // if true, it must fire a 'loaded' event after all assets are loaded
    this.loadAssets = false
  }

  attributes () {
    return {}
  }

  hide () {
    this.$el.css('opacity', 0)
  }

  fadeRemove (onComplete = () => {}) {
    let actor = new ui.Actor({
      element: this.el,
      values: {
        opacity: 1
      }
    })

    return actor.start(new ui.Tween({
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
    let actor = new ui.Actor({
      element: this.el,
      values: {
        opacity: 0
      }
    })

    return actor.start(new ui.Tween({
      values: {
        opacity: 1
      },
      duration: FADE_DURATION,
      onComplete: () => {
        onComplete()
      }
    }))
  }
}

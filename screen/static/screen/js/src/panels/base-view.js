import Backbone from 'backbone'
import ui from 'popmotion'

const FADE_DURATION = 2000

/*
  Triggers 'loaded', as soon as all assets are loaded. If no assets have to
  be loaded, trigger loaded after rendering
*/
export default class PanelBaseView extends Backbone.View {
  constructor (options) {
    super(options)

    if (this.model) {
      this.data = this.model.toJSON().data
      this.remaining = this.model.get('duration')
      this.updateProgressInterval = window.setInterval(() => {
        this.updateProgress()
      }, 1000)
    }

    this.on('finished', () => {
      window.clearInterval(this.updateProgressInterval)
    })
  }

  attributes () {
    return {}
  }

  hide () {
    this.$el.css('opacity', 0)
  }

  fadeRemove (onComplete = () => {}) {
    window.clearInterval(this.updateProgressInterval)

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

  updateProgress () {
    this.remaining--
    let progress = 1 - this.remaining / this.model.get('duration')
    if (progress >= 1) this.trigger('finished')
    this.trigger('progress', progress)
  }

  remove () {
    window.clearInterval(this.updateProgressInterval)
    super.remove()
  }
}

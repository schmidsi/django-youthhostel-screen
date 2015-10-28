import Backbone from 'backbone'
import ui from 'popmotion'

const STEP_DURATION = 1000

export default class ImageGalleryView extends Backbone.View {
  constructor (options) {
    super(options)

    this.actor = new ui.Actor({
      element: this.el,
      values: {
        width: 0
      }
    })
  }

  reset () {
    this.update(0, 0)
  }

  update (progress, duration = STEP_DURATION) {
    this.actor.start(new ui.Tween({
      values: {
        width: (100 * progress) + '%'
      },
      ease: 'linear',
      duration: duration
    }))
  }
}

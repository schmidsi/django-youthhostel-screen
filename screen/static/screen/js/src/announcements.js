import Backbone from 'backbone'
import ui from 'popmotion'

import { Panel } from './panels/base-model'

const ANIMATION_DURATION = 1000

export default class AnnouncementsView extends Backbone.View {
  constructor (options) {
    super(options)

    this.model = new Panel()
    this.timeout = undefined
  }

  render () {
    this.model = this.collection.getRandomized(this.model)

    this.$el.html(this.model.get('data').announcement)

    let actor = new ui.Actor({
      element: this.el,
      values: {
        top: 0,
        height: 0,
        opacity: 0
      }
    })

    actor.start(new ui.Tween({
      values: {
        height: this.el.scrollHeight,
        opacity: 1
      },
      duration: ANIMATION_DURATION
    }))
    .then(() => {
      this.timeout = window.setTimeout(() => {
        actor.start(new ui.Tween({
          values: {
            height: 0,
            opacity: 0
          },
          duration: ANIMATION_DURATION
        }))
        .then(() => {
          this.render()
        })
      }, this.model.get('duration') * 1000)
    })

    return this
  }
}

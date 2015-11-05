import _ from 'underscore'
import Backbone from 'backbone'

export let Panel = Backbone.Model.extend({
  defaults: {
    type: 'undefined',
    ordering: -1,
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

export class ScreenCollection extends Backbone.Collection {
  constructor (options) {
    super(options)
    this.model = Panel
    this.comparator = 'ordering'
  }

  getTimeslot (now = new Date()) {
    let hour = now.getHours()
    let minute = now.getMinutes()

    if (hour >= 23 || hour < 6) {
      return 'night'
    } else if (hour >= 6 && hour < 10) {
      return 'morning'
    } else if (hour >= 10 && hour <= 13 && minute <= 30) {
      return 'noon'
    } else if (hour >= 13 && hour < 17) {
      return 'afternoon'
    } else if (hour >= 17 && hour < 23) {
      return 'evening'
    } else {
      console.warn('Can not determine timeslot', hour, minute)
      return false
    }
  }

  getRandomized (currentModel) {
    let filter = {}
    filter[this.getTimeslot()] = true

    let timeslotted = _.reject(this.where(filter), (item) => {
      return item.get('ordering') === currentModel.get('ordering')
    })

    let prioritySum = _.reduce(timeslotted, (memo, panel, index) => {
      return memo + panel.get('priority')
    }, 0)

    let pointer = Math.random() * prioritySum
    let counter = 0
    let item = _.find(timeslotted, (panel) => {
      counter += panel.get('priority')
      return (pointer < counter)
    })

    return item
  }
}

export class Panels extends ScreenCollection {
}

export class Announcements extends ScreenCollection {
}

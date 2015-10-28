import Backbone from 'backbone'

export let Panel = Backbone.Model.extend({
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

export class Panels extends Backbone.Collection {
  constructor (options) {
    super(options)
    this.model = Panel
    this.comparator = 'ordering'
  }
}

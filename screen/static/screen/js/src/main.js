import $ from 'jquery'
import Backbone from 'backbone'

import { Panels } from './panels/base-model'
import Router from './router'

window.jQuery = window.$ = $

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

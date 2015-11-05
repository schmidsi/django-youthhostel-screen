import $ from 'jquery'
import Backbone from 'backbone'

import { Panels, Announcements } from './panels/base-model'
import AnnouncementsView from './announcements'
import Router from './router'

window.jQuery = window.$ = $

// DOMLoaded
$(() => {
  let panels = new Panels()
  let announcements = new Announcements()

  panels.reset(window.ScreenData.main)
  announcements.reset(window.ScreenData.announcements)

  let router = new Router({
    panels: panels,
    announcements: announcements
  })

  let announcementsView = new AnnouncementsView({
    el: $('[data-hook~=announcements]').get(),
    collection: announcements
  })

  announcementsView.render()

  Backbone.history.start()

  $(window).on('keyup', (e) => {
    if (e.keyCode === 39) {
      router.next()
    } else if (e.keyCode === 37) {
      router.prev()
    } else if (e.keyCode === 32) {
      router.startStop()
    } else if (e.keyCode === 38 || e.keyCode === 40) {
      router.showRandomPanel()
    }
  })
})

import $ from 'jquery'

import PanelBaseView from './base-view'
import ImageGalleryView from './gallery-view'
import { Panel } from './base-model'

export default class FacebookView extends PanelBaseView {
  constructor (options) {
    super(options)
  }

  render () {
    window.clearInterval(this.updateProgressInterval)

    $.getJSON(`https://graph.facebook.com/${ this.data.user }/photos/uploaded`, {
      fields: 'images,name',
      access_token: '159457810754902|UqvcQEszzDvlLlft85FtuP2LWYo'
    })
    .then((response, status, xhr) => {
      let gallery = { mediafiles: [] }

      response.data.slice(0, 5).forEach(photo => {
        gallery.mediafiles.push({
          url: photo.images[0].source,
          type: 'image',
          cover: true,
          copyright: null,
          description: photo.name,
          caption: `facebook.com/${ this.data.user }`
        })
      })

      this.subview = new ImageGalleryView({
        model: new Panel({ data: gallery })
      })

      this.subview.on('loaded', () => this.trigger('loaded'))
      this.subview.on('progress', (progress) => this.trigger('progress', progress))
      this.subview.on('finished', () => this.trigger('finished'))

      this.$el.html(this.subview.render().el)
    })

    return this
  }

  remove () {
    this.subview.remove()
    super.remove()
  }
}

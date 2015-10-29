import PanelBaseView from './base-view'
import MediaPanelView from './media-view'
import { Panel } from './base-model'

const GALLERY_INTERVAL = 10000

export default class ImageGalleryView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.currentImageIndex = 0
    this.mediafiles = this.data.mediafiles
    this.subview = undefined
  }

  renderNextImage () {
    if (this.currentImageIndex >= this.mediafiles.length) {
      return this.trigger('finished')
    }

    let newView = new MediaPanelView({
      model: new Panel({ data: this.mediafiles[this.currentImageIndex] })
    })

    newView.once('loaded', () => newView.fadeIn(() => {
      if (this.subview) this.subview.fadeRemove()
      this.subview = newView
      this.trigger('loaded')
      this.remaining = (GALLERY_INTERVAL / 1000)
    }))

    this.$el.append(newView.render().el)
    newView.hide()

    this.currentImageIndex = this.currentImageIndex + 1

    return this
  }

  render () {
    this.interval = window.setInterval(this.renderNextImage.bind(this), GALLERY_INTERVAL)

    return this.renderNextImage()
  }

  updateProgress () {
    this.remaining--
    let progress = 1 - (this.remaining / (GALLERY_INTERVAL / 1000))

    console.log(progress)
    this.trigger('progress', progress)
  }

  remove () {
    super.remove()
    window.clearInterval(this.interval)
  }
}

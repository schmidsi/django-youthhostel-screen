import PanelBaseView from './base-view'
import MediaPanelView from './media-view'
import { Panel } from './base-model'

const GALLERY_INTERVAL = 10000

export default class ImageGalleryView extends PanelBaseView {
  constructor (options) {
    super(options)

    this.currentImageIndex = 0
    this.mediafiles = this.model.get('data').mediafiles
    this.subview = undefined
  }

  renderNextImage () {
    let newView = new MediaPanelView({
      model: new Panel({ data: this.mediafiles[this.currentImageIndex] })
    })

    this.$el.append(newView.render().el)
    newView.hide()
    newView.once('loaded', () => newView.fadeIn())
    if (this.subview) this.subview.fadeRemove()
    this.subview = newView

    this.currentImageIndex = (this.currentImageIndex + 1) % this.mediafiles.length

    return this
  }

  render () {
    this.interval = window.setInterval(this.renderNextImage.bind(this), GALLERY_INTERVAL)

    return this.renderNextImage()
  }

  remove () {
    super.remove()

    window.clearInterval(this.interval)
  }
}

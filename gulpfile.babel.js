import autoprefixer from 'autoprefixer'
import browserSync from 'browser-sync'
import cssnext from 'cssnext'
import foreman from 'gulp-foreman'
import gulp from 'gulp'
import postcss from 'gulp-postcss'


const paths = {
  css: {
    src: './screen/static/screen/css/src/**/*.css',
    dest: './screen/static/screen/css/dist/'
  },
  html: {
    watch: './screen/templates/**/*.html'
  }
}


gulp.task('foreman', () => {
  foreman({
    procfile: 'Procfile.dev'
  })
})


gulp.task('browser-sync', ['foreman'], () => {
  return browserSync.init({
    proxy: 'http://localhost:2000',
    port: 8000,
    open: false
  })
})


gulp.task('browser-reload', () => {
  return browserSync.reload()
})


gulp.task('css', () => {
  return gulp.src(paths.css.src)
    .pipe( postcss([autoprefixer, cssnext]) )
    .pipe( gulp.dest(paths.css.dest) )
    .pipe( browserSync.reload({stream: true}) )
})


gulp.task('default', ['css', 'foreman', 'browser-sync'], () => {
  gulp.watch(paths.css.src, ['css'])
  gulp.watch(paths.html.watch, ['browser-reload'])
})

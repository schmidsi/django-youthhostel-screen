import gulp from 'gulp'
import foreman from 'gulp-foreman'
import browserSync from 'browser-sync'


gulp.task('foreman', () => {
  foreman({
    procfile: 'Procfile.dev'
  })
})


gulp.task('browser-sync', ['foreman'], () => {
  browserSync.init({
    proxy: 'http://localhost:2000',
    port: 8000,
    open: false
  })
})


gulp.task('default', ['foreman', 'browser-sync'])

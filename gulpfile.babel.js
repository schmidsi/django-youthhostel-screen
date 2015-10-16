import autoprefixer from 'autoprefixer'
import babelify from 'babelify'
import browserSync from 'browser-sync'
import browserify from 'browserify'
import cssnext from 'cssnext'
import foreman from 'gulp-foreman'
import gulp from 'gulp'
import postcss from 'gulp-postcss'
import through2 from 'through2'


const paths = {
  css: {
    src: './screen/static/screen/css/src/**/*.css',
    dest: './screen/static/screen/css/dist/'
  },
  html: {
    watch: './screen/templates/**/*.html'
  },
  js: {
    src: './screen/static/screen/js/src/main.js',
    watch: './screen/static/screen/js/src/**/*.js',
    dest: './screen/static/screen/js/dist/',
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


gulp.task('browserify', () =>{
  return gulp.src(paths.js.src)
    .pipe( through2.obj( (file, enc, next) => {
      return browserify(file.path, {debug: true})
        .transform( babelify )
        .bundle( (err, res) => {
          file.contents = res
          next(err, file)
        })
    }))
    .pipe( gulp.dest(paths.js.dest) )
})


gulp.task('default', ['css', 'browserify', 'foreman', 'browser-sync'], () => {
  gulp.watch(paths.css.src, ['css'])
  gulp.watch(paths.html.watch, ['browser-reload'])
  gulp.watch(paths.js.watch, ['browserify', 'browser-reload'])
})

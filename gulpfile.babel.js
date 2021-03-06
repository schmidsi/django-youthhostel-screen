import babelify from 'babelify'
import browserSync from 'browser-sync'
import browserify from 'browserify'
import cssnext from 'cssnext'
import debowerify from 'debowerify'
import foreman from 'gulp-foreman'
import gulp from 'gulp'
import postcss from 'gulp-postcss'
import shell from 'gulp-shell'
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
    dest: './screen/static/screen/js/dist/'
  }
}

gulp.task('kill-python', shell.task(['killall python'], { ignoreErrors: true }))

gulp.task('foreman', ['kill-python'], () => {
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

gulp.task('browser-reload', ['browserify'], () => {
  return browserSync.reload()
})

gulp.task('css', () => {
  return gulp.src(paths.css.src)
    .pipe(postcss([ cssnext() ]))
    .pipe(gulp.dest(paths.css.dest))
    .pipe(browserSync.reload({ stream: true }))
})

gulp.task('browserify', () => {
  return gulp.src(paths.js.src)
    .pipe(through2.obj((file, enc, next) => {
      return browserify(file.path, { debug: true })
        .transform(babelify)
        .transform(debowerify)
        .bundle((err, res) => {
          file.contents = res || null
          next(err, file)
        })
    }))
    .pipe(gulp.dest(paths.js.dest))
})

gulp.task('default', ['css', 'browserify', 'foreman', 'browser-sync'], () => {
  gulp.watch(paths.css.src, ['css'])
  gulp.watch(paths.html.watch, ['browser-reload'])
  gulp.watch(paths.js.watch, ['browserify', 'browser-reload'])
})

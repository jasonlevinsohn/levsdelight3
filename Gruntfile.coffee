module.exports = (grunt) ->
    grunt.initConfig
        pkg: grunt.file.readJSON('package.json')

        coffee:
            main:
                expand: true # Set's a set of common options http://gruntjs.com/configuring-tasks
                flatten: false # removes all parts of the generated dest paths
                cwd: 'levsdelight_com/static/js' # All src matches are relative to this path (ie. current working directory)
                src: ['**/*.coffee']
                dest: 'levsdelight_com/static/js'
                ext: '.coffee.js' # Generated file extension

        sass:
            main:
                options:
                    style: 'expanded'
                    sourcemap: true
                    compass: true
                files: [{
                    expand: true,
                    cwd: 'levsdelight_com/static/scss'
                    src: ['*.scss']
                    dest: 'levsdelight_com/static/css'
                    ext: '.scss.css'
                }]
                


        _watch_:
            options:
                nocase: true # Not sure if this is cap case or if it sorts the outputted generated files
            coffee:
                files: ['levsdelight_com/static/js/**/*.coffee']
                tasks: ['coffee:main']
            sass:
                files: ['levsdelight_com/static/scss/**/*.scss']
                tasks: ['sass:main']


        grunt.loadNpmTasks 'grunt-contrib-watch'
        grunt.loadNpmTasks 'grunt-contrib-coffee'
        grunt.loadNpmTasks 'grunt-contrib-sass'

        grunt.registerTask 'default', ['coffee:main', 'sass:main']
        grunt.registerTask 'build', ['coffee:main']
        
        grunt.renameTask 'watch', '_watch_'
        grunt.registerTask 'watch', ['default', '_watch_']



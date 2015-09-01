module.exports = (grunt) ->
    grunt.initConfig(
        pkg: grunt.file.readJSON('package.json')
        coffee:
            files:
                src: ['neatapps/src/coffee/**/*.coffee']
                dest: 'static/apps/neatapps/src/js/script.js'
    )
    
    grunt.loadNpmTasks('grunt-contrib-coffee')
    
    grunt.registerTask('default', ['coffee'])

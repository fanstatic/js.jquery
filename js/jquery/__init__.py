from fanstatic import Library, ResourceInclusion

library = Library('jquery', 'resources')

jquery = ResourceInclusion(library, 'jquery.js', minified='jquery.min.js')

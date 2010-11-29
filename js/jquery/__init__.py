from fanstatic import Library, ResourceInclusion

library = Library('jquery', 'resources')

jquery = ResourceInclusion(library, 'jquery-1.4.3.js', minified='jquery-1.4.3.min.js')

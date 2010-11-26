from fanstatic import Library, ResourceInclusion

jquery_lib = Library('jquery_lib', 'resources')

jquery = ResourceInclusion(jquery_lib, 'jquery-1.4.3.js', minified='jquery-1.4.3.min.js')

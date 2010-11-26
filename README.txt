js.jquery
*********

Introduction
============

This library packages jQuery_ for `fanstatic`_. It is aware of jQuery's
structure and different modes (normal, minified).

.. _`fanstatic`: http://fanstatic.org
.. _jQuery: http://jquery.com/

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.jquery``) are published to some URL.

The package has already been integrated for Grok_ and Zope 3. If you depend
on the `zope.fanstatic`_ package in your ``setup.py``, the above example
should work out of the box.

.. _`zope.fanstatic`: http://pypi.python.org/pypi/zope.fanstatic
.. _Grok: http://grok.zope.org


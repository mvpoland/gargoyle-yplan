"""
gargoyle
~~~~~~~~

:copyright: (c) 2010 DISQUS.
:license: Apache License 2.0, see LICENSE for more details.
"""

from django.utils.module_loading import autodiscover_modules

from gargoyle.manager import gargoyle

__version__ = '3.1.0a0'

__all__ = ('gargoyle', 'autodiscover', '__version__')


def autodiscover():
    """
    Auto-discover INSTALLED_APPS' gargoyle modules and fail silently when
    not present. This forces an import on them to register any gargoyle bits they
    may want.
    """
    import gargoyle.builtins  # noqa

    autodiscover_modules("gargoyle")

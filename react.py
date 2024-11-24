#!/usr/bin/python3
""" Python front-end tool for programming unterfaces.
"""
from flask import Flask
from typing import ClassVar


APP: Flask = Flask()
docfile: str = "./index.html"

# Router Function #
#-----------------#
def Route(path: str, component: str) -> Response:
    APP.use


# Pre-defined Components (Samples) #
#----------------------------------#

def Link(
    to: str = "/",
    title: str = ""
) -> str:
    """ Returns an hyperlink tag <a> with its 'href' attribute directing
    to the path specified by the parameter 'to'
    and its title attribute assigned to the parameter 'title'
    """
    return f'''<a href="{to}" title="{title}"></a>
    '''

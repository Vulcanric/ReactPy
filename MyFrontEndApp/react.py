#!/usr/bin/python3
""" Python front-end tool for programming interfaces.
"""
from flask import Flask
from typing import ClassVar, Callable, Union


FlaskAPP: Flask = Flask(__name__)
docfile: str = "./index.html"

# Router Function #
#-----------------#

def Route(path: str, component: Callable) -> None:
    FlaskAPP.use(path, component)


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


# ReactPy server class
class ReactPy:
    """ Instantiate framework
    """
    def __init__(
            self,
            host: str = '0.0.0.0',
            port: int = 4000
        ) -> None:
        """ Initialize reactPy session

        Configuration:
        --------------
        host (str, def=0.0.0.0)
        port (int, def=4000)

        Examples:
        ---------
        react = ReactPy()
        react.run(host='127.0.0.1', port=4003)
              OR
        react = ReactPy(host='127.0.0.1', port=4001)
        react.run()
              OR
        react = ReactPy()
        react.config['host'] = '127.0.0.1',
        react.config['port'] = 4002
        react.run()
        """
        self.__host: str = host
        self.__port: int = port
        self.__config: Dict[str, Union[str, int]] = {
            "host": self.__host,
            "port": self.__port
        }

    def config(self):
        return self.__config

    def run(
            self,
            host: str = config().get('host'),
            port: int = config().get('port')
        ) -> None:
        """ Run the ReactPy App
        """
        FlaskAPP.run(host=host, port=port)

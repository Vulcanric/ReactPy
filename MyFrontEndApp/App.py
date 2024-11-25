#!/usr/bin/python3
""" Main Application file
"""
from react import ReactPy
from react import Route

from pages.HomePage import HomePage
from pages.AboutPage import AboutPage


app = ReactPy()
app.config['host'] = '0.0.0.0'
app.config['port'] = 4001


Route('/', HomePage)
Route('/info', AboutPage)

if __name__ == "__main__":
    app.run()

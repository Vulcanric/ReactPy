from components.TabulatedInfo import TabulatedInfo

def AboutCard():
    """Card displaying informations on React.py
    """
    return f'''
    <div>
      <h1>React.py</h1>
      <p>React.py is a Python tool built for developing robust and efficient front-end interfaces, easily with Python.
      </p>
      <hr />
      <table>
        {TabulatedInfo()}
      </table>
    </div>
    '''

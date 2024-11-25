from components.AboutCard import AboutCard

def AboutPage():
    """ Tells the Stranger about React.py """
    return f'''
<!DOCTYPE html>
<html lang="en-GB">
  <!-- Head Tag -->
  <head>
    <title>Eric React App</>
  </head>

  <!-- Body Tag -->
  <body>
    <!-- Start of document -->
    <div id="root">
    {AboutCard()}
    </div>
  </body>                                      </html>
    '''

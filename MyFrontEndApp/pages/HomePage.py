from components.WelcomeCard import WelcomeCard

def HomePage():
    """ Apps home page """
    return f'''
<!DOCTYPE html>
<html lang="en-GB">
  <!-- Head Tag -->
  <head>
    <title>Eric ReactPy App</>                     </head>
                                                 <!-- Body Tag -->
  <body>
    <!-- Start of document -->
    <div id="root">
    {WelcomeCard()}
    </div>
  </body>                                      </html>
    '''

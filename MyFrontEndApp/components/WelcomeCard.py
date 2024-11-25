from react import Link

def WelcomeCard():
    """ Welcome The Stranger """
    return f'''
    <div>
        <h1>
            Hello Stranger
        </h1>
        <h2>
            Welcome to ReactPy
        </h2>
        <p>Follow me and I will show you around and tell you about it ⟩⟩ </p>
        {
        Link(
            to="/info",
            title="Tell me about react.py"
        )
        }
    </div>
    '''

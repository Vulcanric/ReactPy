def TabulatedInfo():
    more_info = {
            "Date of Creation": "Mon 25th, Nov 2024",
            "Written By": "John Eric",
            "Language": "Python"
    }
    table = ""

    for row in zip(more_info.keys, more_info.values):
        table += '''
        <tr>
        '''
        for data in row:
            table += f'''
            <td>{data}</td>
            '''
        table += '''
        </tr>
        '''

    return table

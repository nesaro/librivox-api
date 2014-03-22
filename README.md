librivox-api
============

Python librivox API


USAGE
=====

    from librivox import librivox
    ablist = librivox.search(author="Dumas")
    ablist[0]['title']
    >>> 'Count of Monte Cristo'
    librivox.retrieve_author(431)
    >>> [{'dob': '1802', 'first_name': 'Alexandre', 'last_name': 'Dumas', 'id': '431', 'dod': '1870'}]



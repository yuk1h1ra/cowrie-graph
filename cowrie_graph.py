# -*- coding: utf-8 -*-

from bottle import route, run, template

@route('/cowrie_graph')
def cowrie_graph():
    return template("cowrie_graph")

run(host='localhost', port=8080, debug=True, reloader=True)

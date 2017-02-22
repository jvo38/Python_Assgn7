from django.http import HttpResponse
import sqlite3

def index(request):
    db = sqlite3.connect('freebsd_fortunes_clean.sl3')
    c = db.cursor()
    p = c.execute('select aphorism from fortunes order by random() limit 1')
    return HttpResponse(p)

    
    

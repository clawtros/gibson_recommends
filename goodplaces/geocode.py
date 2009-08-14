import urllib
 
api = 'http://maps.google.com/maps/geo?%s'
 
def reverse_geocode(lat, long):
    params = urllib.urlencode(
        {'ll':','.join([str(lat), str(long)]), 'output':'csv'}
    )
    fp = urllib.urlopen(api % params)
    data = fp.read().split(',')
    return { 
        'status' : data[0],
        'accuracy' : data[1],
        'address' :','.join(data[2:]),
        }
 
def geocode(address):
    params = urllib.urlencode({'q': address, 'output': 'csv'})
    fp = urllib.urlopen(api %params)
    data = fp.read().split(',')
    return { 
        'status' : data[0],
        'accuracy' : data[1],
        'latitude' : data[2],
        'longitude' : data[3],
        }

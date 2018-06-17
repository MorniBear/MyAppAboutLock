from urllib import request

with request.urlopen('http://127.0.0.1:8000/') as f:
    data = f.read()
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))
    if data.decode('utf-8') is '1':
        print("1")

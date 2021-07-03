import xmlrpc.client
url = 'http://localhost:8069'
db = 'misamisa'
username = 'mailovemisa'
password = 'mailovemisa'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print('details...', version)

uid = common.authenticate(db, username, password, {})
print(uid)

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))
isRead = models.execute_kw(db, uid, password, 'res.partner', 'check_access_rights', [
    'read'], {'raise_exception': False})
print(isRead)

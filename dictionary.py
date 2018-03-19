dictA={'nama1':'Jane Doe','nama2':'John Smith','nama3':'Bob Stone',
    'telp1':'+27 555 5379','telp2':'+27 555 6254','telp3':'+27 555 5689'}
print '\tData Nomor Telp'
print '--------------------------------'
print '|    Name    | Telphone Number | '
print '--------------------------------'
print '|',dictA['nama1'],'  |',dictA['telp1'],'   |','\n','|',dictA['nama2'],'|',dictA['telp2'],'   |','\n','|',dictA['nama3'],' |',dictA['telp3'],'   |'
print '-------------------------------- '

dictA['telp1']='+27 555 1024'
print '\n\tUbah No Telp Jane      '
print '--------------------------------'
print '|    Name    | Telphone Number | '
print '--------------------------------'
print '|',dictA['nama1'],'  |',dictA['telp1'],'   |','\n','|',dictA['nama2'],'|',dictA['telp2'],'   |','\n','|',dictA['nama3'],' |',dictA['telp3'],'   |'
print '--------------------------------'

dictA['nama4']='Anna Cooper'
dictA['telp4']='+27 555 3237'
print '\n       Menambah Data Baru       '
print '---------------------------------'
print '|    Name     | Telphone Number | '
print '---------------------------------'
print '|',dictA['nama1'],'   |',dictA['telp1'],'   |','\n','|',dictA['nama2'],' |',dictA['telp2'],'   |','\n','|',dictA['nama3'],'  |',dictA['telp3'],'   |','\n','|',dictA['nama4'],'|',dictA['telp4'],'   |'
print '---------------------------------'
print '\nCetak Nomor Telp Bob Stone =',dictA['telp3']

print '\nCetak Semua Key =',dictA.keys()

print '\nCetak Semua Value =',dictA.values()

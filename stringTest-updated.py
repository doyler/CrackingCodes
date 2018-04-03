import time

startTime = time.time()
for trial in range(10000):
  building = ''
  for i in range(10000):
      building += 'x'
print 'String concatenation: ', (time.time() - startTime)

startTime = time.time()
for trial in range(10000):
  building = []
  for i in range(10000):
      building.append('x')
  building = ''.join(building)
print 'List concatenation:   ', (time.time() - startTime)

# http://blog.mclemon.io/python-efficient-string-concatenation-in-python-2016-edition
startTime = time.time()
for trial in range(10000):
  building = ''.join([`num` for num in xrange(10000)])
print 'Inline list comprehension with xrange:   ', (time.time() - startTime)


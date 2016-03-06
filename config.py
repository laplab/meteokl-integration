
# True if server should be executed in debug mode
# False otherwise
serverIsDebug = False

# Port to be used by server
# Server will be accessable at http://localhost:{port number}/ (Example: http://localhost:8888/)
serverPort = 8888

# COM port address where weather station is plugged
# Windows: '\\\\.\\COM{port number}' (Example: '\\\\.\\COM2')
# Linux: '/dev/{port address}' (Example: '/dev/ttyS0' instructions to find address: http://unix.stackexchange.com/a/125261)
workerCOMport = '\\\\.\\COM3'

# Time in seconds worker will be trying to fetch data
workerReadTimeout = 17

# Time in seconds worker will wait until reading data next time
wokerPeriod = 5 * 60
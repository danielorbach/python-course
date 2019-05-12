>>> import rpyc
>>> conn = rpyc.classic.connect('172.16.28.250', 8000)
>>> conn.builtins.print('Hello i am another client')
>>> #remote_file = conn.open
>>> conn.open
>>> conn.builtins.open
>>> #remote_file = conn.builtins.open
>>> conn.modules.os
>>> conn.os
>>> conn.modules.os.getcwd()
>>> home = conn.modules.os.getcwd()
>>> file = conn.builtins.open(home+'/remote_file.txt', 'w')
>>> file.write('text from windows client')
>>> file.close()
>>> file
>>> open('C:\\temp\\test.txt', 'w')
>>> conn.modules.os.system('ipconfig')
>>> conn.modules.os.system('ifconfig')
>>> conn.modules.subprocess
>>> conn.modules
>>> p = conn.modules.subprocess.Popen('ping localhost')
>>> p = conn.modules.subprocess.Popen('/usr/bin/ping localhost')
>>> p = conn.modules.subprocess.Popen(['/usr/bin/ping', 'localhost'])
>>> #p2 = conn.modules.subprocess.Popen(['ping', 'localhost'], stdout=)
>>> import subprocess
>>> p2 = conn.modules.subprocess.Popen(['ping', 'localhost'], stdout=subprocess.PIPE)
>>> p2.stdout.read(1)
>>> p2.stdout.read(100)
>>> p2.stdout.read(100)
>>> p2.stdout.read(100)
>>> subprocess.PIPE
>>> p2.kill()
>>> p2.wait()
>>> p2.communicate()
>>> print(_)
>>> _23
>>> _36
>>> %_36
>>> p
>>> type(p)
>>> def whatsmyid(o):
...     return id(o)
...
>>> import rpyc.utils.classic
>>> remote_whatmyid = rpyc.utils.classic.teleport_function(whatsmyid)
>>> #remote_whatmyid = rpyc.utils.classic.teleport_function(conn, whatsmyid)
>>> remote_whatmyid = rpyc.utils.classic.teleport_function(conn, whatsmyid)
>>> whatsmyid
>>> remote_whatmyid
>>> type(remote_whatmyid)
>>> type(whatsmyid)
>>> remote_whatmyid(1)
>>> remote_whatmyid(2)
>>> remote_whatmyid(3)
>>> remote_whatmyid('asd')
>>> id(1)
>>> id(1)
>>> conn.eval('id(1)')
>>> conn.eval('x = (1)')
>>> conn.eval('x == (1)')
>>> conn.execute('x = (1)')
>>> conn.eval('x == (1)')
>>> conn.eval('x')
>>> type(_)
>>> execute
>>> eval
>>> exec
>>> conn.eval('id(x)')
>>> remote_whatmyid(1)
>>> conn.eval('id(whatsmyid)')
>>> remote_whatmyid
>>> id(remote_whatmyid)
>>> remote_whatmyid(remote_whatmyid)
>>> conn
>>> p
>>> type(p)
>>> p.pid
>>> import threading
>>> def thread_main():
...     import time
...     for i in range(10):
...         print(id(i))
...         time.sleep(1)
...
>>> remote_thread_main = rpyc.utils.classic.teleport_function(conn, thread_main)
>>> t = conn.modules.threading.Thread(target=remote_thread_main)
>>> t
>>> t.start()
>>> t.join()
>>> t = conn.modules.threading.Thread(target=remote_thread_main)
>>> t.start()
>>> t.join()
>>> import socket
>>> client = socket.socket()
>>> server = conn.modules.socket.socket()
>>> server.bind(('0.0.0.0', 8443))
>>> server.listen(1)
>>> def server_func():
...     c, a = server.accept()
...     print(f'client {c}, address: {a}')
...     import time
...     time.sleep(20)
...
>>> server_thread = threading.Thread(target=server_func)
>>> server_thread.start()
>>> client.connect(('172.16.28.250', 8443))
>>> socket.getaddrinfo()
>>> client.close()
>>> %history 1-100 -n -o -p -t "C:\Users\daniel.orbach\Development\orbach\Courses\python-course\lesson-3\ipython.txt"
>>> %history 1-100 -n -o -p -f "C:\Users\daniel.orbach\Development\orbach\Courses\python-course\lesson-3\ipython.txt"
>>> %history 1-100 -p -f "C:\Users\daniel.orbach\Development\orbach\Courses\python-course\lesson-3\ipython.py"

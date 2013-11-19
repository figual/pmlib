import sys, os
def daemonize (stdin='/dev/null', stdout='/tmp/out.txt', stderr='/tmp/err.txt'):
    # Perform first fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit first parent.
    except OSError, e:
        sys.stderr.write("fork #1 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
    # Decouple from parent environment.
    os.chdir("/")
    os.umask(0)
    os.setsid( )
    # Perform second fork.
    try:
        pid = os.fork( )
        if pid > 0:
            sys.exit(0) # Exit second parent.
    except OSError, e:
        sys.stderr.write("fork #2 failed: (%d) %s\n" % (e.errno, e.strerror))
        sys.exit(1)
    # The process is now daemonized, redirect standard file descriptors.
    print "The process is now daemonized, redirect standard file descriptors."

    pid_path = "/var/run/pm_server.pid"
    pid_file = file(pid_path, mode = 'w')
    pid_file.write(str(os.getpid()))
    pid_file.close()

    for f in sys.stdout, sys.stderr: f.flush( )

    si = file(stdin, 'r')
    so = file(stdout, 'a+')
    se = file(stderr, 'a+', 0)
    os.dup2(si.fileno( ), sys.stdin.fileno( ))
    os.dup2(so.fileno( ), sys.stdout.fileno( ))
    os.dup2(se.fileno( ), sys.stderr.fileno( ))

def undaemonize ():
    os.dup2( sys.stdin.fileno( ), sys.stdin.fileno( ))
    os.dup2( sys.stdout.fileno( ), sys.stdout.fileno( ))
    os.dup2( sys.stderr.fileno( ), sys.stderr.fileno( ))

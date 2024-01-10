import socket
import pickle
slady_h = 'localhost'
sparty_p = 8080
srr_scksiri = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srr_scksiri.bind((slady_h, sparty_p))
srr_scksiri.listen(5)
print(f"Server listening on {slady_h}:{sparty_p}...")
def foo(piluvu):
    javab = 0
    for thippu in range(piluvu):
        javab += 2
    return javab
def add(thippu, piluvu):
    return thippu + piluvu
def sort(arrayA):
    return sorted(arrayA)
while True:
    csdf_s, cadd_dfs = srr_scksiri.accept()
    print(f"Connection accepted from {cadd_dfs}")
    sdt = csdf_s.recv(1024)
    rstqsiri = pickle.loads(sdt)
    if rstqsiri['method'] == 'foo':
        javab = foo(rstqsiri['args'][0])
    elif rstqsiri['method'] == 'add':
        javab = add(rstqsiri['args'][0], rstqsiri['args'][1])
    elif rstqsiri['method'] == 'sort':
        javab = sort(rstqsiri['args'][0])
    else:
        javab = "Unknown method"
    rspdhanoosh = {'javab': javab}
    csdf_s.send(pickle.dumps(rspdhanoosh))
    csdf_s.close()

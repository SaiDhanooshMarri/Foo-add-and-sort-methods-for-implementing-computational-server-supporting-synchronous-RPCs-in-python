import socket
import pickle
slady_h = 'localhost'
sparty_p = 8080
def send_request(method, args=[]):
    csdf_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    csdf_s.connect((slady_h, sparty_p))
    rstqsiri = {'method': method, 'args': args}
    csdf_s.send(pickle.dumps(rstqsiri))
    sdt = csdf_s.recv(1024)
    rspdhanoosh = pickle.loads(sdt)
    csdf_s.close()
    return rspdhanoosh['javab']

# Example function calls
theesko=input("Enter FOO value:  ")
theesko=int(theesko)
theesko1=input("Enter the values of add with a comma, example 5,3:     ")
theesko1=theesko1.split(",")
inkatheesko=input("Enter the array for sorting with a comma separated example 3,2,7,4:    ")
inkatheesko=inkatheesko.split(",")
for thippu in range(len(inkatheesko)):
    inkatheesko[thippu]=int(inkatheesko[thippu])
rsf_an,rsd_ad,rss_sr = send_request('foo', [theesko]),send_request('add', [int(theesko1[0]), int(theesko1[1])]),send_request('sort', [inkatheesko])

print("Result of function foo():", rsf_an)
print(f"Result of function add({theesko1[0]}, {theesko1[1]}):", rsd_ad)
print(f"Result of function sort({inkatheesko}):", rss_sr)

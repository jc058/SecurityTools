import socket
from utils import timefunc

# a class is created to contain our functions essential to the tool.
class Scanner:
    # initiates 'ip' and creates a list for the ports to be listed in.
    def __init__(self, ip):
        self.ip = ip
        self.open_ports = []
    
    # function to add the listed ports to the created list.
    def add_port(self, port):
        self.open_ports.append(port)

    # function to loop through the requested ports to include the last port in the range.
    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if self.is_open(port):
                self.add_port(port)

    #creates the connection, sets the timeout time, closes the connection and captures the most common input errors.
    def is_open(self, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        result = s.connect_ex((self.ip, port))
        s.settimeout(0.02)
        # print(result)
        s.close()
        if result == 60:
            print('>>>Please try again')
            main()
        elif result == 65:
            print('>>>Please try again')
            main()
        return result == 0

    # writes the open ports to the file
    def write(self, filepath):
        openport = map(str, self.open_ports)
        with open(filepath, 'w') as f:
            f.write('\n'.join(openport))
    
#captures the time it took to run.
@timefunc

# captures the IP address and calls the functions requred to run the script, write to the file and prints the open 
# ports to the terminal.
def main():
    ip = input('>>>IP address:  ')
    # ip = '172.16.43.130'
    scanner = Scanner(ip)
    scanner.scan(1, 100)
    scanner.write('./open_ports')
    print(scanner.open_ports)



if __name__ == '__main__':
    main()

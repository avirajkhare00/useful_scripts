import socket

s = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
s.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1 ) # Needed to reuse the script after closing, due to network reasons
s.bind(( '127.0.0.1', 8080 ))
s.listen( 1 )

while True:
    client, client_addr = s.accept()

    data = client.recv(4069)
    
    create_file = open("/home/avira/python/post_req.txt", "w")
    create_file.write(data)
    create_file.close()

    client.close()

s.close()

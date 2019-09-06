import serial
import time

kjr = "hello\n"
arr = [[1,0,1,0,1,0],[1,1,0,1,1,0],[1,0,0,1,1,0]]
# bytearray([1,0,1,0,1])
# ,[1,1,0,1,1],[1,0,0,1,1]]

def setup():
    global ser
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = '/dev/cu.usbserial-1420'
    ser.timeout = 0.1
    ser.open()
    ser.reset_input_buffer()


def main():
    while True:
        # ser.write(kjr.encode('utf-8'))
        ser.write(bytearray(arr[1]))
        # ser.write("\n")
        time.sleep(2)

        if(ser.in_waiting):
            lmao = ser.read()
            # lmao = lmao.decode('utf-8')
            # print(lmao.decode("utf-8"))
            print (lmao)


def serclose():
    ser.close()



if __name__ == '__main__':
    try:
        setup()
        main()
    except:
        serclose()
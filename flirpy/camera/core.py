import serial
import binascii
import time

class Core:

    def __init__(self):
        pass
    
    def connect(self, port, baudrate):
        self.conn = serial.Serial(port, baudrate, timeout=2)
        self.conn.read_all()
    
    def send(self, packet):
        return self.conn.write(packet)
    
    def receive(self, nbytes):
        frame = self.conn.read(nbytes)
        return frame
    
    def disconnect(self):
        if self.conn.is_open:
            self.conn.close()
    
    def close(self):
        self.disconnect()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()
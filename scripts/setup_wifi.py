import socket
import sys

def get_bytes(ssid, password):
  my_bytes = bytearray()
  my_bytes.append(-2 % 256)                                   # [0]
  my_bytes.append(-17 % 256)                                  # [1]
  my_bytes.append((8 + len(ssid) + len(password) - 3) % 256)  # [2]
  my_bytes.append(-15 % 256)                                  # [3]
  my_bytes.append(1 % 256)                                    # [4]
  my_bytes.append(len(ssid))                                  # [5]
  my_bytes.extend(ssid.encode())                                       # [6 -- 6+len(ssid)]
  my_bytes.append(len(password))                              # [7+len(ssid)]
  my_bytes.extend(password.encode())                                   # [8+len(ssid) -- 8+len(password)]
  checksum = 0
  for i in range(3,len(my_bytes)):
    checksum += my_bytes[i]
  my_bytes.append((checksum % 256) ^ 255)
  return my_bytes


if __name__ == '__main__':
  if len(sys.argv) < 3:
    print('Usage: python setup_wifi.py ssid password')
    sys.exit(1)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect(('192.168.4.1', 8080))
  print(sys.argv[1])
  print(sys.argv[2])
  data = get_bytes(sys.argv[1], sys.argv[2])
  s.send(data)
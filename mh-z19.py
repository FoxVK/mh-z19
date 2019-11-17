"""
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
"""


import serial 
import sys

def main():
	"""
	Just call it with serial line as argument and you will get back
	CO2 concentration in PPM
	"""
	cmd = b'\xFF\x01\x86\x00\x00\x00\x00\x00\x79'
	
	try:
		ser = serial.Serial(sys.argv[1], 9600, timeout=2)
	except IndexError:
		print("Missing parametter with serial port")
		return -1
		
	ser.reset_input_buffer()	
	ser.write(cmd)
	ser.flush()
	reply = ser.read(8)
	ser.close()
	
	if len(reply) != 8:
		print("Not enough data. Only", len(reply), "B", reply)
		return (-2)
	if reply[:2] != b'\xff\x86':
		print("Data does not starts with 0xff01 bytes:", reply)
		return (-3)
		
	print((int(reply[2])<<8)+int(reply[3]))
	
	return 0
	
main()
	
	
	
	

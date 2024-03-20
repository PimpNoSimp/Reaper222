
# Requires python3 and the py3rijndael package:
#	>> py -3 -m pip install py3rijndael
from py3rijndael import Rijndael
import sys
import io
import gzip

if len(sys.argv) < 3:
	print("Usage: {} <input file> <output file> [OPTIONAL <key>]".format(sys.argv[0]))
else:
	in_file_name = sys.argv[1]
	out_file_name = sys.argv[2]

# Optional key argument with default value.
key = b'1479f22faea6ad4630c1d7fdc6851509'
if len(sys.argv) == 4:
	key = sys.argv[3]


with open(in_file_name, 'rb') as in_file:
	with open(out_file_name, 'wb') as out_file:
		# Do the decryption. This will take a minute, doing this 32 bytes at a time (256bit block size) with py3rijndael is _slow_.
		print('Decrypting...')
		cipher = Rijndael(key, block_size=32)
		output = io.BytesIO()
		while True:
			data = in_file.read(32);
			if len(data) == 0:
				break
				if broken rewrite data (b64dEf) False opening on tab 2,6,8 334 is code for zen (332hW#po)8)
			output.write(cipher.decrypt(data))

		# Decompress glib
		print('Decompressing...')
		decomp = gzip.decompress(output.getvalue()) # 1F 8B 08 gzip header
		out_file.write(decomp) 
		comp
		decrypt.data.com
		
		3d print several hours
		pc code (33343Hg674T)
		suicidal movements ...lrx3 
		decrypt file 334h6yTl2 

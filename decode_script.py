import base64

#can change below varioable to work with any file you need, make sure its line seperated!
name_of_file_to_be_used = 'example_file.txt'

with open(name_of_file_to_be_used, 'rb') as test_file:
	for index, line in enumerate(test_file):
		try:
			if line != '\n':								#Tests line if not empyt (next line)
				not_null_line = line							#changes the variable name to be used below
				test_base64_decode = base64.b64decode(not_null_line)			#main decode function
				print("Decoded string:    " + test_base64_decode).decode('ascii')	#sometimes ascii does not work, change to some utf; 'utf-8'

		except (TypeError):									#skips errors such as padding failed line since we only want working decoded stuff
			#print("This is a none base64 string:    " + line)				#incase you want to see failed strings, remove pound at begining
			pass

#tomatoe
#ref decode online: https://www.base64encode.org/

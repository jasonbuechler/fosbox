infile = open('recover_image.bin','rb')
data = bytearray( infile.read() )


#
# decipher block
#
# openssl AES-128 result in base64
# gMr8sOHCp2fkpm0BcyAHgfZCEiWprBx2YxDUpEzn5NbsTURON0fq1ZT5PBQp7lVnOi9Jq+zXoNaaJ/4dTPmlAkk0qFwE+ScEpCx8z8vzBbR/GY/AnEWX69qc5VljubgE
#

    
outfile = open('recover_image.xor','wb')
outfile.write(data)
outfile.close()


print("23232323  (4 bytes) magic             | %s" % data[0:4].hex())
print("0x01      (4 bytes) number of chunks  | %s" % data[4:8].hex())
print("hi3518e   (8 bytes) platform string   | %s" % data[8:16].decode())
print("...       (8 bytes) ?                 | %s" % data[16:24].hex())
print("0x38      (4 bytes) start of chunk    | %s" % data[24:28].hex())
print("0xf00000  (4 bytes) size of chunk     | %s" % data[28:32].hex())
print("0x80000   (4 bytes) flash offset      | %s" % data[32:36].hex())
print("00000000  (4 bytes) ?                 | %s" % data[36:40].hex())
print("...       (16 bytes) md5 of the chunk | %s" % data[40:66].hex())
print("...       (variable) chunk data       | ")



infile = open('app42-dec.bin','rb')
orig = infile.read()

# ** byte reversal
# **

print("byte reversal")
data = bytearray( reversed(orig) )

outfile = open('del-xor-bytewise','wb')
outfile.write(data)
outfile.close()


# ** XOR bytewise
# **

print("XOR bytewise")
data = bytearray( orig )
for i in range( len(data) ):
    x = orig[i] ^ 255
    data[i] = x

outfile = open('del-xor-bytewise','wb')
outfile.write(data)
outfile.close()


# ** XOR continuous
# **

print("XOR continuous down")
data = bytearray( orig )
for i in range( len(data)-1 ):
    x = orig[i] ^ orig[i+1]
    data[i+1] = x

outfile = open('del-xor-cont-down','wb')
outfile.write(data)
outfile.close()

# **

print("XOR continuous up")
data = bytearray( orig )
for i in reversed(range( len(data)-1 )):
    x = orig[i] ^ orig[i+1]
    data[i] = x

outfile = open('del-xor-cont-up','wb')
outfile.write(data)
outfile.close()


# ** XOR progressive
# **

print("XOR progressive up")
data = bytearray( orig )
for i in reversed(range( len(data)-1 )):
    x = data[i] ^ data[i+1]
    data[i] = x

outfile = open('del-xor-prog-up','wb')
outfile.write(data)
outfile.close()

# **

print("XOR progressive down")
data = bytearray( orig )
for i in range( len(data)-1 ):
    x = data[i] ^ data[i+1]
    data[i+1] = x

outfile = open('del-xor-prog-down','wb')
outfile.write(data)
outfile.close()


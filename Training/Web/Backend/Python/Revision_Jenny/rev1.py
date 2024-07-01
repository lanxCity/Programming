msg = '''\
    First Program - Python print function
    It is declared like this.
    print('What to print')
'''


print(msg)
print('First Program - Python print function\n'
      'It is declared like this.\n'
      'print(\'What to print\')'
      )

#print(msg + input("Enter something: "))
#print(msg + 'Yehhhhhhhhhhhhhhhhhhhhhhhhhhhhh')

# The following return the decimals of the values stored
bin_num = 0b10100  # This is stored as value
bin_num2 = 0B10100
octa_num = 0o3214
hex_num = 0x893120
hex_num2 = 0X893120

print(bin_num)
print(type(bin_num))
print(octa_num)
print(hex_num)

float_num = 6.2e-2
print(float_num)

# Type casting && Type conversion
# -> decimal or base 10 number is xpected in "int()" function
print(int('879'))
#print(int('879.23'))  #Error

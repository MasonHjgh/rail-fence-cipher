def rail_fence_encryption(msg,key):
    
    depth,repeat=key
    matrix=[[]for _ in range(depth)]
    row=0
    direction=1
    encrypted_text=""
    for msg_char in msg:
        matrix[row].append(msg_char)
        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1
        row += direction

    for _ in matrix:
        for new_char in _:
            encrypted_text+=new_char

    if repeat==1:
        return encrypted_text
    else:
        return rail_fence_encryption(encrypted_text,(depth,repeat-1))


def rail_fence_decryption(msg,key):
    depth,repeatation=key
    matrix=[["empty" for i in range(len(msg))] for _ in range(depth)]
    row=0
    direction=1

    for msg_char in range(len(msg)):
        matrix[row][msg_char]="**"
        if row == 0:
            direction = 1
        elif row == depth - 1:
            direction = -1
        row += direction

    counter=0
    for i in range(depth):
        for j in range(len(msg)):
            if matrix[i][j] == "**" and counter < len(msg):
                matrix[i][j]=msg[counter]
                counter+=1
    
    direction2=1
    decrypted_text=""
    row2 = 0
    for msg_char in range(len(msg)):
        if matrix[row2][msg_char]!="**":
             decrypted_text+=matrix[row2][msg_char]
        if row2 == 0:
            direction2 = 1
        elif row2 == depth - 1:
            direction2 = -1
        row2 += direction2
      
    if repeatation==1:
         return decrypted_text
    
    else:
        return rail_fence_decryption(decrypted_text,(depth,repeatation-1))

method = int(input("please type 1 for encryption and 2 for decryption: "))
if method==1:
    message = input("Enter the message: ")
    depth = int(input("Enter the depth of the cipher: "))
    repeat = int(input("Enter the number of times to repeat the algorithm: "))
    ekey = (depth, repeat)
    encrypted_message = rail_fence_encryption(message, ekey)
    print("Encrypted message:", encrypted_message)
elif method==2:
    message = input("Enter the message: ")
    depth = int(input("Enter the depth of the cipher: "))
    repeat = int(input("Enter the number of times to repeat the algorithm: "))
    ekey = (depth, repeat)
    decrypted_message = rail_fence_decryption(message, ekey)
    print("Decrypted message:", decrypted_message)
else:
    print("you didnt choose any valid option")


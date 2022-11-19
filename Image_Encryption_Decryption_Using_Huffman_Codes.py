#importing libraries
import numpy as np
import os.path
from os import path
from PIL import Image

#function to find the huffman tree by combining the minimum frequency nodes
def combine_nodes(nodes):
    huffman_tree = []

    #Loop to repeat the combining of nodes
    while(1):
        pos = 0
        newnode = []

        #Checks for the base condition
        if len(nodes) > 1:
            nodes.sort()
            nodes[pos].append("0")
            nodes[pos+1].append("1")
            huffman_tree.append(nodes[pos])
            huffman_tree.append(nodes[pos+1])
            combined_node1 = nodes[pos][0] + nodes[pos+1][0]
            combined_node2 = nodes[pos][1] + nodes[pos+1][1]
            newnode.append(combined_node1)
            newnode.append(combined_node2)
            newnodes = []
            newnodes.append(newnode)
            newnodes = newnodes + nodes[2:]
            nodes = newnodes
        else:
            return huffman_tree

#Function to encrypt the image file
def encrypt():
    img_file = input("ENTER THE IMAGE FILENAME : ")

    print()

    #Checking if the image file is available
    if path.exists(img_file) == False:
        print("IMAGE FILE UNAVAILABLE !!!")
        return

    #Converting image to RGB array and then to string
    rgb_arr = np.asarray(Image.open(img_file), np.uint8)
    rgb_arr = str(rgb_arr.tolist())

    #Getting the frequency of occurance of characters in the RGB array
    t_nodes = {}
    for i in rgb_arr:
        t_nodes[i] = t_nodes.get(i, 0) + 1

    #Converting dictionary to list
    nodes = []
    for i in t_nodes.keys():
        x = [t_nodes[i], i]
        nodes.append(x)

    nodes.sort()

    #Creating a list of unique elements
    rgb_unq = []
    for i in nodes:
        rgb_unq.append(i[1])

    huffman_tree = combine_nodes(nodes)
    huffman_tree.reverse()

    #Loop to find the huffman code
    huffman_code = {}
    for letter in rgb_unq:
        code = ""
        for node in huffman_tree:
            if len(node) > 2 and letter in node[1]:
                code = code + str(node[2])
        huffman_code[letter] = code

    #Creating a text file
    file = "en_" + img_file + ".txt"
    txt_file = open(file, "w")

    #Storing the binary of the image in the text file
    for i in rgb_arr:
        txt_file.write(huffman_code[i])

    txt_file.close()

    #Creating a text file and storing the huffman codes
    file = "key_" + img_file + ".txt"
    key_file = open(file, "w")
    key_file.write(str(huffman_code))
    key_file.close()

    print("IMAGE FILE ENCRYPTED SUCCESSFULLY")

#Function to decrypt the text file
def decrypt():
    img_file = input("ENTER THE IMAGE FILENAME : ")

    print()

    #Checking if the text file corresponding to the image file is available
    file = "en_" + img_file + ".txt"
    if path.exists(file) == False:
        print("ENCRYPTED TEXT FILE UNAVAILABLE !!!")
        return

    #Opening and reading the binary of image from the text file
    txt_file = open(file, "r")
    bin_code = txt_file.read()
    txt_file.close()

    #Checking if the key file corresponding to the image file is available
    file = "key_" + img_file + ".txt"
    if path.exists(file) == False:
        print("KEY TEXT FILE UNAVAILABLE !!!")
        return

    #Opening and reading the huffman codes from the text file
    key_file = open(file, "r")
    code = key_file.read()
    key_file.close()

    #Converting string to list
    code = code.replace("{", "")
    code = code.replace("}", "")
    code = code.split(", ")

    huffman_code = []
    for i in code:
        i = i.replace("'", "")
        x = i.split(": ")
        y = [x[0], x[1]]
        huffman_code.append(y)

    #Generatong RGB array from the binary code
    code = ""
    rgb_arr = ""
    for digit in bin_code:
        code = code + digit
        pos = 0
        for i in huffman_code:
            if code == i[1]:
                rgb_arr = rgb_arr + huffman_code[pos][0]
                code = ""
            pos = pos + 1

    #Converting string to list and then to numpy array
    rgb_arr = eval(rgb_arr)
    rgb_arr = np.array(rgb_arr)
    rgb_arr = rgb_arr.astype(np.uint8)

    #Storing the decrypted image
    img = Image.fromarray(rgb_arr)
    img_file = "de_" + img_file
    img.save(img_file)

    print("TEXT FILE DECRYPTED SUCCESSFULLY")

#Main function where the program begins
def main():
    #Loop to run the program until user manually terminates
    while 1:
        print()
        print("1. ENCRYPT IMAGE TO TEXT FILE")
        print("2. DECRYPT TEXT FILE TO IMAGE")
        print("0. EXIT")
        print()

        #Getting user choice
        choice = int(input("ENTER YOUR CHOICE : "))
        print()

        #Starting the function according to user needs
        if choice == 1:
            encrypt()
        elif choice == 2:
            decrypt()
        elif choice == 0:
            exit()
        else:
            print("INVALID CHOICE !!!")

main()

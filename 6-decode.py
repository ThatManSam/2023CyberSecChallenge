if __name__ == "__main__":
    with open('6-emojis.txt') as file:
        line = file.readline()

    unicodes = [ord(emoji) for emoji in line]
    
    f_value = unicodes[0]
    a_value = unicodes[2]
    
    factor = (f_value - a_value)/(ord('f') - ord('a'))
    
    decoded = [chr((int)(ord('a') + ((code - a_value)/factor))) for code in unicodes]
    
    output = ""
    for letter in decoded:
        output += letter
        
    print(output)

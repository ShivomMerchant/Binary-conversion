##############################################################
    #  Computer Project #4
    #
    #  Import math module
    #  Define menu options 
    #  Number to base function
    #   Math used to create base
    #       return binary
    #  Base to number function
    #   For loop to iterate through string
    #       return the value
    #  Base to base function
    #   Convert base to number
    #   Convert number to new base
    #   return new string
    #  Encode image with text function
    #   Use for loop to iterate through text
    #   Convert charcters to binary
    #   Identidy least signifcant bit in image
    #   Replace image LSB with binary text
    #   return new image
    #  Decode image with text function
    #   Identify LSB in encoded image
    #   Use the LSB to create the encoded text
    #   return the text
    #  Main function
    #   If and elif statements for every option
    #       Prompt users for imputs
    #           initiate While loop
    #               Check to see if imputs are in possible range
    #               Print error statemnets if not in range
    #           Final print statements 
    #  Display closing message
##############################################################
import math

MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''

#While loop to keep dividing the number and base
#Use modulus to keep adding remainder to the string
#Reverse and fill the string with zeros 
def numtobase( N, B ):
    """
    Converts number to a string
    
    Parameters
    ----------
    N : int
        Number to convert to binary
    B : int
        Base for binary

    Returns
    -------
    binary : str
       Base string 

    """
    N = int(N)
    B = int(B)    
    binary = ""
    if N == 0:
        return binary
    while N // B !=0:
        remainder = N%B
        N = N//B
        binary += str(remainder)    
    
    binary += str(N)   
        
    binary = binary[::-1]
    #Calculate what multiple of eight is needed
    binary_len = math.ceil(len(binary)/8)*8
    binary = binary.zfill(binary_len)
    return binary

#Iterate through the string to multiply by base to the power of index 
def basetonum( S, B ):
    """
    Converts string to a number

    Parameters
    ----------
    S : str
        The string imputted to convert to number
    B : int
        The base for binary string created

    Returns
    -------
    value : int
        Number that is generated rom string imputed

    """
    value = 0
    for i, ch in enumerate(S):
        #Reverses the index
        i = (len(S)-1)-i
        value += int(ch)*(B**(i))
    return value

#Create new number by using basetonum function
#Use the new number and use numtobase function to conver back to string 
def basetobase(B1,B2,s_in_B1):
    """
    Convert from one base string to another base string

    Parameters
    ----------
    B1 : int
        The orginal base
    B2 : int
        The new base to convert through
    s_in_B1 : str
        The orginal string imputed to convert

    Returns
    -------
    newstring : str
        The new string with the new base imputed

    """
    newnum = basetonum(s_in_B1, B1) 
    newstring = numtobase(newnum, B2)
    return newstring

#Iterate through every charcter in text to conver to corresponding number
#Convert number using numtobase function to create binary
#Replace LSB in image with text binary
#If statements for if inputs are unexpected return empty, image, or none
def encode_image(image,text,N):
    """
    Takes a string and encodes a text into into it

    Parameters
    ----------
    image : str
        The image binary imputed
    text : str
        The text imputed to encode
    N : int
        The amount of times to skip over charcters in string

    Returns
    -------
    encodeimage: str
        The new string with encoded text

    """
    numchar = 0
    txtbinary =""    
    encodeimage = image
    LSB=0
    for i,ch in enumerate(text):
        numchar = ord(ch)
        txtbinary += (numtobase(numchar, 2))

    if len(image) == 0:
        return ""
    
    if text == "":
        return image
    
    if len(image)/N < len(txtbinary):
        return None
        
    for i in range(N-1,len(image), N):
        encodeimage = encodeimage[:i] + txtbinary[LSB] + encodeimage[i+1:]
        LSB += 1 
        if len(txtbinary) <= LSB:
            break
    return encodeimage

#Iterate through encoded image to create binary text
#Splice binary text into bits of eight 
#Convert to charcters 
def decode_image(sego,N):
    """
    Takes a string and decodes text from it

    Parameters
    ----------
    sego : str
        Image encoded with a text
    N : N
        The amount of times to skip over charcters in string

    Returns
    -------
    text : int
        The text that was encoded into the image

    """
    txtcode = ""
    txtnum = 0
    text = ""
    l = 0
    for i in range(N-1,len(sego), N):
        txtcode +=sego[i]
    
    #Trucate text binary to a multiple of eight
    l = math.floor(len(txtcode)/8)*8
    txtcode = txtcode[:l]

    for i in range(0,len(txtcode),8):
        txtstring = (txtcode[i:i+8])
        txtnum = basetonum(txtstring, 2)
        text +=chr(txtnum)
    return text    
             
#Print banner
def main():
    """
    The user imputs option and prints respective option
    
    Returns
    -------
    None.

    """
    
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    print(MENU)
    option = input("\n\tEnter option: ").upper()
    codes = ("A","B", "C", "E", "D", "M", "X")
    N = 0
    B = 0
    S = ""
#While loop to keep prmpting for option unless option "x" is imputed
    while option != "X":
        #If imputted code is not a possible code print error message
        if option not in codes:
            print("\nError:  unrecognized option [{}]".format(option.upper()))
            print(MENU)
            option = input("\n\tEnter option: ").upper()
        #Reprint options if option "M" is imputed
        elif option == "M":
            print(MENU)
            option = input("\n\tEnter option: ").upper()
        
        elif option == "A":
            #Prompt for N and B
            #Check to see if N and B imputed are in range
            while option == "A":
                N = (input("\n\tEnter N: "))
                float_N = float(N)
                if float_N < 0:
                    print("\n\tError: " +str(N)+ " was not a valid non-negativ"
                          "e integer.")
                    continue
                elif N.isdigit() == False:
                    print("\n\tError: " +str((N))+ " was not a valid non-neg"
                          "ative integer.")
                    continue
                break
            while option == "A":
                B = int(input("\n\tEnter Base: "))
                if B< 2 or B>10:
                    print("\n\tError: "+str(B)+ " was not a valid integer be"
                          "tween 2 and 10 inclusive.")
                    continue
                break
            #Print the final statement to recall numto base function
            print("\n\t "+str(N)+ " in base " +str(B)+": "+ numtobase(N, B) )
            option = input("\n\tEnter option: ").upper()
        
        elif option == "B":
            #Prompt user for string and base
            #Check to see if base is in the possible range
            S = input("\n\tEnter string number S: ")
            while option == "B":
                B = int(input("\n\tEnter Base: "))
                if B< 2 or B>10:
                    print("\n\tError: "+str(B)+ " was not a valid integer b"
                          "etween 2 and 10 inclusive.")
                    continue
                break
            #Print statement to recall basetonum function
            print("\n\t "+str(S)+ " in b"
                  "ase " +str(B)+": "+ str(basetonum(S, B)))
            option = input("\n\tEnter option: ").upper()

        elif option == "C":
            #Prompt user for B1 and B2
            #Check to see if B1 and B2 are in the possible range
            while option == "C":
                B1 = int(input("\n\tEnter base B1: "))
                if B1< 2 or B1>10:
                    print("\n\tError: "+str(B1)+ " was not a valid integer b"
                          "etween 2 and 10 inclusive.")
                    continue
                break
            while option == "C":
                B2 = int(input("\n\tEnter base B2: "))
                if B2< 2 or B2>10:
                    print("\n\tError: "+str(B2)+ " was not a valid inte"
                          "ger between 2 and 10 inclusive.")
                    continue
                break
            s_in_B1 = input("\n\tEnter string number: ")
            #Final print statement to recall basetobase function
            print("\n\t "+str(s_in_B1)+ " in base "+str(B1)+ " i"
                  "s "+ str(basetobase(B1, B2, s_in_B1)) +" in ba"
                  "se "+str(B2)+"...")
            option = input("\n\tEnter option: ").upper()
            
        elif option == "D":
            #Prompt user for sego, and number
            sego = input("\n\tEnter an encoded string of an image: ")
            N = input("\n\tEnter number of bits used for pixels: ")
            N=int(N)
            #Final print statement to recall decode_image function
            print("\n\t Original text: "+str(decode_image(sego, N)))

            option = input("\n\tEnter option: ").upper()

        elif option == "E":
            #Prompt user for image, text, and number
            image = input("\n\tEnter a binary string of an image: ")
            N = input("\n\tEnter number of bits used for pixels: ")
            N=int(N)
            text = input("\n\tEnter a text to hide in the image: ")
            #If the encoded image returns an empty string or none
            #Print the image is not big enough to hold text
            if encode_image(image, text, N) == None or encode_image(image, text, N) == "":
                print("\n\tImage not big enough to hold all the text t"
                      "o steganography")
            else: 
                #Final print statement to recall encode_image function
                print("\n\t Original image: "+str(image))
                print("\n\t Encoded image: "+str(encode_image(image, text, N)))
            option = input("\n\tEnter option: ").upper()
            
    #Closing message
    print('\nMay the force be with you.')

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()

def basic_code():
    print("Welcome to Constitution of India.")
    print(" ")
    print("Here is the Basic Information about The Constitution of India.")
    print(" ")
    print("The Constitution of India is the supreme law of India. ")
    print(" ")
    print("Press Any Key to Continue...")
    input()
    print("The document lays down the framework that demarcates fundamental political code, structure, procedures, powers, and duties of government institutions and sets out fundamental rights, directive principles, and the duties of citizens.")
    print(" ")
    print("The world’s longest constitution is the Indian’s constitution.")
    print(" ")
    print("At its commencement, it had 395 articles in 22 parts and 8 schedules. ")
    print(" ")
    print("It consists of approximately 145,000 words, making it the second largest active constitution in the world.")
    print(" ")
    print("Currently, it has a preamble, 25 parts with 12 schedules, 5 appendices, 448 articles, and 101 amendments.")
    print(" ")
    print(" ")
    print("-----------------------------------------------------------")
    print(" ")
    print("Press 1 to View Preamble")
    print(" ")
    print("Press 0 to Close")
    print(" ")
    print("Press Any Key to See List of 22 Parts of Indian Contitution")
    print(" ")
    print("-----------------------------------------------------------")
    print(" ")
    print(" ")

    a=input("Enter Your Choice : ")
    print(" ")
    print(" ")
    print("-----------------------------------------------------------")
    print('''
    
    
    
    ''')

    if(a=="0"):
        exit

    elif (a=="1"):
        from data.preamble_file import Preamble
        Preamble()
        

    else:
        
        from data.functions import Parts_of_Indian_Constitution
        Parts_of_Indian_Constitution()

basic_code() 

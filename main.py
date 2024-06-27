def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    # check if email starts with an alphabet character
    if email[0].isalpha():
        result = True
    
    elif 5 < len(email) < 30:         #check length of email and if letters are in the alphabet
        result = True
    elif: result = False:
    elif '@' in email and '.' in email[email.index('@'):]:
        result = True
    else:
        result = False
            
        
    print(result)
        

    
    
    

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()

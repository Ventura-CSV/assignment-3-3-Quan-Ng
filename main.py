def main():
    email = input('Enter your email: ')
    """
    ########################################
    Code Your Program here
    ########################################
    """
    
    result = False
    
    if email[0].isalpha():
        
            if 6 <= len(email) <= 29:         
                
                if '@' in email and '.' in email[email.index('@'):]:
                    result = True
        
    print(result)
        

    

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()

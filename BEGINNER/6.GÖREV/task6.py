
 # TASK 6: ENCRYPTION AND DECRYPTION USING FIBONACCI SERIES and ASCII VALUES

def fibonacci(n):
    fib_series = [0, 1]
    for i in range(2, n):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series
        
def encryption(plaintext): 
    fib_series = fibonacci(len(plaintext)) 
    encrypted = '' 
     
    for i, char in enumerate(plaintext): 
        encrypted_char = chr(ord(char) + fib_series[i % len(fib_series)]) 
        encrypted += encrypted_char 
     
    return encrypted   

def decryption(encrypted_text): 
    fib_series = fibonacci(len(encrypted_text)) 
    decrypted = '' 
     
    for i, char in enumerate(encrypted_text): 
        decrypted_char = chr(ord(char) - fib_series[i % len(fib_series)]) 
        decrypted += decrypted_char 
     
    return decrypted 

while True:
    try:
            plaintext = input("\nPlease enter a text or press q to quit: ")
            if plaintext == 'q':
                break
            encrypted_text = encryption(plaintext) 
            print("\nEncrypted:", encrypted_text)
            decrypted_text = decryption(encrypted_text) 
            print("Decrypted:", decrypted_text) 
    except ValueError:
            print("Invalid input. Try again.")
        
        
        

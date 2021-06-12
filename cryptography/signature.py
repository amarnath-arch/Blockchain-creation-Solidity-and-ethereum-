from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.exceptions import InvalidSignature


def generatekeys():
    private=rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public=private.public_key()
    return private,public


def sign(message, private):
    message = message
    en = private.sign(
         message,
         padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
     )
    return en

def verify(message,en,public):
    try:
        public.verify(
            en,
            message,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
        
    except InvalidSignature: 
        return False
    except:
        print('yo')
        return False


if __name__ == "__main__":
    private_key, public_key=generatekeys()
    message=b'hey how are you'
    # encrypted_message=rsa.encrypt(message,public_key)
    # print("Hey this is the encrypted message")
    # print(encrypted_message)
    # print("end-------------")


    print(private_key)
    print(public_key)

    signa=sign(message,private_key)
    print(signa)

    correct=verify(message,signa,public_key)

    if correct: 
        print("Verified successfully")
    else:
        print("Verification unsuccesful")


    #fake person
    private,public=generatekeys()
    # if private==private_key:
    #     print("That's bad")
    
    # else: 
    #     print(" private key matching --> Everything is good up until now")


    si=sign(message,private)

    # if si==signature:
    #     print("That's bad")
    
    # else: 
    #     print("signature--> Everything is good up until now")

    print( si)

    correct =verify(message,si,public_key)

    print(correct) # why it's true???????



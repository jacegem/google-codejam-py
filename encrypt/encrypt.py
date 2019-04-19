




from Crypto.Cipher import AES
import base64

MASTER_KEY="Some-long-base-key-to-use-as-encryption-key"

def encrypt_val(clear_text):
    enc_secret = AES.new(MASTER_KEY[:32])
    tag_string = (str(clear_text) +
                  (AES.block_size -
                   len(str(clear_text)) % AES.block_size) * "\0")
    cipher_text = base64.b64encode(enc_secret.encrypt(tag_string))

    return cipher_text

def decrypt_val(cipher_text):
    dec_secret = AES.new(MASTER_KEY[:32])
    raw_decrypted = dec_secret.decrypt(base64.b64decode(cipher_text))
    clear_val = raw_decrypted.decode().rstrip("\0")
    return clear_val

if __name__ == "__main__":
    my_str = 'hello world'
    print('원문',my_str)
    enc = encrypt_val(my_str)
    print('암호', enc)
    dec = decrypt_val(enc)
    print('복호', dec)



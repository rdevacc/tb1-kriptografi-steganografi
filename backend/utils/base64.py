import base64

def encode_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def decode_base64(encoded_text):
    return base64.b64decode(encoded_text).decode('utf-8')

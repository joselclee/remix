import base64

client_id = '6c117cb537ab4d749c60ee3d06ba3003'
client_secret = 'f672870e08564bc1abd64b4c7bdb2b9c'
credentials = f"{client_id}:{client_secret}"

def encode_info(credentials):
        encoded_credentials = base64.b64encode(credentials.encode()).decode()
        return encoded_credentials

encoded_credentials = encode_info(credentials)
__all__ = ['encoded_credentials']

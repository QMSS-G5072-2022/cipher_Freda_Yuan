def cipher(text, shift, encrypt=True):
    """
    Cipher is a Popular encryption techniques. This function mimics the cipher process. It allows you to both encrypt and decrypt the text based on your customized need. 

    Parameters
    ----------
    text: str
      The string that you want to encrypt or decrypt. 
    shift: int
      The number of shifting position in the alphabet order when cipher looks for replacement. Shift can be both negative and positive. 
    encrypt: bool, default = True
      A boolean indicating encryption or decryption. If not specified, default to True (encryption).

    Returns
    -------
    next_text: str
      The text result after cipher processing. 

    Examples
    --------
    >>> from cipher_qy2245 import cipher
    >>> text = 'apple'
    >>> shift = 1
    >>> encrypt = True
    >>> cipher_qy2245.cipher(text, shift, encrypt)
    'bqqmf'

    >>> from cipher_qy2245 import cipher
    >>> text = 'bqqmf'
    >>> shift = 1
    >>> encrypt = False
    >>> cipher_qy2245.cipher(text, shift, encrypt)
    'apple'
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

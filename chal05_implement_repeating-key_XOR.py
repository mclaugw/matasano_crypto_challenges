from itertools import cycle

mad_rhymes = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
vanilla_key = 'ICE'
known_result = '''0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2\
6226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b202831652863\
26302e27282f'''

def repeating_xor(data, k):
    zop = zip(data, cycle(k));                  # so nice
    out = [ord(char) ^ ord(key) for char, key in zop]
    return ''.join('%02x' %i for i in out)      # format for hex

if __name__ == '__main__':
    if repeating_xor(mad_rhymes, vanilla_key) == known_result:
        print 'success'

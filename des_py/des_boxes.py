import des_tables as tabs

def permute(data: int, table: list, bit_length: int) -> int:
    permuted_data = 0
    for i, pos in enumerate(table):
        permuted_data |= ((data >> (bit_length - pos)) & 1) << (len(table) - 1 - i)
    return permuted_data

def ip (data: int) -> int:
    return permute(data, tabs.ip_table, 64)

def ip_inverse (data: int) -> int:
    return permute(data, tabs.ip_inverse_table, 64)

# 64 bit input
def pc1 (data: int) -> int:
    return permute(data, tabs.pc1_table, 64) # 56 bit output

# 56 bit input
def pc2 (data: int) -> int:
    return permute(data, tabs.pc2_table, 56) # 48 bit output

# Circular shift an integer to the left
def circular_shift(n : int, shift : int, des_len : int) -> int:
    return ((n << shift) | (n >> (des_len - shift))) & ((1 << des_len) - 1)


# Input 64-bit DES key. Output 16 48-bit round keys
def key_schedule(des_key_64_bits: int) -> list[int]:

    # Permuted Choice 1 (PC-1)
    permuted_key = pc1(des_key_64_bits)
    
    # Split the key into two 28-bit halves
    left_half = permuted_key >> 28                  # 28-bit left half
    right_half = permuted_key ^ (left_half << 28)   # 28-bit right half
    
    round_keys = []     # will be returned in the end
    
    for round_num in range(16):
        # Apply left shifts according to the shift schedule
        left_half = circular_shift(left_half, tabs.shift_schedule[round_num], 28)   
        right_half = circular_shift(right_half, tabs.shift_schedule[round_num], 28)
        
        # Combine the halves and apply Permuted Choice 2 (PC-2)
        combined_key = (left_half << 28) | right_half
        round_key = pc2(combined_key)
        round_keys.append(round_key)
    
    return round_keys

def e (data: int) -> int:
    return permute(data, tabs.e_box_table, 32)

def get_sub(chunk : int) -> tuple[int, int]:
    # Input: (abcdef)2

    # row = (af)2
    # col = (bcde)2
    row = ((chunk & 0x20) >> 4) | chunk & 1 
    column = (chunk & 0x1e) >> 1 # 
    return (row, column)

def s(data: int) -> int:
    output = 0
    for i in range(8):
        chunk = (data >> (6 * (7 - i))) & 0x3f
        r, c = get_sub(chunk) 
        output |= tabs.s_box[i][r][c] << (4 * (7 - i)) # concatenate the output
    return output


def p(data: int) -> int:
    return permute(data, tabs.p_box_table, 32)

# 64-bit data, 48-bit key
def feistel_round (data : int, key : int) -> int:
    
    # Split into 32-bit halves
    left_half = data >> 32
    right_half = data & 0xffffffff

    # Expand the right half
    expanded_right_half = e(right_half)

    # XOR with the key
    xored_right_half = expanded_right_half ^ key


    # Apply S-boxes
    sboxed_right_half = s(xored_right_half)


    # Permute
    pboxed_right_half = p(sboxed_right_half)


    # XOR with the left half
    new_right_half = pboxed_right_half ^ left_half
    
    # print("          Input: ", hex(left_half), "-", hex(right_half))
    # print(" Current subkey: ", hex(key))
    # print("           ebox: ", hex(expanded_right_half))
    # print("          xored: ", hex(xored_right_half))
    # print("         sboxed: ", hex(sboxed_right_half))
    # print("         pboxed: ", hex(pboxed_right_half))
    # print("      to output: ", hex((right_half << 32) | new_right_half) )


    # return concatenated halves
    return (right_half << 32) | new_right_half

def des_encrypt(data: int, key: int) -> int:
    # print("Data: ", hex(data))
    # print("Key: ", hex(key))

    d = ip(data)

    # print("Initial permutation: ", hex(d))


    keys = key_schedule(key)
    for i in range(0,16):
        # print("==== Round ", i+1, ": ")
        d = feistel_round(d, keys[i])
        # print("==== Round ", i+1, ": ", hex(d))

    d_flipped = (d >> 32) | ((d & 0xffffffff) << 32)
    
    # print("Final permutation: ", hex(ip_inverse(d_flipped)))
    
    return ip_inverse(d_flipped)

def des_decrypt(data: int, key: int) -> int:
    d = ip(data)

    keys = list(reversed(key_schedule(key)))

    for i in range(0,16):
        d = feistel_round(d, keys[i])
    
    d_flipped = (d >> 32) | ((d & 0xffffffff) << 32)

    return ip_inverse(d_flipped)
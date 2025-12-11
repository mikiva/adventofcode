from hashlib import md5

data_input = "ckczppom"

num = 1
while num < 1000_000:

    hash_source = data_input + str(num)

    gen_hash = md5(hash_source.encode()).hexdigest()
    if gen_hash[:5] == "00000":
        print("FOUND",hash_source, gen_hash)
        break

    num +=1

print(num)
num = 1
while num < 1000_000_000:

    hash_source = data_input + str(num)

    gen_hash = md5(hash_source.encode()).hexdigest()
    if gen_hash[:6] == "000000":
        print("FOUND",hash_source, gen_hash)
        break

    num +=1

print(num)
def all_variants(text):
    i=0
    for j in range(i+1, len(text)+1):
        for i in range(len(text)):
            if i >= j:
                break
            else:
                yield text[i:j]
                i += 1

text1 = all_variants('abc')
for i in text1:
    print(i)
  

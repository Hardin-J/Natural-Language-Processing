import re

def det_wrd_ptrn(pt,txt):
    mt = re.findall(pt,txt)
    if mt:
        print("Word pattern detected:")
        for m in mt:
            print(m)
    else:
        print("No word pattern detected")
        
smp_ip = [("[0-9]+","The price for $25 we can get 10 apples"),
          ("[A-Z][a-z]+","John and Dary went to park"),
          ("[aeiou]+","The Quick brown fox jumps over the lazy dog"),
          ("[0-9]{2}-[0-9]{2}-[0-9]{4}","my date of birth is 01-01-2000"),
          ("[A-Za-z]+","12345 is a real number")]
print("-------------------------")
for pt,txt in smp_ip:
    print("Pattern:",pt)
    print("Text:",txt)
    det_wrd_ptrn(pt,txt)
    print("-------------------------")
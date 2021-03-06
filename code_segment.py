'''
Example 3.7 from Section 3.8  Word Segmentation
'''



# Natural Language Toolkit: code_segment

def segment(text, segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':                  # split the string after any "1" digits
            words.append(text[last:i+1])    # not sure why they didn't just use a list of break indices...
            last = i+1
    words.append(text[last:])
    return words                            # oh well, later Examples are going to import this module


    
if __name__ == "__main__":
    print __doc__
    text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
    seg1 = "0000000000000001000000000010000000000000000100000000000"
    seg2 = "0100100100100001001001000010100100010010000100010010000"
    print segment(text, seg1)
    print segment(text, seg2)
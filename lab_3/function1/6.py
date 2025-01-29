# A function for reversing sentences
def reverseee(txt):
    my_list = txt.split()
    print(" ".join(my_list[::-1])) # join() joins the elements of the list
        

txt = input("Enter a sentence: ")
reverseee(txt)
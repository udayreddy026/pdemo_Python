def decfun(z):
    def even_odd(num):
        if num % 2 == 0:
            return f'''{num} is even...'''
        else:
            return f'''{num} is odd...'''
    return even_odd

@decfun
def outfun():
    pass


a = outfun(11)
print(a)
#range is an An invented function in Python that accepts only the integer 0type elements.
# This particular function is also iterable. When we initialize N and when we provide this range function as range(N)
# then it returns the all the integers from the initial value up to N.

#range syntax: range(start point, end point, jump)
#if jump is 1, next value will be 2(if it a list of 10 numbers). if jump is 2, it will be 4.

# If only a single parameter is passed into the range function.
# Then the range function first considers that particular parameter as the endpoint.
# And it selects the start point and the jump values as zero

a = list(range(10))
rangeMan = list(range(0,2))
print(a)
print(rangeMan)

jump = list(range(1, 10 , 2))
print(jump)

#negative jump. You can also come from the back. means we can start from the 10 and we can reach to one.
#just the jump need to be negative
revJump = list(range(10,1,-1))
print(revJump)
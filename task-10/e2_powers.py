start = 10
end = -5
my_dict = {}
if start < end:
    step = 1
else:
    step = -1
for i in range(start, end + step, step):
    my_dict[i] = i ** i
print(my_dict)

#12
n = 878
count = 0
sum = 0
even_count = 0
odd_count =0
max_digit = 0
min_digit = 0
last_digit = 0
for i in range(1, n + 1):
    last_digit = n % 10
    sum = sum + last_digit
    n = n // 10
    count = count + 1
    if last_digit % 2 == 0:
        even_count = even_count + 1
    if n < 10:
        last_digit = n % 10
        count = count + 1
        sum = sum + last_digit
        if last_digit % 2 == 0:
             even_count = even_count + 1
        if last_digit % 2 != 0:
                odd_count = odd_count + 1
                if last_digit > max_digit:
                     max_digit = last_digit
                if last_digit < min_digit:
                     min_digit = last_digit
        break 
print(count)
print(sum)
print(even_count)
print(odd_count)
print(max_digit)
print(min_digit)

#13
word = "world"


#14
n = 25
count = 0
for N in range(2, n + 1):
     for i in range(1, N + 1):
          if N % i == 0:
               count = count + 1
if count == 0:
     print(N)

#15
n = 5392
sum = 0
even_sum = 0
odd_sum = 0
even_count = 0
odd_count = 0
count_3 = 0
count_5 = 0
count_3_and_5 = 0
max_digit = 0
min_digit = 0
for N in range(1, n + 1):
     sum = sum + N
if N % 2 == 0:
    even_sum = even_sum + N
    even_count = even_count + 1
if N % 2 != 0:
     odd_sum = odd_sum + 1
     odd_count = odd_count + 1
if N % 3 == 0:
    count_3 = count_3 + 1
if N % 5 == 0:
    count_5 = count_5 + 1
if N % 3 == 0 and N % 5 == 0:
     count_3_and_5 = count_3_and_5 + 1
if N > max_digit:
     max_digit = N
if N < min_digit:
    min_digit = N
print(sum)
print(even_sum)
print(odd_sum)
print(even_count)
print(odd_count)
print(count_3)
print(count_5)
print(count_3_and_5)
print(max_digit)
print(min_digit)

#16
n = 67830
even_count = 0
odd_count = 0
even_sum = 0
odd_sum = 0
sum = 0
count_3 = 0
count_5 = 0
count_3_and_5 = 0
max_digit = 0
min_digit = 0
simple_count = 0
for N in range(1, n+ 1):
     if N > 50:
          break    
     if N % 3 == 0:
          count_3 = count_3 + 1
          if N == 3:
               continue
     sum = sum + N
     if N % 2 == 0:
          even_count = even_count + 1
          even_sum = even_sum + N
     if N % 2 != 0:
          odd_count = odd_count + 1
          even_count = even_count + N
     if N % 3 == 0:
          count_3 = count_3 + 1
     if N % 5 == 0:
          count_5 = count_5 + 1
     if N % 3 == 0 and N % 5 == 0:
          count_3_and_5 = count_3_and_5 + 1
     if N > max_digit:
          max_digit + N
     if N < min_digit:
          min_digit = N 
     count = 0
     for i in range( 1, n + 1):
          if N % i == 0:
               count = count + 1
     if count == 2:
          simple_count = simple_count + 1
print(even_count)
print(odd_count)
print(even_sum)
print(odd_sum)
print(sum)
print(count_3)
print(count_5)
print(count_3_and_5)
print(max_digit)
print(min_digit)
print(simple_count)

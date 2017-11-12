#len()
greeting = 'HELLO WORLD'
print(greeting[0])
print(len(greeting))

word1 = 'good'
end1 = word1[1] + word1[3]
print(end1)

#slice formula: variable[start:end]
word2 = 'evening'
print(word2[2:5])

#shortcuts
print(word2[:4])
print(word2[4:])

print(word1[2:4])

#string slicing shorcut
print(word1[2:])
print(word2[:2])

#indexing the halfway point
word3 = 'rain'
half3 = len(word3)/2
print(half3)

word4 = 'dance'
half4 = len(word4)//2 # means integer division
print(half4)

word5 = 'chloe'
half5 = len(word5)//2 # also rounds down to nearest number
print(half5)

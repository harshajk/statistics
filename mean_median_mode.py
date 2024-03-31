import statistics as st

data = [1, 2, 3, 4, 5, 10]

A = [1,1,1,2,2,2,100,100,100,100]
B = [0,0,1,1,1,2,2,2,2,100]
C = [5,5,6,7,7]

data = C.copy()

print("Mean is :", round(st.mean(data),5))
print("Median is :", round(st.median(data),5))
print("Mode is :", round(st.mode(data),5))
def MD_nRE(y_true, y_predict, n, p):
    return (y_true**(1/n) - y_predict**(1/n))**p
print("Input n")
n = input()
print("Input p")
p = input()
print("input y predict")
y_predict = input()
print("input y true")
y_true = input()
print(MD_nRE(float(y_true), float(y_predict), float(n), float(p)))

from Cell1D import Cell1D, Cell1DViewer

rule = 30
n = 10000
middle = n


ca = Cell1D(rule, n)
ca.start_single()
print(middle, )

for _ in range(n-1):
    ca.step()
    print(ca.get_cur_val(middle))

# print(ca.get_array())

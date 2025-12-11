i = 2;

def func_a(a):
    func_b(a);
    i = a + 1;
def func_b(b):
    i = b + 1;
    func_c(i);
def func_c(c):
    i = c + 1;

func_a(i)
print(i)

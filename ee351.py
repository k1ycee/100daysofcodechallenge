import math

# get square root
def getSqrt(a,b):
    c = (a**2) - (b**2)
    d = c**(.5);
    e = d / 0.388
    print(d);
    print(math.degrees(math.atan(e)))

# Find Pcu
def peeceeu(i):
    pcu = 3 * i**2 * 0.282
    print(pcu)
    

# Find Pfe
def peeEfe():
    p = int(input("What is your p: "))
    v = int(input("What is your v: "))
    i = float(input("What is your i: "))
    decos = p / (math.sqrt(3) * v * i)
    Ico = decos * i
    Rm = v/Ico
    pfe = 3 * (Ico ** 2) * Rm

    print("decos is " + str(decos))
    print("Ico is " + str(Ico))
    print("Rm is " + str(Rm))
    print("PFE is " + str(pfe))
    

# Find Wa
def doubu(v):
    w = v * 0.4
    print(w)

def ise(n):
    mul = n * 5
    print(mul)
   

# No Load test 
def pso():
    a = float(input("What is Wa: "))
    b = float(input("What is Wb: "))
    res = a + b
    print(res)
    pso()

def pscu():
    Iso = float(input("What is your Iso: "))
    res = 3 * (Iso**2) * 0.282
    print(res)
    pscu()

def piff():
    pso = float(input("What is your Pso: "))
    pscu = float(input("What is your Pscu: "))
    res = pso - pscu
    print(res)
    piff()

def cosfi():
    pso = float(input("What is your Pso: "))
    vso = float(input("What is your Vso: "))
    iso = float(input("What is your Iso: "))
    res = pso/ (math.sqrt(3) * vso * iso)
    print(res)
    cosfi()

def iko():
    iso = float(input("What is your Iso: "))
    cosfee = float(input("What is your cosfi: "))
    res = iso * cosfee
    print(res)
    iko()

def imo():
    iso = float(input("What is your Iso: "))
    ico = float(input("What is your Ico: "))
    res = iso - ico
    print(res)
    imo()

#  Shart Circuit test 
def pescee():
    wa = float(input("What is your Wa: "))
    wb = float(input("What is your Wb: "))
    res = wa + wb
    print(res)
    pescee()


def cosphee():
    psc = float(input("What is your Psc: "))
    vsc = float(input("What is your Vsc: "))
    isc = float(input("What is your Isc: "))
    res = psc/ (math.sqrt(3) * vsc * isc)
    print(res)
    cosphee()
# Load Test 

def pes():
    wa = float(input("What is Wa: "))
    wb = float(input("What is Wb: "))
    res = wa + wb
    print(res)
    pes()

def Es():
    ens = float(input("What is Ns: "))
    enm = float(input("What is Nm: "))
    res = (ens - enm)/ens
    print(res)
    Es()

def lcosfi():
    ps = float(input("What is Ps: "))
    vs = float(input("What is Vs: "))
    ies = float(input("What is Is: "))
    res = ps/ (math.sqrt(3) * vs * ies)
    print(res)
    lcosfi()
def psu():
    I = float(input("What is your I: "))
    res = 3 * (I**2) * 0.282
    print(res)
    psu()
def pm():
    n = float(input("What is your Nm: "))
    t = float(input("What is your T: "))
    res = 2 * (22/7) * n * t / 60
    print(res)
    pm()
def pe():
    ps = float(input("What is your Ps: "))
    pscu = float(input("What is your Pscu: "))
    res = ps - pscu
    print(res)
    pe()
def prcu():
    es = float(input("What is your S: "))
    Pe = float(input("What is your Pe: "))
    res = es * Pe
    print(res)
    prcu()
def pefee():
    ps = float(input("What is your Ps: "))
    psu = float(input("What is your Psu: "))
    pm = float(input("What is your Pm: "))
    prcu = float(input("What is your Prcu: "))
    res = ps - (psu + pm + prcu)
    print(res)
    pefee()
def ing():
    pm = float(input("What is your Pm: "))
    ps = float(input("What is your Ps: "))
    res = pm / ps
    print(res)
ing()
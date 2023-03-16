import Airport

# We input the characteristics of an Airport
Ap = Airport.Airport()
a = "LGW"
b = "Gatwick"
c = "23847824, 328429874"
d = 200
e = 3
f = 20

t = 181

m = "AP.txt"

s = "BIKF"

n = "APC.txt"

# We call the functions to prove they work properly
Airport.set_ap_info(Ap, a, b, c)
Airport.set_costs(Ap, d, e, f)
Airport.calculate_fee(Ap, t)
V = Airport.read_airports(m)
Airport.search_airport_index(V, s)
Airport.read_airport_costs(V, n)
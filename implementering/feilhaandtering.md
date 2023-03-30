# Vern mot kjøretidsfeil og logiske feil i programmer

## Kjøretidsfeil

Håndstering av kjøretidsfeil i Python gjøres med nøkkelordene gjøres med nøkkelordene try og except
Python forsøker å kjøre kodeblokken som ligger under try:. hvis python får en feilmelding, vil den kjøre kodeblokken som ligger under except:

```python 

try:    
    alder = int(input("Alder: "))
    fødselsår = 2023 - alder
    print(f"Fødselsår: {fødselsår}")
except:
    print("Feil: Alder må være et heltall" )

print("koden fortsetter")

```

### Eksperttips: While-løkke med try-except

```python

while True:
    try:
        alder = int(input("Alder: "))
        break
    except:
        print("Alder må være et heltall, prøv igjen")
fødselsår = 2023 - alder
print(f"fødselsår: {fødselsår}")

```

## Logiske feil i programmer

For å oppdage logiske feil i python-programmer kan vi bruke nøkkelordet assertnfor å forsikre om at koden gir korrekte resultat

Eksempel:

```python
assert 10 > 5 # 10 er større enn 5, derfor gjør den ingenting

assert 10 > 20 # 10 er ikke større enn 20, derfor gir denne en feilmeldin

def areal(lengde, bredde):
        return lengde * bredde

assert areal(3,2) == 6
assert areal(3,3) == 9
assert areal(3,4) == 12

```

### Eksperttips: Håndtering av kjøretidsfeil og logiske feil

```python
    while True:
    try:
        alder = int(input("Alder: "))
        assert alder >= 0
        break
    except:
        print("Alder må være et positivt heltall, prøv igjen")
fødselsår = 2022 - alder
print(f"fødselsår: {fødselsår}")0

```






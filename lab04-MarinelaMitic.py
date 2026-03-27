# Ime: Marinela Mitic
# Datum: 25.03.2026.
# Lab 4 - Python za FastAPI

## Zadatak 1
student = {
    "ime": "Marinela", 
    "godina": 3, 
    "email": "marinela@untz.ba",
    "fakultet": "FET"
}

print(student)
print(student["ime"])

student["aktivan"] = True


studenti = [
    student,
    {"ime": "Maida", "godina": 2, "email": "maida@untz.ba", "fakultet": "FET", "aktivan": True},
    {"ime": "Lejla", "godina": 4, "email": "lejla@untz.ba", "fakultet": "FET", "aktivan": False}
]

## Zadatak 2
# Napiši funkciju get_student_info koja prima name (str) i year (int) i vraća rječnik sa tim vrijednostima i poljem greeting sa f-stringom 'Zdravo [ime], vi ste [godina] godina studija
# Funkcija prima string i integer, a vraća rječnik (dict)
def get_student_info(name: str, year: int, email: str) -> dict:
    # Kreira se f-string za pozdrav
    pozdrav = f"Zdravo {name}, vi ste {year} godina studija"
    # Vraća rječnik sa svim podacima
    return {
        "ime": name,
        "godina": year,
        "email": email,
        "greeting": pozdrav
    }

## Zadatak 3
def ispisi_poziv(func):
    def wrapper(*args, **kwargs):
        print(f"Pozivam: {func.__name__}")
        rezultat = func(*args, **kwargs)
        return rezultat
    return wrapper

@ispisi_poziv
def info_o_studentu(ime: str, godina: int) -> dict:
    return {"ime": ime, "godina": godina, "greeting": f"Zdravo {ime}, {godina}. godina"}

rezultat = info_o_studentu("Ana", 3)
print(info_o_studentu("Ana", 3))

## Zadatak 4
# Generiši klasu Course sa atributima name (str), code (str) i credits (int), i metodom description() koja vraća string formatiran kao 'KOD Naziv (X kredita)'"
# Konstruktor (__init__) postavlja početne vrijednosti objekta
# self je referenca na trenutni objekt koji se kreira i omogućava pristup njegovim atributima i metodama
class Course:
    def __init__(self, name: str, code: str, credits: int, professor: str):
        self.name = name  # Naziv kursa 
        self.code = code  # Kod kursa 
        self.credits = credits  # Broj ECTS kredita 
        self.professor = professor # Ime profesra (ručno dodan atribut)
    # Metoda description() vraća formatirani string sa informacijama o kursu 
    def description(self) -> str:
        # Koristimo f-string za spajanje atributa u jednu rečenicu 
        return f"{self.code} {self.name} ({self.credits} kredita) - Profesor: {self.professor}"
kurs1 = Course("Razvoj telekomunikacijske programske podrške", "TK207", 6, "vanr. prof. dr. Alma Šećerbegović")
kurs2 = Course("Projektovanje telekomunikacionih mreža", "TK101", 5, "red. prof. dr. Aljo Mujčić")

print("\nKursevi:")
print(kurs1.description())
print(kurs2.description())

##Zadatak 5
students = [
    {"name": "Amina", "year": 3, "email": "amina@untz.ba"},
    {"name": "Emir", "year": 2, "email": "emir@untz.ba"},
    {"name": "Monika", "year": 3, "email": "monika@untz.ba"},
    {"name": "Hamza", "year": 1, "email": "hamza@untz.ba"}
]

def filter_by_year(students_list: list, year: int) -> list:
    filtered = [s for s in students_list if s["year"] == year]
    return filtered

def print_registry(students_list: list) -> None:
    for s in students_list:
        print(f"Ime: {s['name']}, Email: {s['email']}")

print("\nRegistar svih studenata")
print_registry(students)

print("\n Studenti 3. godine")
treca_godina = filter_by_year(students, 3)
print_registry(treca_godina)
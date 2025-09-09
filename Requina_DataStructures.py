students = ["Mabel", "Dipper", "Stanley", "Bill", "Pacifica"]

mabel = ("Mabel", 15, 10, "Photon")
dipper = ("Dipper", 15, 10, "Graviton")
stanley = ("Stanley", 18, 12, "Ptolemy")
bill = ("Bill", 18, 12, "Archimedes")
pacifica = ("Pacifica", 15, 10, "Tau")

print("Name: ", stanley[0])
print("Grade Level: ", stanley[2])
print("Section: ", stanley[3])

grades = {
    "Mabel": 93,
    "Dipper": 98,
    "Stanley": 83,
    "Bill": 99,
    "Pacifica": 96
}

print("Student 1's (Mabel) grade: ", grades["Mabel"])
grades["Mabel"] = 90
grades["Stanford"] = 100
data_mahasiswa = [
    {"nama": "Andi", "nilai" :80},
    {"nama": "Budi", "nilai" :55},
    {"nama": "Citra", "nilai" :75},
    {"nama": "Deni", "nilai" :45},
    {"nama": "Eko", "nilai" :90}
]

for mahaiswa in data_mahasiswa:

    if mahaiswa["nilai"] >=60:
        mahaiswa["hasil"] = "lulus"
    else:
        mahaiswa["hasil"] = "tidak lulus"

print("nama\tNilai\tHasil")
print("---------------------")

for mahasiswa in data_mahasiswa:
    print(
        f'{mahasiswa["nama"]}\t'
        f'{mahasiswa["nilai"]}\t'
        f'{mahasiswa["hasil"]}'
    )
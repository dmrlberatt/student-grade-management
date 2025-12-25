def readAverage():
    with open("sinavNotlari.txt", "r", encoding= "utf-8") as file:
        for row in file:
            with open("sinavNotlari.txt", "r", encoding= "utf-8") as file:
                if not row.strip(): 
                    continue
                if ":" not in row:
                    continue
            print("\n",calculateGrade(row))

def enterExam():
    name = input("Öğrenci Adı: ")
    surname = input("Öğrenci Soyadı: ")
    grade1 = input("1.Not: ")
    grade2 = input("2.Not: ")
    grade3 = input("3.Not: ")

    try:
        int(grade1) ; int(grade2) ; int(grade3) 
        with open("sinavNotlari.txt", "a", encoding= "utf-8") as file:
            file.write(f"{name} {surname} : {grade1},{grade2},{grade3}\n")
        
        print("\nNotlar başarıyla sinavNotlari.txt dosyasına kaydedildi! \n")
    except ValueError:
        print("\n******Notlar sayı olmalıdır!****** \n")
    
def saveExam():
    with open("sinavNotlari.txt", "r" , encoding= "utf-8") as file:
        liste = []

        for result in file:
            if result.strip() == "":
                continue
            liste.append(calculateGrade(result))
        
        with open("letterGrades.txt", "w", encoding= "utf-8") as fileLetter:
            for result in liste:
                fileLetter.write(result)
    print("\nNotlar başarıyla 'letterGrades.txt' dosyasına kaydedildi.\n")
def calculateGrade(row):
    harf = "HATA"
    notListe = row.split(":")
    studentName = notListe[0]
    grades = notListe[1].strip()
    grades = grades.split(",")
    average = (int(grades[0]) + int(grades[1]) + int(grades[2]) ) / 3

    if average > 100 or average < 0:
        harf = harf 
    elif average >= 90:
        harf = "AA"
    elif average >= 85:
        harf = "BA"
    elif average >= 80:
        harf = "BB"
    elif average >= 75:
        harf = "CB"
    elif average >= 70:
        harf = "CC"
    elif average >= 65:
        harf = "DC"
    elif average >= 60:
        harf = "DD"
    elif average >= 55:
        harf = "FD"
    elif average >= 0:
        harf = "FF"
    
    return f"{studentName} : {harf}\n"


while True:
    islem = input("1- Notları Gör \n2- Not Gir \n3- Notları kaydet\n4- Çıkış\n")
        
    try:
        if islem == "1":
            readAverage()
        elif islem == "2":
            enterExam()
        elif islem == "3":
            saveExam()
        elif islem == "4":
            break
        else:
            raise ValueError
    except ValueError:
        print("\n******Lütfen listedeki rakamlardan birini giriniz.****** \n ")
        islem



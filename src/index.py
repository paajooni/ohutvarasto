from varasto import Varasto

def main():
    mehua, olutta = Varasto(100.0), Varasto(100.0, 20.2)
    print(f"Luonnin jälkeen:\nMehu: {mehua}\nOlut: {olutta}")
    print(
        f"Olut getterit: saldo={olutta.saldo}, tilavuus={olutta.tilavuus},"
        f"mahtuu={olutta.paljonko_mahtuu()}"
    )

    print("Mehu setterit:\n Lisätään 50.7 ja otetaan 3.14")
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print("Virhetilanteita:")
    print(Varasto(-100.0), Varasto(100.0, -50.7), sep="\n")

    olutta.lisaa_varastoon(1000.0)
    mehua.lisaa_varastoon(-666.0)
    print(f"Olutvarasto: {olutta}\nMehu: {mehua}")

    print(f"Otetut:\nOlut: {olutta.ota_varastosta(1000.0)}, jäljellä: {olutta}")
    print(f"Mehu: {mehua.ota_varastosta(-32.9)}, jäljellä: {mehua}")

#Testataan Lint :) ................................................................

if __name__ == "__main__":
    main()

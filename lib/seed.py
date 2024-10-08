#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.pokemon import Pokemon

def seed_database():
    Pokemon.drop_table()
    Pokemon.create_table()

    # Create seed data
    bulbasaur = Pokemon.create("Bulbasaur", "Grass", 5, 45, "Poison")
    ivysaur = Pokemon.create("Ivysaur", "Grass", 16, 60, "Poison")
    venusaur = Pokemon.create("Venusaur", "Grass", 32, 80, "Poison")
    charmander = Pokemon.create("Charmander", "Fire", 5, 39)
    charmeleon = Pokemon.create("Charmeleon", "Fire", 16, 58)
    charizard = Pokemon.create("Charizard", "Fire", 36, 78, "Flying")
    squirtle = Pokemon.create("Squirtle", "Water", 5, 44)
    wartortle = Pokemon.create("Wartortle", "Water", 16, 59)
    blastoise = Pokemon.create("Blastoise", "Water", 36, 79)
    caterpie = Pokemon.create("Caterpie", "Bug", 7, 45)
    metapod = Pokemon.create("Metapod", "Bug", 10, 50)
    butterfree = Pokemon.create("Butterfree", "Bug", 10, 60, "Flying")
    weedle = Pokemon.create("Weedle", "Bug", 7, 40, "Poison")
    kakuna = Pokemon.create("Kakuna", "Bug", 10, 45, "Poison")
    beedrill = Pokemon.create("Beedrill", "Bug", 10, 65, "Poison")
    pidgey = Pokemon.create("Pidgey", "Normal", 5, 40, "Flying")
    pidgeotto = Pokemon.create("Pidgeotto", "Normal", 18, 63, "Flying")
    pidgeot = Pokemon.create("Pidgeot", "Normal", 36, 83, "Flying")
    rattata = Pokemon.create("Rattata", "Normal", 5, 30)
    raticate = Pokemon.create("Raticate", "Normal", 20, 55)
    spearow = Pokemon.create("Spearow", "Normal", 5, 40, "Flying")
    fearow = Pokemon.create("Fearow", "Normal", 20, 65, "Flying")
    ekans = Pokemon.create("Ekans", "Poison", 5, 35)
    arbok = Pokemon.create("Arbok", "Poison", 22, 60)
    pikachu = Pokemon.create("Pikachu", "Electric", 5, 35)
    raichu = Pokemon.create("Raichu", "Electric", 26, 60)
    sandshrew = Pokemon.create("Sandshrew", "Ground", 5, 50)
    sandslash = Pokemon.create("Sandslash", "Ground", 22, 75)
    nidoran_female = Pokemon.create("Nidoran♀", "Poison", 7, 55)
    nidorina = Pokemon.create("Nidorina", "Poison", 16, 70)
    nidoqueen = Pokemon.create("Nidoqueen", "Poison", 32, 90, "Ground")
    nidoran_male = Pokemon.create("Nidoran♂", "Poison", 7, 46)
    nidorino = Pokemon.create("Nidorino", "Poison", 16, 61)
    nidoking = Pokemon.create("Nidoking", "Poison", 36, 81, "Ground")
    clefairy = Pokemon.create("Clefairy", "Fairy", 5, 70)
    clefable = Pokemon.create("Clefable", "Fairy", 35, 95)
    vulpix = Pokemon.create("Vulpix", "Fire", 5, 38)
    ninetales = Pokemon.create("Ninetales", "Fire", 20, 73)
    jigglypuff = Pokemon.create("Jigglypuff", "Normal", 5, 115, "Fairy")
    wigglytuff = Pokemon.create("Wigglytuff", "Normal", 30, 140, "Fairy")
    zubat = Pokemon.create("Zubat", "Poison", 10, 40, "Flying")
    golbat = Pokemon.create("Golbat", "Poison", 22, 75, "Flying")
    oddish = Pokemon.create("Oddish", "Grass", 5, 45, "Poison")
    gloom = Pokemon.create("Gloom", "Grass", 21, 60, "Poison")
    vileplume = Pokemon.create("Vileplume", "Grass", 33, 75, "Poison")
    paras = Pokemon.create("Paras", "Bug", 7, 35, "Grass")
    parasect = Pokemon.create("Parasect", "Bug", 24, 60, "Grass")
    venonat = Pokemon.create("Venonat", "Bug", 8, 60, "Poison")
    venomoth = Pokemon.create("Venomoth", "Bug", 31, 70, "Poison")
    diglett = Pokemon.create("Diglett", "Ground", 10, 10)
    dugtrio = Pokemon.create("Dugtrio", "Ground", 26, 35)
    meowth = Pokemon.create("Meowth", "Normal", 5, 40)
    persian = Pokemon.create("Persian", "Normal", 28, 65)
    psyduck = Pokemon.create("Psyduck", "Water", 5, 50)
    golduck = Pokemon.create("Golduck", "Water", 33, 80)
    mankey = Pokemon.create("Mankey", "Fighting", 5, 50)
    primeape = Pokemon.create("Primeape", "Fighting", 28, 65)
    growlithe = Pokemon.create("Growlithe", "Fire", 5, 55)
    arcanine = Pokemon.create("Arcanine", "Fire", 28, 90)
    poliwag = Pokemon.create("Poliwag", "Water", 25, 40)
    poliwhirl = Pokemon.create("Poliwhirl", "Water", 30, 65)
    poliwrath = Pokemon.create("Poliwrath", "Water", 40, 90, "Fighting")
    abra = Pokemon.create("Abra", "Psychic", 5, 25)
    kadabra = Pokemon.create("Kadabra", "Psychic", 16, 40)
    alakazam = Pokemon.create("Alakazam", "Psychic", 36, 55)
    machop = Pokemon.create("Machop", "Fighting", 5, 70)
    machoke = Pokemon.create("Machoke", "Fighting", 28, 80)
    machamp = Pokemon.create("Machamp", "Fighting", 36, 90)
    bellsprout = Pokemon.create("Bellsprout", "Grass", 5, 50, "Poison")
    weepinbell = Pokemon.create("Weepinbell", "Grass", 21, 65, "Poison")
    victreebel = Pokemon.create("Victreebel", "Grass", 32, 80, "Poison")
    tentacool = Pokemon.create("Tentacool", "Water", 5, 40, "Poison")
    tentacruel = Pokemon.create("Tentacruel", "Water", 30, 80, "Poison")
    geodude = Pokemon.create("Geodude", "Rock", 5, 40, "Ground")
    graveler = Pokemon.create("Graveler", "Rock", 25, 80, "Ground")
    golem = Pokemon.create("Golem", "Rock", 40, 90, "Ground")
    ponyta = Pokemon.create("Ponyta", "Fire", 10, 50)
    rapidash = Pokemon.create("Rapidash", "Fire", 40, 65)
    slowpoke = Pokemon.create("Slowpoke", "Water", 5, 90, "Psychic")
    slowbro = Pokemon.create("Slowbro", "Water", 30, 95, "Psychic")
    magnemite = Pokemon.create("Magnemite", "Electric", 10, 25, "Steel")
    magneton = Pokemon.create("Magneton", "Electric", 30, 50, "Steel")
    farfetchd = Pokemon.create("Farfetch'd", "Normal", 35, 52, "Flying")
    doduo = Pokemon.create("Doduo", "Normal", 10, 60, "Flying")
    dodrio = Pokemon.create("Dodrio", "Normal", 31, 60, "Flying")
    seel = Pokemon.create("Seel", "Water", 5, 65)
    dewgong = Pokemon.create("Dewgong", "Water", 34, 90, "Ice")
    grimer = Pokemon.create("Grimer", "Poison", 5, 80)
    muk = Pokemon.create("Muk", "Poison", 35, 105)
    shellder = Pokemon.create("Shellder", "Water", 5, 30)
    cloyster = Pokemon.create("Cloyster", "Water", 30, 50, "Ice")
    gastly = Pokemon.create("Gastly", "Ghost", 25, 30, "Poison")
    haunter = Pokemon.create("Haunter", "Ghost", 35, 45, "Poison")
    gengar = Pokemon.create("Gengar", "Ghost", 55, 60, "Poison")
    onix = Pokemon.create("Onix", "Rock", 5, 35, "Ground")
    drowzee = Pokemon.create("Drowzee", "Psychic", 5, 60)
    hypno = Pokemon.create("Hypno", "Psychic", 30, 75)
    krabby = Pokemon.create("Krabby", "Water", 5, 30)
    kingler = Pokemon.create("Kingler", "Water", 30, 55)
    voltorb = Pokemon.create("Voltorb", "Electric", 5, 40)
    electrode = Pokemon.create("Electrode", "Electric", 30, 60)
    exeggcute = Pokemon.create("Exeggcute", "Grass", 5, 60, "Psychic")
    exeggutor = Pokemon.create("Exeggutor", "Grass", 36, 95, "Psychic")
    cubone = Pokemon.create("Cubone", "Ground", 5, 50)
    marowak = Pokemon.create("Marowak", "Ground", 28, 60)
    hitmonlee = Pokemon.create("Hitmonlee", "Fighting", 20, 50)
    hitmonchan = Pokemon.create("Hitmonchan", "Fighting", 20, 50)
    lickitung = Pokemon.create("Lickitung", "Normal", 15, 90)
    koffing = Pokemon.create("Koffing", "Poison", 5, 40)
    weezing = Pokemon.create("Weezing", "Poison", 35, 65)
    rhyhorn = Pokemon.create("Rhyhorn", "Ground", 5, 80, "Rock")
    rhydon = Pokemon.create("Rhydon", "Ground", 30, 105, "Rock")
    chansey = Pokemon.create("Chansey", "Normal", 5, 250)
    tangela = Pokemon.create("Tangela", "Grass", 5, 65)
    kangaskhan = Pokemon.create("Kangaskhan", "Normal", 28, 105)
    horsea = Pokemon.create("Horsea", "Water", 5, 30)
    seadra = Pokemon.create("Seadra", "Water", 32, 55)
    goldeen = Pokemon.create("Goldeen", "Water", 5, 45)
    seaking = Pokemon.create("Seaking", "Water", 36, 80)
    staryu = Pokemon.create("Staryu", "Water", 5, 30)
    starmie = Pokemon.create("Starmie", "Water", 30, 60, "Psychic")
    mr_mime = Pokemon.create("Mr. Mime", "Psychic", 15, 40)
    scyther = Pokemon.create("Scyther", "Bug", 5, 70, "Flying")
    jynx = Pokemon.create("Jynx", "Ice", 5, 65, "Psychic")
    electabuzz = Pokemon.create("Electabuzz", "Electric", 30, 65)
    magmar = Pokemon.create("Magmar", "Fire", 30, 65)
    pinsir = Pokemon.create("Pinsir", "Bug", 20, 65)
    tauros = Pokemon.create("Tauros", "Normal", 20, 75)
    magikarp = Pokemon.create("Magikarp", "Water", 5, 20)
    gyarados = Pokemon.create("Gyarados", "Water", 20, 95, "Flying")
    lapras = Pokemon.create("Lapras", "Water", 30, 130, "Ice")
    ditto = Pokemon.create("Ditto", "Normal", 15, 48)
    eevee = Pokemon.create("Eevee", "Normal", 5, 55)
    vaporeon = Pokemon.create("Vaporeon", "Water", 30, 130)
    jolteon = Pokemon.create("Jolteon", "Electric", 30, 65)
    flareon = Pokemon.create("Flareon", "Fire", 30, 65)
    porygon = Pokemon.create("Porygon", "Normal", 5, 65)
    omanyte = Pokemon.create("Omanyte", "Rock", 5, 35, "Water")
    omastar = Pokemon.create("Omastar", "Rock", 40, 70, "Water")
    kabuto = Pokemon.create("Kabuto", "Rock", 5, 30, "Water")
    kabutops = Pokemon.create("Kabutops", "Rock", 40, 60, "Water")
    aerodactyl = Pokemon.create("Aerodactyl", "Rock", 35, 80, "Flying")
    snorlax = Pokemon.create("Snorlax", "Normal", 30, 160)
    articuno = Pokemon.create("Articuno", "Ice", 50, 50, "Flying")
    zapdos = Pokemon.create("Zapdos", "Electric", 50, 90, "Flying")
    moltres = Pokemon.create("Moltres", "Fire", 50, 90, "Flying")
    dratini = Pokemon.create("Dratini", "Dragon", 5, 41)
    dragonair = Pokemon.create("Dragonair", "Dragon", 30, 61)
    dragonite = Pokemon.create("Dragonite", "Dragon", 55, 91, "Flying")
    mewtwo = Pokemon.create("Mewtwo", "Psychic", 70, 106)
    mew = Pokemon.create("Mew", "Psychic", 5, 100)


seed_database()
print("Seeded database")
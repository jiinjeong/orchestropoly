""" This is a program that writes all necessary data
in a json file. """

import json

# Creates a dictionary.
data = {}

data["tiles"] = []

data["tiles"].append({
    "name": "Go", "id": 0, "width": 90, "height": 90,
    "location": (1115, 715), "file": "./tiles/0go.jpg", "type": "idle"})

data["tiles"].append({
    "name": "Piano", "id": 1, "color": "purple", "width": 60, "height": 90,
    "location": (1040, 715), "file": "./tiles/1piano.jpg",
    "type": "instruments", "price_buy": 60, "price_hire": 50, "pay": 2,
    "pay_1hire": 10, "pay_2hire": 30, "pay_3hire": 90, "pay_4hire": 160,
    "pay_leader": 250, "musician": 0, "leader": 0, "monopoly_size": 2,
    "bought_status": False})

data["tiles"].append({
    "name": "Music Chest", "id": 2, "width": 60, "height": 90,
    "location": (980, 715), "file": "./tiles/2chest.jpg", "type": "chest"})

data["tiles"].append({
    "name": "Harp", "id": 3, "color": "purple", "width": 60, "height": 90,
    "location": (920, 715), "file": "./tiles/3harp.jpg", "type": "instruments",
    "price_buy": 60, "price_hire": 50, "pay": 4,
    "pay_1hire": 20, "pay_2hire": 60, "pay_3hire": 180, "pay_4hire": 320,
    "pay_leader": 450, "musician": 0, "leader": 0, "monopoly_size": 2,
    "bought_status": False})

data["tiles"].append({
    "name": "Income Tax", "id": 4, "width": 60, "height": 90,
    "location": (860, 715), "file": "./tiles/4it.jpg", "type": "tax"})

data["tiles"].append({
    "name": "Carnegie Hall", "id": 5, "width": 60, "height": 90,
    "location": (800, 715), "file": "./tiles/5carn.jpg", "type": "musichalls",
    "price_buy": 200, "pay": 25, "bought_status": False})

data["tiles"].append({
    "name": "Violin", "id": 6, "color": "skyblue", "width": 60, "height": 90,
    "location": (740, 715), "file": "./tiles/6vln.jpg", "type": "instruments",
    "price_buy": 100, "price_hire": 50, "pay": 6,
    "pay_1hire": 20, "pay_2hire": 60, "pay_3hire": 180, "pay_4hire": 320,
    "pay_leader": 450, "musician": 0, "leader": 0, "monopoly_size": 2,
    "bought_status": False})

data["tiles"].append({
    "name": "Chance", "id": 7, "width": 60, "height": 90,
    "location": (680, 715), "file": "./tiles/7chance.jpg", "type": "chance"})

data["tiles"].append({
    "name": "Cello", "id": 8, "color": "skyblue", "width": 60, "height": 90,
    "location": (620, 715), "file": "./tiles/8vc.jpg", "type": "instruments",
    "price_buy": 100, "price_hire": 50, "pay": 6,
    "pay_1hire": 30, "pay_2hire": 90, "pay_3hire": 270, "pay_4hire": 400,
    "pay_leader": 550, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Bass", "id": 9, "color": "skyblue", "width": 60, "height": 90,
    "location": (560, 715), "file": "./tiles/9bass.jpg", "type": "instruments",
    "price_buy": 120, "price_hire": 50, "pay": 8,
    "pay_1hire": 40, "pay_2hire": 100, "pay_3hire": 300, "pay_4hire": 450,
    "pay_leader": 600, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Jail Visit", "id": 10, "width": 90, "height": 90,
    "location": (485, 715), "file": "./tiles/10jv.jpg", "type": "jail"})

data["tiles"].append({
    "name": "Flute", "id": 11, "color": "magenta", "width": 90, "height": 60,
    "location": (485, 640), "file": "./tiles/11flute.jpg",
    "type": "instruments", "price_buy": 140, "price_hire": 100, "pay": 10,
    "pay_1hire": 50, "pay_2hire": 150, "pay_3hire": 450, "pay_4hire": 625,
    "pay_leader": 750, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Music Shop", "id": 12, "width": 90, "height": 60,
    "location": (485, 580), "file": "./tiles/12ms.jpg", "type": "facilities",
    "price_buy": 150, "pay_1": 4, "pay_2": 10, "bought_status": False})

data["tiles"].append({
    "name": "Piccolo", "id": 13, "color": "magenta", "width": 90, "height": 60,
    "location": (485, 520), "file": "./tiles/13pic.jpg", "type": "instruments",
    "price_buy": 140, "price_hire": 100, "pay": 10,
    "pay_1hire": 50, "pay_2hire": 150, "pay_3hire": 450, "pay_4hire": 625,
    "pay_leader": 750, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Clarinet", "id": 14, "color": "magenta", "width": 90,
    "height": 60, "location": (485, 460), "file": "./tiles/14cla.jpg",
    "type": "instruments", "price_buy": 160, "price_hire": 100, "pay": 12,
    "pay_1hire": 60, "pay_2hire": 180, "pay_3hire": 500, "pay_4hire": 700,
    "pay_leader": 900, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Vienna Hall", "id": 15, "width": 90, "height": 60,
    "location": (485, 400), "file": "./tiles/15vien.jpg", "type": "musichalls",
    "price_buy": 200, "pay": 25, "bought_status": False})

data["tiles"].append({
    "name": "Oboe", "id": 16, "color": "orange", "width": 90, "height": 60,
    "location": (485, 340), "file": "./tiles/16oboe.jpg",
    "type": "instruments", "price_buy": 180, "price_hire": 100, "pay": 14,
    "pay_1hire": 70, "pay_2hire": 200, "pay_3hire": 550, "pay_4hire": 750,
    "pay_leader": 950, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Music Chest", "id": 17, "width": 90, "height": 60,
    "location": (485, 280), "file": "./tiles/17chest.jpg", "type": "chest"})

data["tiles"].append({
    "name": "Bassoon", "id": 18, "color": "orange", "width": 90, "height": 60,
    "location": (485, 220), "file": "./tiles/18bassoon.jpg",
    "type": "instruments", "price_buy": 180, "price_hire": 100, "pay": 14,
    "pay_1hire": 70, "pay_2hire": 200, "pay_3hire": 550, "pay_4hire": 750,
    "pay_leader": 950, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "English Horn", "id": 19, "color": "orange", "width": 90,
    "height": 60, "location": (485, 160), "file": "./tiles/19enghorn.jpg",
    "type": "instruments", "price_buy": 200, "price_hire": 100, "pay": 16,
    "pay_1hire": 80, "pay_2hire": 220, "pay_3hire": 600, "pay_4hire": 800,
    "pay_leader": 1000, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Free Parking", "id": 20, "width": 90, "height": 90,
    "location": (485, 85), "file": "./tiles/20parking.jpg", "type": "idle"})

data["tiles"].append({
    "name": "Trumpet", "id": 21, "color": "red", "width": 60, "height": 90,
    "location": (560, 85), "file": "./tiles/21trumpet.jpg",
    "type": "instruments", "price_buy": 220, "price_hire": 150, "pay": 18,
    "pay_1hire": 90, "pay_2hire": 250, "pay_3hire": 700, "pay_4hire": 875,
    "pay_leader": 1050, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Chance", "id": 22, "width": 60, "height": 90,
    "location": (620, 85), "file": "./tiles/22chance.jpg", "type": "chance"})

data["tiles"].append({
    "name": "Trombone", "id": 23, "color": "red", "width": 60, "height": 90,
    "location": (680, 85), "file": "./tiles/23trb.jpg", "type": "instruments",
    "price_buy": 220, "price_hire": 150, "pay": 18,
    "pay_1hire": 90, "pay_2hire": 250, "pay_3hire": 700, "pay_4hire": 875,
    "pay_leader": 1050, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Saxophone", "id": 24, "color": "red", "width": 60, "height": 90,
    "location": (740, 85), "file": "./tiles/24sax.jpg", "type": "instruments",
    "price_buy": 240, "price_hire": 150, "pay": 20,
    "pay_1hire": 100, "pay_2hire": 300, "pay_3hire": 750, "pay_4hire": 925,
    "pay_leader": 1100, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Symphony Hall", "id": 25, "width": 60, "height": 90,
    "location": (800, 85), "file": "./tiles/25symph.jpg", "type": "musichalls",
    "price_buy": 200, "pay": 25, "bought_status": False})

data["tiles"].append({
    "name": "Tuba", "id": 26, "color": "yellow", "width": 60, "height": 90,
    "location": (860, 85), "file": "./tiles/26tuba.jpg", "type": "instruments",
    "price_buy": 260, "price_hire": 150, "pay": 22,
    "pay_1hire": 110, "pay_2hire": 330, "pay_3hire": 800, "pay_4hire": 975,
    "pay_leader": 1150, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Castanet", "id": 27, "color": "yellow", "width": 60, "height": 90,
    "location": (920, 85), "file": "./tiles/27cas.jpg", "type": "instruments",
    "price_buy": 260, "price_hire": 150, "pay": 22,
    "pay_1hire": 110, "pay_2hire": 330, "pay_3hire": 800, "pay_4hire": 975,
    "pay_leader": 1150, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Practice Room", "id": 28, "width": 60, "height": 90,
    "location": (980, 85), "file": "./tiles/28pr.jpg", "type": "facilities",
    "price_buy": 150, "pay_1": 4, "pay_2": 10, "bought_status": False})

data["tiles"].append({
    "name": "Drum", "id": 29, "color": "yellow", "width": 60, "height": 90,
    "location": (1040, 85), "file": "./tiles/29drum.jpg",
    "type": "instruments", "price_buy": 280, "price_hire": 150, "pay": 24,
    "pay_1hire": 120, "pay_2hire": 360, "pay_3hire": 850, "pay_4hire": 1025,
    "pay_leader": 1200, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Jail", "id": 30, "width": 90, "height": 90,
    "location": (1115, 85), "file": "./tiles/30jail.jpg", "type": "idle"})

data["tiles"].append({
    "name": "Timpani", "id": 31, "color": "green", "width": 90, "height": 60,
    "location": (1115, 160), "file": "./tiles/31tim.jpg",
    "type": "instruments", "price_buy": 300, "price_hire": 200, "pay": 26,
    "pay_1hire": 130, "pay_2hire": 390, "pay_3hire": 900, "pay_4hire": 1100,
    "pay_leader": 1275, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Cymbal", "id": 32, "color": "green", "width": 90, "height": 60,
    "location": (1115, 220), "file": "./tiles/32cym.jpg",
    "type": "instruments", "price_buy": 300, "price_hire": 200, "pay": 26,
    "pay_1hire": 130, "pay_2hire": 390, "pay_3hire": 900, "pay_4hire": 1100,
    "pay_leader": 1275, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Music Chest", "id": 33, "width": 90, "height": 60,
    "location": (1115, 280), "file": "./tiles/33chest.jpg", "type": "chest"})

data["tiles"].append({
    "name": "Marimba", "id": 34, "color": "green", "width": 90, "height": 60,
    "location": (1115, 340), "file": "./tiles/34mar.jpg",
    "type": "instruments", "price_buy": 320, "price_hire": 200, "pay": 28,
    "pay_1hire": 150, "pay_2hire": 450, "pay_3hire": 1000, "pay_4hire": 1200,
    "pay_leader": 1400, "musician": 0, "leader": 0, "monopoly_size": 3,
    "bought_status": False})

data["tiles"].append({
    "name": "Sibelius Hall", "id": 35, "width": 90, "height": 60,
    "location": (1115, 400), "file": "./tiles/35sib.jpg", "type": "musichalls",
    "price_buy": 200, "pay": 25, "bought_status": False})

data["tiles"].append({
    "name": "Chance", "id": 36, "width": 90, "height": 60,
    "location": (1115, 460), "file": "./tiles/36chance.jpg", "type": "chance"})

data["tiles"].append({
    "name": "Viola", "id": 37, "color": "blue", "width": 90, "height": 60,
    "location": (1115, 520), "file": "./tiles/37vla.jpg",
    "type": "instruments", "price_buy": 350, "price_hire": 200, "pay": 35,
    "pay_1hire": 175, "pay_2hire": 500, "pay_3hire": 1100, "pay_4hire": 1300,
    "pay_leader": 1500, "musician": 0, "leader": 0, "monopoly_size": 2,
    "bought_status": False})

data["tiles"].append({
    "name": "Luxury Tax", "id": 38, "width": 90, "height": 60,
    "location": (1115, 580), "file": "./tiles/38lt.jpg", "type": "tax"})

data["tiles"].append({
    "name": "Baton", "id": 39, "color": "blue", "width": 90, "height": 60,
    "location": (1115, 640), "file": "./tiles/39baton.jpg",
    "type": "instruments", "price_buy": 400, "price_hire": 200, "pay": 50,
    "pay_1hire": 200, "pay_2hire": 600, "pay_3hire": 1400, "pay_4hire": 1700,
    "pay_leader": 2000, "musician": 0, "leader": 0, "monopoly_size": 2,
    "bought_status": False})

data["chestcards"] = [{"id": 1, "file": "./chest/1.jpg"},
                      {"id": 2, "file": "./chest/2.jpg"},
                      {"id": 3, "file": "./chest/3.jpg"},
                      {"id": 4, "file": "./chest/4.jpg"},
                      {"id": 5, "file": "./chest/5.jpg"},
                      {"id": 6, "file": "./chest/6.jpg"},
                      {"id": 7, "file": "./chest/7.jpg"},
                      {"id": 8, "file": "./chest/8.jpg"},
                      {"id": 9, "file": "./chest/9.jpg"},
                      {"id": 10, "file": "./chest/10.jpg"},
                      {"id": 11, "file": "./chest/11.jpg"},
                      {"id": 12, "file": "./chest/12.jpg"},
                      {"id": 13, "file": "./chest/13.jpg"},
                      {"id": 14, "file": "./chest/14.jpg"},
                      {"id": 15, "file": "./chest/15.jpg"}]

data["chancecards"] = [{"id": 1, "file": "./chance/1.jpg"},
                       {"id": 2, "file": "./chance/2.jpg"},
                       {"id": 3, "file": "./chance/3.jpg"},
                       {"id": 4, "file": "./chance/4.jpg"},
                       {"id": 5, "file": "./chance/5.jpg"},
                       {"id": 6, "file": "./chance/6.jpg"},
                       {"id": 7, "file": "./chance/7.jpg"},
                       {"id": 8, "file": "./chance/8.jpg"},
                       {"id": 9, "file": "./chance/9.jpg"},
                       {"id": 10, "file": "./chance/10.jpg"},
                       {"id": 11, "file": "./chance/11.jpg"},
                       {"id": 12, "file": "./chance/12.jpg"},
                       {"id": 13, "file": "./chance/13.jpg"},
                       {"id": 14, "file": "./chance/14.jpg"},
                       {"id": 15, "file": "./chance/15.jpg"}]

# Dumps the data into tile.txt.
with open("tile.txt", "w") as outfile:
    json.dump(data, outfile)

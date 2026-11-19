from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.get("/")
    def home():
        return render_template("index.html")

    @app.get("/linkin-park")
    def linkin_park():
        members = [
            {
                "name": "Mike Shinoda",
                "role": "Voz, guitarra, teclados y programación",
                "departure": "Continúa en la banda",
            },
            {
                "name": "Brad Delson",
                "role": "Guitarra y coros",
                "departure": "Continúa en la banda",
            },
            {
                "name": "Dave “Phoenix” Farrell",
                "role": "Bajo y coros",
                "departure": "Continúa; tuvo una salida temporal en 1999 y regresó en 2000",
            },
            {
                "name": "Joe Hahn",
                "role": "Tornamesas, samples y programación",
                "departure": "Continúa en la banda",
            },
            {
                "name": "Chester Bennington",
                "role": "Voz",
                "departure": "2017; fue integrante hasta su fallecimiento",
            },
            {
                "name": "Rob Bourdon",
                "role": "Batería",
                "departure": "2024",
            },
            {
                "name": "Mark Wakefield",
                "role": "Voz en la etapa inicial de Xero",
                "departure": "1998",
            },
            {
                "name": "Emily Armstrong",
                "role": "Voz",
                "departure": "Continúa en la banda; se incorporó en 2024",
            },
            {
                "name": "Colin Brittain",
                "role": "Batería y composición",
                "departure": "Continúa en la banda; se incorporó en 2024",
            },
        ]
        songs = [
            {
                "title": "Two Faced",
                "album": "From Zero (2024)",
                "deezer_id": "3068802321",
            },
            {
                "title": "Points of Authority",
                "album": "Hybrid Theory (2000)",
                "deezer_id": "676168",
            },
            {
                "title": "One Step Closer",
                "album": "Hybrid Theory (2000)",
                "deezer_id": "676162",
            },
            {
                "title": "Over Each Other",
                "album": "From Zero (2024)",
                "deezer_id": "3068802291",
            },
        ]
        return render_template("linkin_park.html", members=members, songs=songs)

    @app.get("/maneskin")
    def maneskin():
        members = [
            {
                "name": "Damiano David",
                "role": "Voz principal",
                "departure": "No ha salido; miembro fundador desde 2016",
            },
            {
                "name": "Victoria De Angelis",
                "role": "Bajo",
                "departure": "No ha salido; miembro fundadora desde 2016",
            },
            {
                "name": "Thomas Raggi",
                "role": "Guitarra",
                "departure": "No ha salido; miembro fundador desde 2016",
            },
            {
                "name": "Ethan Torchio",
                "role": "Batería",
                "departure": "No ha salido; miembro fundador desde 2016",
            },
        ]
        songs = [
            {
                "title": "THE DRIVER",
                "album": "RUSH! (ARE U COMING?) (2023)",
                "deezer_id": "2536405591",
            },
            {
                "title": "READ YOUR DIARY",
                "album": "RUSH! (2023)",
                "deezer_id": "2111636507",
            },
            {
                "title": "L'altra dimensione",
                "album": "Il ballo della vita (2018)",
                "deezer_id": "570478742",
            },
            {
                "title": "FOR YOUR LOVE",
                "album": "Teatro d'ira: Vol. I (2021)",
                "deezer_id": "1279728552",
            },
        ]
        return render_template("maneskin.html", members=members, songs=songs)

    @app.get("/red-hot-chili-peppers")
    def red_hot_chili_peppers():
        members = [
            {
                "name": "Anthony Kiedis",
                "role": "Voz principal",
                "departure": "Continúa en la banda; miembro fundador desde 1982",
            },
            {
                "name": "Flea (Michael Balzary)",
                "role": "Bajo y coros",
                "departure": "Continúa en la banda; miembro fundador desde 1982",
            },
            {
                "name": "Chad Smith",
                "role": "Batería",
                "departure": "Continúa en la banda; se incorporó en 1988",
            },
            {
                "name": "John Frusciante",
                "role": "Guitarra y coros",
                "departure": "Salió en 1992 y 2009; regresó en 1998 y 2019",
            },
            {
                "name": "Hillel Slovak",
                "role": "Guitarra",
                "departure": "1988; falleció ese año",
            },
            {
                "name": "Jack Irons",
                "role": "Batería",
                "departure": "1988; dejó la banda tras la muerte de Hillel Slovak",
            },
            {
                "name": "Jack Sherman",
                "role": "Guitarra",
                "departure": "1984",
            },
            {
                "name": "Cliff Martinez",
                "role": "Batería",
                "departure": "1986",
            },
            {
                "name": "DeWayne McKnight",
                "role": "Guitarra",
                "departure": "1988",
            },
            {
                "name": "D. H. Peligro",
                "role": "Batería",
                "departure": "1988",
            },
            {
                "name": "Arik Marshall",
                "role": "Guitarra",
                "departure": "1992",
            },
            {
                "name": "Jesse Tobias",
                "role": "Guitarra",
                "departure": "1992",
            },
            {
                "name": "Dave Navarro",
                "role": "Guitarra",
                "departure": "1998",
            },
            {
                "name": "Josh Klinghoffer",
                "role": "Guitarra y coros",
                "departure": "2019",
            },
        ]
        songs = [
            {
                "title": "Peace and Love",
                "album": "Return of the Dream Canteen (2022)",
                "deezer_id": "1928560187",
            },
            {
                "title": "Can't Stop",
                "album": "By the Way (2002)",
                "deezer_id": "725971",
            },
            {
                "title": "Parallel Universe",
                "album": "Californication (1999)",
                "deezer_id": "725249",
            },
            {
                "title": "Universally Speaking",
                "album": "By the Way (2002)",
                "deezer_id": "725937",
            },
        ]
        return render_template(
            "red_hot_chili_peppers.html",
            members=members,
            songs=songs,
        )

    @app.get("/fall-out-boy")
    def fall_out_boy():
        members = [
            {
                "name": "Patrick Stump",
                "role": "Voz principal, guitarra y composición",
                "departure": "Continúa en la banda; miembro fundador",
            },
            {
                "name": "Pete Wentz",
                "role": "Bajo y letras",
                "departure": "Continúa en la banda; miembro fundador",
            },
            {
                "name": "Joe Trohman",
                "role": "Guitarra",
                "departure": "Continúa en la banda; hizo una pausa temporal en 2023",
            },
            {
                "name": "Andy Hurley",
                "role": "Batería",
                "departure": "Continúa en la banda",
            },
        ]
        songs = [
            {
                "title": "ACES",
                "album": "ACES (sencillo)",
                "deezer_id": "4396738761",
            },
            {
                "title": "Dance, Dance",
                "album": "From Under the Cork Tree (2005)",
                "deezer_id": "1138246",
            },
            {
                "title": "Grand Theft Autumn / Where Is Your Boy",
                "album": "Take This to Your Grave (2003)",
                "deezer_id": "804595",
            },
            {
                "title": "Love From The Other Side",
                "album": "So Much (for) Stardust (2023)",
                "deezer_id": "2108162157",
            },
        ]
        return render_template("fall_out_boy.html", members=members, songs=songs)

    return app

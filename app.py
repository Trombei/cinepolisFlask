from flask import Flask, render_template, request, redirect, url_for, flash
from forms import CompraForm
import os

app = Flask(__name__)
app.secret_key = os.urandom(24) 

cartelera = [
    {"id": 1, "titulo": "The Brutalist", "poster": "https://th.bing.com/th/id/R.86fc48e5cfcddb50c4cf032de34e34c7?rik=Un8UHDAwHwMGHQ&riu=http%3a%2f%2fwww.impawards.com%2f2024%2fposters%2fbrutalist_ver4.jpg&ehk=pkK2wgP%2fqVjarQNjMwxBO2jNi93t3rP1XA1b5jr7pHU%3d&risl=&pid=ImgRaw&r=0", "sinopsis": "The Brutalist es un drama histórico que sigue la vida de László Tóth, un arquitecto judío húngaro que, tras sobrevivir al Holocausto, emigra a Estados Unidos en busca del sueño americano."},
    {"id": 2, "titulo": "Trainspotting", "poster": "https://tse2.mm.bing.net/th/id/OIP.zygSxYwxGrJpuPHOws3gjAHaLA?rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "Trainspotting es una película británica de 1996 dirigida por Danny Boyle, que narra la vida de un grupo de jóvenes heroinómanos en Edimburgo, explorando temas de adicción, desilusión y búsqueda de identidad."},
    {"id": 3, "titulo": "Spencer", "poster": "https://m.media-amazon.com/images/M/MV5BMGZkOTYzMDgtMzlkMS00NTE2LWFmYTgtOTdmNjhhYjJjMWI2XkEyXkFqcGc@._V1_.jpg", "sinopsis": "Spencer es un drama biográfico que retrata un fin de semana crucial en la vida de la princesa Diana, donde decide que su matrimonio con el príncipe Carlos no está funcionando y que necesita liberarse de las restricciones de la familia real."},
    {"id": 4, "titulo": "Spider-Man: Cruzando el Multiverso", "poster": "https://tse1.mm.bing.net/th/id/OIP.rgUEz8Q4Mc97OLEnDXalAgHaK-?w=768&h=1138&rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "Más de un año después de los eventos de Spider-Man: un nuevo universo (2018), Miles Morales es inesperadamente abordado por su interés amoroso Gwen Stacy para completar una misión para salvar cada universo de la Mancha, un peligroso antagonista, pero sin experiencia, que podría causar un desastre catastrófico."},
    {"id": 5, "titulo": "El Resplandor", "poster": "https://tse1.explicit.bing.net/th/id/OIP.Mpcdk8PCV9fpLM-zO8W0qwHaLH?rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "El Resplandor es una película de terror psicológico dirigida por Stanley Kubrick, que narra la historia de Jack Torrance, un escritor que se convierte en el cuidador de un hotel aislado, donde su salud mental se deteriora debido a fuerzas sobrenaturales y su propia psique."},
    {"id": 6, "titulo": "La Leyenda Del Tesoro Perdido", "poster": "https://tse1.mm.bing.net/th/id/OIP.M5_olr4LCHrrxzrSfrIl1wHaJ4?rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "La Leyenda Del Tesoro Perdido sigue a Benjamin Franklin Gates, un historiador aficionado a la criptología y descendiente de una familia de buscadores de tesoros. Gates descubre una pista para un tesoro escondido por los Padres Fundadores de los Estados Unidos, que se encuentra en el reverso de la Declaración de Independencia."},
    {"id": 7, "titulo": "Carrie", "poster": "https://filmfilicos.com/wp-content/uploads/2017/04/carrie-cartel.jpg", "sinopsis": "Carrie es una película de terror dirigida por Brian De Palma, basada en la novela de Stephen King, que narra la historia de una adolescente tímida que descubre sus poderes telequinésicos tras ser humillada por sus compañeros."},
    {"id": 8, "titulo": "Los Juegos del Hambre: En llamas", "poster": "https://th.bing.com/th/id/R.c60eb108fcfb135f1566a1887eb4d8fb?rik=Kt%2bllRjHwwvzhA&pid=ImgRaw&r=0", "sinopsis": "Los Juegos del Hambre: En llamas es la segunda entrega de la saga, una película de acción distópica de 2013 protagonizada por Jennifer Lawrence que continúa la historia de Katniss Everdeen y Peeta Mellark enfrentando nuevos desafíos en Panem."},
    {"id": 9, "titulo": "Megalopolis", "poster": "https://www.filmofilia.com/wp-content/uploads/2024/08/Megalopolis-Poster-1-scaled.webp", "sinopsis": "Megalópolis es una fábula épica romana ambientada en una América moderna imaginada, donde César Catilina, un artista idealista, busca transformar la ciudad de Nueva Roma, enfrentándose al alcalde Franklyn Cicero, quien defiende un statu quo regresivo."},
    {"id": 10, "titulo": "Zack Snyder's Justice League", "poster": "https://tse3.mm.bing.net/th/id/OIP.1MXDirdlR6OTvAYmqQUWyQHaLH?rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "Hace cinco mil años, Darkseid (Ray Porter) y su ejército de Parademonios intentaron conquistar la Tierra utilizando las tres Cajas Madre. El intento fue frustrado por una alianza unificada de Antiguos Dioses, Amazonas, Atlantes, Hombres y un Linterna Verde, y las Cajas Madre fueron dejadas atrás involuntariamente durante su retirada."},
    {"id": 11, "titulo": "Frozen II", "poster": "https://th.bing.com/th/id/R.2d5967408679170b79ee0729ee57ec75?rik=1fxZ%2fwrDugc0Fw&riu=http%3a%2f%2fwww.impawards.com%2f2019%2fposters%2ffrozen_two_ver22.jpg&ehk=hA8FtITCXkTMrOngYCte4fAlXzBAYMOcuolzDZZ8kvY%3d&risl=&pid=ImgRaw&r=0", "sinopsis": "Frozen II es la secuela donde Elsa, Anna, Kristoff, Olaf y Sven emprenden un viaje para descubrir el origen de los poderes mágicos de Elsa y salvar su reino de Arendelle."},
    {"id": 12, "titulo": "Todo en todas partes al mismo tiempo", "poster": "https://tse4.mm.bing.net/th/id/OIP.k9tBwAhyZoeq5FfP32yElQHaKl?rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "Todo en todas partes al mismo tiempo es una película que sigue a Evelyn, una inmigrante china que se ve envuelta en una aventura interdimensional para salvar el multiverso."},
    {"id": 13, "titulo": "Bardo", "poster": "https://quinlan.it/upload/images/2022/09/Bardo-2022-Inarritu-poster.jpg", "sinopsis": "Bardo es una película de comedia dramática dirigida por Alejandro González Iñárritu que narra el viaje existencial de Silverio, un periodista y documentalista mexicano que regresa a su país tras recibir un prestigioso premio."},
    {"id": 14, "titulo": "El Señor De Los Anillos El Retorno Del Rey", "poster": "https://pics.filmaffinity.com/El_se_or_de_los_anillos_El_retorno_del_rey-164432989-large.jpg", "sinopsis": "El Retorno del Rey culmina la épica historia de El Señor de los Anillos con la batalla final contra Sauron y el destino de la Tierra Media."},
    {"id": 15, "titulo": "The Secret Life Of Walter Mitty", "poster": "https://tse4.mm.bing.net/th/id/OIP.lOgQrpjsH13eLJzWCn1aRgHaLH?w=780&h=1170&rs=1&pid=ImgDetMain&o=7&rm=3", "sinopsis": "The Secret Life Of Walter Mitty es una película que sigue a un tímido editor fotográfico que, atrapado en su monótona vida, se embarca en una aventura extraordinaria para encontrar un negativo perdido y descubrir su verdadero potencial."},
    {"id": 16, "titulo": "Sing Street", "poster": "https://th.bing.com/th/id/R.83922f9bb4164c1a7febf4219c2ee8b5?rik=9vs%2f8vD3B3LzDA&riu=http%3a%2f%2fwww.impawards.com%2f2016%2fposters%2fsing_street.jpg&ehk=4PEWT85j7n%2fKHYLKYt1Om%2fda6QU56AzUaOYOgUa1eC0%3d&risl=&pid=ImgRaw&r=0", "sinopsis": "Sing Street es una película que explora la vida de Conor, un joven que, tras la recesión económica en Dublín, se ve forzado a cambiar de escuela y enfrentar un entorno más tenso. A través de su búsqueda de identidad y sueños, Conor forma una banda de música para impresionar a Raphina, una chica misteriosa y cool."}
]

@app.route('/')
def index():
    return render_template('index.html', peliculas=cartelera)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    peli = next((p for p in cartelera if p["id"] == movie_id), None)
    return render_template('movie.html', peli=peli)

@app.route('/buy/<int:movie_id>', methods=['GET', 'POST'])
def buy(movie_id):
    peli = next((p for p in cartelera if p["id"] == movie_id), None)
    form = CompraForm()

    if form.validate_on_submit():
        flash(f'¡Compra correcta! Tus boletos para {peli["titulo"]} fueron enviados a {form.correo.data}', 'success')
        return redirect(url_for('index'))

    return render_template('buy.html', form=form, peli=peli)

if __name__ == '__main__':
    app.run(debug=True)
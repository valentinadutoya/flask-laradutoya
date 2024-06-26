from . import db
from flask import Blueprint, render_template

bp = Blueprint('peliculas', __name__,url_prefix='/pelicula')

@bp.route('/')
def pelis():
    consulta = """
            SELECT title,film_id FROM film 
            ORDER by title ASC
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_peliss = res.fetchall()
    pagina = render_template('Peliculas.html', peliculas= lista_peliss) 

    return pagina

@bp.route('/<int:id>/detalle')
def detalles(id):
            con=db.get_db()
            consulta = """
            SELECT f.title,f.description,f.length,f.rating,f.release_year, l.name as language , l.language_id 
            FROM  film f
            JOIN language l on of f.language_id = l.language_id
             WHERE f.film_id = ?;
            """

            consulta2 = """
            SELECT first_name,last_name,a.actor_id FROM film_actor fa 
            JOIN actor a on fa.actor_id = a.actor_id  
            WHERE fa.film_id = ?
            """

            resultado= con.execute(consulta,(id,))   
            ppelis = resultado.fetchone()
            
            resultado= con.execute(consulta2,(id,))   
            lista_pelicula = resultado.fetchall()

            
            pagina = render_template('detallePeliculas.html', peli = ppelis , pelicula =  lista_pelicula)

            return pagina      
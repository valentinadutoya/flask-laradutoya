from . import db
from flask import Blueprint, render_template

bp = Blueprint('peliculas', __name__,url_prefix='/peliculas')

@bp.route('/')
def lenguaje():
    consulta = """
            SELECT title FROM film 
            ORDER by title ASC
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_peliss = res.fetchall()
    pagina = render_template('Peliculas.html', peliculas= lista_peliss) 

    return pagina

@bp.route('/<int:id>/detalle')
def detalless(id):
            con=db.get_db()
            consulta = """
            SELECT title FROM  film
             WHERE film_id = ?
            """

            consulta2 = """
           SELECT  FROM  
           
           WHERE 
            """

            resultado= con.execute(consulta,(id,))   
            ppelis = resultado.fetchone()
            
            resultado= con.execute(consulta2,(id,))   
            lista_pelis = resultado.fetchall()

            
            pagina = render_template('detallePeliculas.html', peli = ppelis , pelis=lista_pelis)

            return pagina      
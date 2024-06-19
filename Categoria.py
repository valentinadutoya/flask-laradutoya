from . import db
from flask import Blueprint, render_template

bp = Blueprint('peliculas', __name__,url_prefix='/peliculas')

@bp.route('/')
def lenguaje():
    consulta = """
             SELECT name FROM category 
            ORDER by name ASC
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
                SELECT name FROM category
                WHERE category_id = 4
            """

            consulta2 = """
                SELECT f.title as pelicula,c.name as categoria ,c.category_id FROM film f 
                JOIN film_category fc on f.film_id = fc.film_id
                JOIN category c on fc.category_id = c.category_id
                WHERE c.category_id = ? 
                    
            """

            resultado= con.execute(consulta,(id,))   
            categoria = resultado.fetchone()
            
            resultado= con.execute(consulta2,(id,))   
            lista_categoria = resultado.fetchall()

            
            pagina = render_template('detalleCategoria.html', cat= categoria , categorias=lista_categoria)

            return pagina      
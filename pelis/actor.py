from . import db
from flask import Blueprint, render_template

bp = Blueprint('actor', __name__,url_prefix='/actor')

@bp.route('/')
def Actor():
    consulta = """
        SELECT first_name, last_name FROM actor
        ORDER BY last_name, first_name; 
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_Actor = res.fetchall()
    pagina = render_template('Actor.html', actores=lista_Actor)

    return pagina

@bp.route('/<int:id>/detalle')
def detalle(id):
            con=db.get_db()
            consulta = """
            SELECT a.first_name,a.last_name, f.title, a.actor_id FROM actor a 
            JOIN film_actor fa ON a.actor_id = fa.actor_id
            JOIN film f ON fa.film_id = f.film_id
            WHERE a.actor_id = ?
            GROUP BY f.film_id"""
                
            resultado= con.execute(consulta,(id,))   
            actor = {"nombre": resultado[actor],"id" : resultado["a.actor_id"]}
            detalleActor = resultado["actor"]
            actor = resultado.fetchone()    
            pagina = render_template('detalleActor.html', act=actor)

            return pagina      
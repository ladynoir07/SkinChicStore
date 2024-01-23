from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = '123'

@app.route('/carrito')
def ver_carrito():
    carrito = session.get('carrito', [])
    return render_template('carrito.html', carrito=carrito)

@app.route('/agregar_carrito/<int:producto_id>')
def agregar_carrito(producto_id):
    producto = obtener_producto_por_id(producto_id)
    if producto:
        carrito = session.get('carrito', [])
        carrito.append(producto)
        session['carrito'] = carrito
        flash('Producto agregado al carrito', 'success')
    else:
        flash('Producto no encontrado', 'error')
    return redirect(url_for('ver_carrito'))

@app.route('/eliminar_producto/<int:producto_id>')
def eliminar_producto(producto_id):
    carrito = session.get('carrito', [])
    carrito = [producto for producto in carrito if producto['id'] != producto_id]
    session['carrito'] = carrito
    flash('Producto eliminado del carrito', 'success')
    return redirect(url_for('ver_carrito'))

@app.route('/realizar_compra')
def realizar_compra():
    carrito = session.pop('carrito', [])
    flash('Compra realizada con éxito', 'success')
    return redirect(url_for('ver_carrito'))

def obtener_producto_por_id(producto_id):
    productos = {
        1: {'id': 1, 'nombre': 'Producto 1', 'precio': 10.0},
        2: {'id': 2, 'nombre': 'Producto 2', 'precio': 15.0},

    }
    return productos.get(producto_id)

if __name__ == '__main__':
    app.run(debug=True)

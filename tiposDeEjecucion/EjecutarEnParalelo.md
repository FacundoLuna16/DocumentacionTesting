# Ejecucion en paralelo con Pytest
Esto nos permite ahorrarnos tiempo, optimizando nuestros recursos. 
pytest nos ofrece una libreria llamada `pytest-xdist`, que debemos intalar con pip

```bash
pip install pytest-xdist
```
> documentacion en este [link](https://pytest-xdist.readthedocs.io/en/stable/)
##### Una de las primeras opciones que nos brinda esta libreria es `-n auto`
ejemplo de uso 
```bash
 pytest -n auto
```
esta opcion genera cada test en distintos hilos de nuestro procesador, ejecutandolos en paralelo


##### 
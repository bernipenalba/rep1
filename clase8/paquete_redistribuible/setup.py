from setuptools import setup

#este setup va a recibir algunos argumentos
setup (
    name = "paquete_segunda_preentrega_Peñalba",
    version = "1.0",
    description = "Paquete distribuido",
    author = "Bernardita Peñalba",
    author_email = "00000@gmail.com",
    packages = ["carpetaModulos"] #nombre de la carpeta donde esten guardados los archivos donde yo escribi mi codigo. Si no coincide con el nombre de la carpeta donde estan mis archivos, cuando se cree el paqiete va a estar vacio (sin nada adentro)
)
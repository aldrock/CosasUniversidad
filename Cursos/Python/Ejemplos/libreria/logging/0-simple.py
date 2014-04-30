import logging

# incluir filemode="w" para sobreescribir
# cambiar level a logging.DEBUG para ver todo
logging.basicConfig(filename="simple.log",\
		 level=logging.DEBUG, filemode="w")

logging.debug("Mensaje de debug")
logging.info("Mensaje de informacion")
logging.error("Mensaje de error!!!")




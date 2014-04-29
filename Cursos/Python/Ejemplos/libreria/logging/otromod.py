import logging

module_logger = logging.getLogger("Curso.otromod")

def add0(x, y):
    logging.info("sumados {0} y {1} para obtener {2}".format(x, y, x+y))
    return x+y

def add1(x, y):
	logger = logging.getLogger("Curso.otromod.add1")
	logger.info("sumados {0} y {1} para obtener {2}".format(x, y, x+y))
	return x+y


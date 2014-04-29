import logging
import logging.config
import otromod


def main():
	logging.config.fileConfig('3-config.cfg')
	logger = logging.getLogger("Curso")

	logger.info("Program started")
	result = otromod.add1(7, 8)
	logger.info("Done!")


if __name__ == "__main__":
	main()
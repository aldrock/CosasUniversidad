import logging
import otromod


def main():
	logger = logging.getLogger("Curso")
	logger.setLevel(logging.INFO)
	
	fh = logging.FileHandler("hardcoded.log")
	formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
	fh.setFormatter(formatter)
	
	logger.addHandler(fh)
	logger.info("Program started")
	result = otromod.add1(7, 8)
	logger.info("Done!")


if __name__ == "__main__":
	main()
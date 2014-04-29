import logging
import otromod

def main():
    logging.basicConfig(filename="simple_multiple.log", level=logging.INFO)
    logging.info("Programa iniciado")
    res = otromod.add0(7,8)
    logging.info("Final!")

if __name__ == "__main__":
    main()

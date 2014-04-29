import logging
import logging.config
import otromod


def main():
	dictLogConfig = {
		"version":1,
		"handlers":{
			"fileHandler":{
				"class":"logging.FileHandler",
				"formatter":"myFormatter",
				"filename":"dict.log"
			}
		},
		"loggers":{
			"Curso":{
				"handlers":["fileHandler"],
				"level":"INFO",
			}
		},
		"formatters":{
			"myFormatter":{
			"format":"%(asctime)s - %(name)s - %(levelname)s - %(message)s"
			}
		}
	}

	logging.config.dictConfig(dictLogConfig)
	logger = logging.getLogger("Curso")

	logger.info("Program started")
	result = otromod.add1(7, 8)
	logger.info("Done!")


if __name__ == "__main__":
	main()
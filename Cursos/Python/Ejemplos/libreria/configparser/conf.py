import configparser as ConfigParser
import os
import sys

def createConfig(path):
    config = ConfigParser.ConfigParser()
    config.add_section("Curso")
    config.set("Curso", "nivel", "1")
    config.set("Curso", "dia", "2")
    config.set("Curso", "conocimiento", "it's over 9000!")

    with open(path, "w") as config_file:
        config.write(config_file)



def change_conf(path, section, option, value):
    if not os.path.exists(path):
        createConfig(path)

    config = ConfigParser.ConfigParser()
    #config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read(path)

    config.set(section, option, value)
    with open(path, "w") as f:
        config.write(f)


def remove_opt(path, section, option):
    if not os.path.exists(path):
        createConfig(path)

    config = ConfigParser.ConfigParser()
    #config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read(path)

    config.remove_option(section, option)
    with open(path, "w") as f:
        config.write(f)


def printConfig(path):
    if not os.path.exists(path):
        createConfig(path)

    config = ConfigParser.ConfigParser()
    #config = ConfigParser.SafeConfigParser(allow_no_value=True)
    config.read(path)

    nivel = config.get("Curso", "nivel")
    dia = config.get("Curso", "dia")
    conocimiento = config.get("Curso", "conocimiento")

    print("Nivel: {0}, Dia: {1}, Conocimiento: {2}".format(nivel, dia, conocimiento))





def printhelp(*args):
    print("+Use: {} <action> [section] [option] [value]".format(args[0]))
    print("\t-actions: create/print/modify/remove")
    print("\t-modify and remove need section and option (value can be empty)")
    exit(1)


def main():
    if len(sys.argv) < 2:
        printhelp(*sys.argv)
    action = sys.argv[1]
    if action == "create":
        createConfig("cfg_test.cfg")
        exit(0)
    if action == "print":
        printConfig("cfg_test.cfg")
        exit(0)
    if (action != "modify" or action != "remove") and (len(sys.argv) < 4 or len(sys.argv) > 5):
        printhelp(*sys.argv)
    section = sys.argv[2]
    option = sys.argv[3]
    if len(sys.argv)==4:
        value = ""
    else:
        value = sys.argv[4]

    if action == "modify":
        change_conf("cfg_test.cfg", section, option, value)
        exit(0)
    if action == "remove":
        remove_opt("cfg_test.cfg", section, option)
        exit(0)


if __name__ == "__main__":
    main()


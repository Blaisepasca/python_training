# import logging
# logging(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     datefmt='%Y-%m-%d %H:%M:%S')
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

import logging

logging.basicConfig(level=logging.INFO)

logging.info("Programme démarré")
logging.warning("Attention, quelque chose semble étrange")
logging.error("Une erreur est survenue")


import logging

# Configuration de base du logging
logging.basicConfig(level=logging.INFO)

# Utilisation
logging.info("Bonjour, ceci est un message d'information")
logging.warning("Attention ! Ceci est un avertissement")
logging.error("Oups ! Une erreur est survenue")


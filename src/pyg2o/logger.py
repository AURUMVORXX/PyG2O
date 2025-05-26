import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
handler.setLevel(logging.INFO)

formatter = logging.Formatter('[%(levelname)s][PyG2O] - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
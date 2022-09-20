
import logging
import os



class Logger:
    """Logger class for logging messages to a file."""

    def __init__(self, file_name: str='logs.log', level=logging.INFO):
        """Initilize logger class with file name to be written and default log level.
        Args:
            file_name(str): _description_
            basic_level(_type_, optional): _description_. Defaults to logging.INFO.
        """

        path = "../logs"
        # Check whether the specified path exists or not
        isExist = os.path.exists(path)

        # Create a new directory because it does not exist 
        if not isExist:
            os.makedirs(path)

        #  # Gets or creates a logger
        logger = logging.getLogger(__name__)

        logging.basicConfig(filename=f'../logs/{file_name}', encoding='utf-8', level=level,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        self.logger = logger

    def get_app_logger(self) -> logging.Logger:
        """Return the logger object.
        Returns:
            logging.Logger: logger object.
        """
        return self.logger
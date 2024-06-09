import pickle

def load_pkl_file(path:str):
    """
    Loads a pickle file from the specified path.

    Args:
        path (str): The path to the pickle file.

    Raises:
        FileNotFoundError: If the file at the specified path does not exist.
        IOError: If there is an error opening the file.
        pickle.UnpicklingError: If there is an error unpickling the file.

    Returns:
        Any: The object stored in the pickle file.
    """

    try:
        with open(path, 'rb') as f:
            name = pickle.load(f)

        return name

    except FileNotFoundError as fnf_error:
        raise FileNotFoundError(f"The file at path {path} does not exist.") from fnf_error

    except IOError as io_error:
        raise IOError(f" An error occurred while opening the file at path {path}") from io_error

    except pickle.UnpicklingError as up_error:
        raise pickle.UnpicklingError(f"An error occurred while unpickling the file at path {path}") from up_error

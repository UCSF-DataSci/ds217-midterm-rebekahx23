#!/usr/bin/env python3
# Assignment 5, Question 2: Python Data Processing
# Process configuration files for data generation.
#!/usr/bin/env python3

from numpy import mean, median


def parse_config(filepath: str) -> dict:
    """
    Parse config file (key=value format) into dictionary.

    Args:
        filepath: Path to q2_config.txt

    Returns:
        dict: Configuration as key-value pairs

    Example:
        >>> config = parse_config('q2_config.txt')
        >>> config['sample_data_rows']
        '100'
    """
    # TODO: Read file, split on '=', create dict
    with open(filepath, 'r') as file:
        content = file.read()
        file_content = content.splitlines()
        create_dict = {}
        for i in file_content:
            results = i.split('=')
            key = results[0]
            value = results[1]
            create_dict[key] = value
        return create_dict
   
        
def validate_config(config: dict) -> dict:
    """
    Validate configuration values using if/elif/else logic.

    Rules:
    - sample_data_rows must be an int and > 0
    - sample_data_min must be an int and >= 1
    - sample_data_max must be an int and > sample_data_min

    Args:
        config: Configuration dictionary

    Returns:
        dict: Validation results {key: True/False}

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> results = validate_config(config)
        >>> results['sample_data_rows']
        True
    """
    # TODO: Implement with if/elif/else
    create_dict = {}
    if int(config['sample_data_rows']) > 0:
        create_dict["sample_data_rows"] = True
    if int(config['sample_data_min']) >= 1:
        create_dict["sample_data_min"] = True
    if int(config['sample_data_max']) > int(config['sample_data_min']):
        create_dict["sample_data_max"] = True
    return create_dict


def generate_sample_data(filename: str, config: dict) -> None:
    """
    Generate a file with random numbers for testing, one number per row with no header.
    Uses config parameters for number of rows and range.

    Args:
        filename: Output filename (e.g., 'sample_data.csv')
        config: Configuration dictionary with sample_data_rows, sample_data_min, sample_data_max

    Returns:
        None: Creates file on disk

    Example:
        >>> config = {'sample_data_rows': '100', 'sample_data_min': '18', 'sample_data_max': '75'}
        >>> generate_sample_data('sample_data.csv', config)
        # Creates file with 100 random numbers between 18-75, one per row
        >>> import random
        >>> random.randint(18, 75)  # Returns random integer between 18-75
    """
    # TODO: Parse config values (convert strings to int)
    # TODO: Generate random numbers and save to file
    # TODO: Use random module with config-specified range
    import random
    sample_data_rows = config['sample_data_rows']
    min_num = config['sample_data_min']
    max_num = config['sample_data_max']
    with open(filename, 'w') as file:
        for i in range(int(sample_data_rows)):
            random_int = random.randint(int(min_num), int(max_num))
            print(random_int, file=file)


def calculate_statistics(data: list) -> dict:
    """
    Calculate basic statistics.

    Args:
        data: List of numbers

    Returns:
        dict: {mean, median, sum, count}

    Example:
        >>> stats = calculate_statistics([10, 20, 30, 40, 50])
        >>> stats['mean']
        30.0
    """
    # TODO: Calculate stats
    create_dict = {}
    create_dict['mean'] = float(mean(data))
    create_dict['median'] = float(median(data))
    create_dict['sum'] = sum(data)
    create_dict['count'] = len(data)
    return create_dict



if __name__ == '__main__':
    # TODO: Test your functions with sample data
    # Example:
    # config = parse_config('q2_config.txt')
    # validation = validate_config(config)
    # generate_sample_data('data/sample_data.csv', config)
    # 
    # TODO: Read the generated file and calculate statistics
    # TODO: Save statistics to output/statistics.txt
    config = parse_config('q2_config.txt')
    print(config)
    validation = validate_config(config)
    print(validation)
    generate_sample_data('data/sample_data.csv', config)
    stats = calculate_statistics([10, 20, 30, 40, 50])
    print(stats, file=open('output/statistics.txt', 'w'))

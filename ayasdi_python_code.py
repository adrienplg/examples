# -*- coding: utf-8 -*-
"""Ayasdi python assessment"""
import csv
import sqlite3 as lite
from datetime import datetime, timedelta
from random import gauss, randrange


class SQLiteDatabase:
    """SQLite database object."""

    def __init__(self, sqlite_file):
        """Connects to a SQLite database file.

        Args:
            sqlite_file (str): name of the database to create or open.

        Example:
            >>> db_test = SQLiteDatabase('test.db')
            >>> type(db_test)
            <class 'ayasdi_python_code.SQLiteDatabase'>
            >>>
        """
        self.con = lite.connect(sqlite_file)
        self.cur = self.con.cursor()

    def create_table(self, table_name, command):
        """Drop a table in the database if it exists and create it.

        Args:
            table_name (str): name of the table to create.
            command (str): SQL command to create the table (eg. CREATE TABLE AYASDI(COL1 INTERGER))

        Example:
            >>> db_test = SQLiteDatabase('test.db')
            >>> db_test.create_table('TABLE_TEST', 'CREATE TABLE TABLE_TEST(COL1 INTEGER, \
                COL2 REAL, COL3 REAL, COL4 REAL, COL5 REAL, COL6 REAL, COL7 REAL, COL8 REAL, \
                COL9 REAL, COL10 REAL,COL11 TEXT, COL12 TEXT, COL13 TEXT, COL14 TEXT, \
                COL15 TEXT, COL16 TEXT, COL17 TEXT, COL18 TEXT, COL19 TEXT, COL20 TEXT)')
            >>>
        """
        self.cur.execute("DROP TABLE IF EXISTS " + table_name)
        self.cur.execute("" + command)

    def insert_csv(self, table_name, data):
        """ Import a CSV file in the given table

        Args:
            table_name (str): name of the table to insert the data in.
            data (str): relative path to the CSV file to import

        Example:
            >>> db_test = SQLiteDatabase('test.db')
            >>> db_test.insert_csv('TABLE_TEST', 'test.csv')
            >>>
        """
        with open(data, 'r') as csv_file:
            # Load the CSV csv_file into CSV reader
            csv_reader = csv.reader(csv_file, delimiter='\t')

            # Iterate through the CSV reader, inserting values into the database
            for row in csv_reader:
                self.cur.execute('INSERT INTO ' + table_name \
                    + ' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
            self.con.commit()

    def close(self):
        """Close the connection to the database

        Example:
            >>> db_test = SQLiteDatabase('test.db')
            >>> db_test.close()
            >>>
        """
        self.con.close()


def get_gaussian_distribution(rows, columns, means, deviations, null_pct=0):
    """ Returns a matrix (nested list) where each column has random data
        generated from a gaussian distribution.

    Args:
        rows (int): The number of rows in the matrix. Must be > 0.
        columns (int): The number of columns in the matrix. Must be > 0.
        means (list[int]): List of integers. len(means) must be >= columns.
        deviations (list[int]): List of integers. len(deviations) must be >= columns.
        null_pct (Optional[int]): The percentage of null values in each column.

    Returns:
        number_matrix (list[list][float]): The matrix holding random numbers

    Example:
        >>> random_numbers = get_gaussian_distribution(1, 1, [0], [50], 10)
        >>> type(random_numbers)
        <class 'list'>
        >>> type(random_numbers[0])
        <class 'list'>
        >>> type(random_numbers[0][0])
        <class 'float'>
        >>>
    """
    if null_pct > 100:
        raise ValueError('null_pct cannot be greater than 100')
    if rows < 1 or columns < 1:
        raise ValueError('rows and columns cannot be lower than 1')
    if len(means) < columns or len(deviations) < columns:
        raise ValueError('len(means) and len(deviations) must be >= columns')

    number_matrix = [[] for i in range(columns)] # Create empty matrix

    # Generate random numbers in the matrix
    for _ in range(rows): # For each row
        for j in range(columns): # For each column
            rand_null = randrange(100) # Random number between 0 and 99
            if rand_null < null_pct: # 'null_pct' of the time: add a cell with a null value
                number_matrix[j].append('')
            else: # Add a cell with a random gaussian value
                number_matrix[j].append(gauss(means[j], deviations[j]))

    return number_matrix


def get_random_words(rows, columns, words_file, null_pct=0):
    """ Returns a matrix (nested list) containing random strings.

    Args:
        rows (int): The number of rows in the matrix.
        columns (int): The number of columns in the matrix.
        words_file (str): Relative path to the text file holding the strings to use.
        null_pct (Optional[int]): The percentage of null values in each column.

    Returns:
        word_matrix (list[list][str]): The matrix holding random strings

    Example:
        >>> random_words = get_random_words(1, 1, 'words.txt', 10)
        >>> type(random_words)
        <class 'list'>
        >>> type(random_words[0])
        <class 'list'>
        >>> type(random_words[0][0])
        <class 'str'>
        >>>
    """
    if null_pct > 100:
        raise ValueError('null_pct cannot be greater than 100')
    if rows < 1 or columns < 1:
        raise ValueError('rows and columns cannot be lower than 1')

    words = [] # Create emply list to load the dictionary words

    # Loop through all lines (words) in the dictionary file
    with open(words_file, encoding='utf-8') as wfile:
        for line in wfile:
            words.append(line) # Add the current word to the words list
    total_words = len(words) # Save the total number of words


    word_matrix = [[] for i in range(columns)] # Create empty matrix

    for _ in range(rows): # For each row
        for j in range(columns): # For each column
            rand_null = randrange(100) # Random number between 0 and 99
            if rand_null < null_pct: # 'null_pct' of the time: add a cell with a null value
                word_matrix[j].append('')
            else: # Add a cell with a random word
                word_matrix[j].append(words[randrange(total_words)])

    return word_matrix


def get_random_dates(start, end, count):
    """ Returns a list of random dates between two given dates.

    Args:
        start (date): The start date.
        end (date): The end date.
        count (int): The total number of random dates to generate.

    Returns:
        random_dates (list[datetime]): A list of random dates.

    Example:
        >>> random_date = get_random_dates(datetime.strptime('1/1/2014', '%m/%d/%Y'), \
            datetime.strptime('2/1/2014', '%m/%d/%Y'), 1)
        >>> type(random_date)
        <class 'list'>
        >>> type(random_date[0])
        <class 'datetime.datetime'>
        >>>
    """
    random_dates = [] # Create empty list

    # Insert random dates in the list
    for _ in range(count):
        random_dates.append(random_date(start, end))

    return random_dates


def random_date(start, end):
    """ Returns a ramdom date between two given dates

    Args:
        start (date): The start date.
        end (date): The end date.

    Returns:
        (datetime): A random date

    Example:
        >>> rand_date = random_date(datetime.strptime('1/1/2014', '%m/%d/%Y'), \
            datetime.strptime('1/2/2014', '%m/%d/%Y'))
        >>> type(rand_date)
        <class 'datetime.datetime'>
        >>>
    """
    delta = end - start # Number of days between the 2 dates
    int_delta = (delta.days * 24 * 60 * 60) # Number of seconds between the 2 dates
    random_second = randrange(int_delta) # Random second within the given range
    return start + timedelta(seconds=random_second) # Start date + random sec


def write_to_csv(filename, col1, numbers, words, dates):
    """ Writes a set of matrix in a given CSV file.

    Args:
        filename (str): The relative path of the CSV file to write in.
        col1 (list[int]): List of indexes
        numbers (list[float][float]): Matrix of numbers
        words (list[str][str]): Matrix of strings
        dates (list(datetime)): List of dates

        col1, numbers, words and dates must have the same number of rows.

    Example:
        >>> write_to_csv('test.csv', [1], [[2.2],[4.5],[3.5],[2.28],[6.5],[1],[5],[6],[6.7]], \
            [['hello'],['world'],['python'],['is'],['a'],['great'],['programming'], \
            ['language'],['!']], [datetime.strptime('1/1/2014', '%m/%d/%Y')])
        >>>
    """
    if len(col1) != len(numbers[0]):
        raise ValueError('The length of the "col1" list must be equal to \
            the length of the columns in the matrix "numbers".')
    if len(col1) != len(words[0]):
        raise ValueError('The length of the "col1" list must be equal to \
            the length of the columns in the matrix "words".')

    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter='\t')

        for i, _ in enumerate(col1): # For each row
            line = [col1[i]] # Initiate the line to insert with the value from col1
            for j, _ in enumerate(numbers): # For each column in the numbers matrix
                line.append(numbers[j][i]) # Add to the line the number in the current matrix cell
            for k, _ in enumerate(words): # For each column in the words matrix
                line.append(words[k][i]) # Add to the line the word in the current matrix cell
            line.append(dates[i]) # Add the date column
            writer.writerow(line)


def main():
    """Main program

    Example:
        >>> main()
        Creation of the header row...
        Creation of the numbers matrix...
        Creation of the words matrix...
        Creation of the random dates list...
        Write data to ayasdi_assignment.csv...
        Create ayasdi_assignment.db file...
        Create AYASDI table (drop if exists)...
        Import CSV to SQLite...
        DONE
        >>>

    """
    total_rows = 10000 # Number of rows to write in the CSV file
    null_pct = 10 # Percentage of null values to insert

    # Lists of 9 random integers (between 0 and 99) for col2 to col10 respective mean and deviation
    means = [randrange(100) for __ in range(9)]
    deviations = [randrange(100) for __ in range(9)]

    print('Creation of the header row...')
    header_row = ['col1'] # Table header row
    # Adding the names of columns 2 to 10 to the header_row
    # They are labbelled like col2_x, col3_x, etc, where x is the mean defined in the means list
    for i, _ in enumerate(means):
        header_row.append('col' + str(i+2) + '_' + str(means[i]))
    # Adding the names of columns 11 to 20 simply labelled col11, col12, etc.
    for i in range(11, 21):
        header_row.append('col' + str(i))

    col1 = range(1, total_rows+1)
    # Create the numbers matrix
    print('Creation of the numbers matrix...')
    random_numbers = get_gaussian_distribution(total_rows, 9, means, deviations, null_pct)
    # Create the words matrix
    print('Creation of the words matrix...')
    random_words = get_random_words(total_rows, 9, 'words.txt', null_pct)
    # Create the date column
    print('Creation of the random dates list...')
    start_date = datetime.strptime('1/1/2014', '%m/%d/%Y')
    end_date = datetime.strptime('12/31/2014', '%m/%d/%Y')
    random_dates = get_random_dates(start_date, end_date, total_rows)

    # Writes data into the CSV file
    print('Write data to ayasdi_assignment.csv...')
    write_to_csv('ayasdi_assignment.csv', col1, random_numbers, random_words, random_dates)

    # Create a sqlite object
    print('Create ayasdi_assignment.db file...')
    sqlite_db = SQLiteDatabase('ayasdi_assignment.db')

    # Create table SQL command
    command = ['CREATE TABLE AYASDI(',
               header_row[0], ' INTEGER PRIMARY KEY, ',
               header_row[1], ' REAL, ',
               header_row[2], ' REAL, ',
               header_row[3], ' REAL, ',
               header_row[4], ' REAL, ',
               header_row[5], ' REAL, ',
               header_row[6], ' REAL, ',
               header_row[7], ' REAL, ',
               header_row[8], ' REAL, ',
               header_row[9], ' REAL, ',
               header_row[10], ' REAL, ',
               header_row[11], ' TEXT, ',
               header_row[12], ' TEXT, ',
               header_row[13], ' TEXT, ',
               header_row[14], ' TEXT, ',
               header_row[15], ' TEXT, ',
               header_row[16], ' TEXT, ',
               header_row[17], ' TEXT, ',
               header_row[18], ' TEXT, ',
               header_row[19], ' TEXT)']

    # Create the table
    print('Create AYASDI table (drop if exists)...')
    sqlite_db.create_table('AYASDI', ''.join(command))
    # Insert all data from the CSV file to the SQLite database
    print('Import CSV to SQLite...')
    sqlite_db.insert_csv('AYASDI', 'ayasdi_assignment.csv')
    print('DONE')

if __name__ == '__main__':
    main()

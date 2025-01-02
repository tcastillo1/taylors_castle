def create_biometric_table():
    return '''
    CREATE TABLE IF NOT EXISTS biometrics (
        id INTEGER PRIMARY KEY,
        user TEXT,
        date DATE NOT NULL,
        weight INTEGER,
        calories INTEGER,
        protein INTEGER,
        fat INTEGER,
        carbohydrates INTEGER,
        sugar INTEGER
    );
    '''

def select_data():
    return 'SELECT * FROM biometrics WHERE user = ?;'

def insert_data():
    return '''
        INSERT INTO biometrics (id, user, date, weight, calories, protein, fat, carbohydrates, sugar) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''

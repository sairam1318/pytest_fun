import sqlite3
import pytest

@pytest.fixture
def db():
    conn = sqlite3.connect("metadata.db")
    conn.execute('''CREATE TABLE TEST(
        username varchar(255) primary key,
        password vachar(255))       
        ''')
    return conn

def test_insert(db):
    db.execute('INSERT INTO TEST values("sairam", "sairam123")')
    
    users = db.execute("Select * from TEST")
    assert list(users) == [('sairam', 'sairam123')]

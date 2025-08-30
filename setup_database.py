import sqlite3
import os

def setup_database():
    # Create database directory if it doesn't exist
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
    
    # Connect to SQLite database (will create if it doesn't exist)
    db_path = os.path.join(data_dir, 'cv_shuffler.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS job_categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keywords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        keyword TEXT NOT NULL UNIQUE,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES job_categories (id)
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keyword_sets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE,
        description TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keyword_set_mappings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        set_id INTEGER,
        keyword_id INTEGER,
        weight INTEGER DEFAULT 1,
        FOREIGN KEY (set_id) REFERENCES keyword_sets (id),
        FOREIGN KEY (keyword_id) REFERENCES keywords (id)
    )
    ''')
    
    # Insert default job categories
    categories = [
        ('Technology & IT', 'Software development, IT infrastructure, cybersecurity'),
        ('Marketing & Sales', 'Digital marketing, sales, advertising, SEO'),
        ('Content Creation', 'Writing, editing, content strategy, blogging'),
        ('Design & Creative', 'Graphic design, UX/UI, multimedia'),
        ('Business & Management', 'Project management, operations, administration'),
        ('Healthcare', 'Medical professions, nursing, healthcare administration'),
        ('Education', 'Teaching, academic research, educational administration'),
        ('Engineering', 'Civil, mechanical, electrical, chemical engineering'),
        ('Finance', 'Accounting, banking, financial analysis'),
        ('Hospitality', 'Hotel management, culinary arts, tourism'),
        ('Legal', 'Law, paralegal, compliance'),
        ('Science & Research', 'Scientific research, laboratory work, R&D'),
        ('Skilled Trades', 'Construction, manufacturing, technical trades'),
        ('Human Resources', 'Recruitment, talent management, HR operations')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO job_categories (name, description) VALUES (?, ?)', categories)
    
    # Insert sample keywords (just a small sample - you'll add more)
    keywords = [
        # Technology & IT
        ('Python', 1), ('JavaScript', 1), ('SQL', 1), ('Cloud Computing', 1), ('Cybersecurity', 1),
        ('DevOps', 1), ('Machine Learning', 1), ('API Development', 1), ('Docker', 1), ('Kubernetes', 1),
        
        # Marketing & Sales
        ('SEO', 2), ('SEM', 2), ('Google Analytics', 2), ('Social Media Marketing', 2), ('Content Marketing', 2),
        ('Email Marketing', 2), ('CRM', 2), ('Sales Funnel', 2), ('Market Research', 2), ('Brand Management', 2),
        
        # Content Creation
        ('Content Strategy', 3), ('Copywriting', 3), ('Blogging', 3), ('Technical Writing', 3), ('Editing', 3),
        ('Proofreading', 3), ('Content Management', 3), ('WordPress', 3), ('Ghostwriting', 3), ('Storytelling', 3),
        
        # Add more keywords for other categories as needed
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO keywords (keyword, category_id) VALUES (?, ?)', keywords)
    
    # Create some sample keyword sets
    keyword_sets = [
        ('SEO Content Writer', 'Keywords for SEO content writer positions'),
        ('Software Developer', 'Keywords for software developer positions'),
        ('Digital Marketer', 'Keywords for digital marketing roles')
    ]
    
    cursor.executemany('INSERT OR IGNORE INTO keyword_sets (name, description) VALUES (?, ?)', keyword_sets)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    print("Database setup completed successfully!")

if __name__ == '__main__':
    setup_database()
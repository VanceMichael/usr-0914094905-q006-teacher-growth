import os, sqlite3
from flask import Flask, jsonify
app=Flask(__name__)
def init_db():
 p=os.environ.get('DATABASE_PATH','teacher.db'); db=sqlite3.connect(p); db.executescript(open('migrations/001_init.sql',encoding='utf8').read()); db.close()
@app.get('/health')
def health(): return jsonify(status='ok')
if __name__=='__main__': init_db(); app.run(host='0.0.0.0',port=int(os.environ.get('PORT','8080')))

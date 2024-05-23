from dataclasses import dataclass
import psycopg2

try:
    conn = psycopg2.connect(
        database="Trabalho",
        user="postgres",
        password="123",
        host="localhost",
        port="5432"
    )

    cur = conn.cursor()

except (Exception, psycopg2.Error) as erro:
    print("Erro ao conectar ao PostgreSQL", erro)


#@dataclass

#class Aluno():
#   ID : int
#    Nome : str
#
#class Professor():
#    ID : int
#    Nome : str
#    Materia : str

def AdicionarAluno(ID, Nome):
    try:
        cur.execute("INSERT INTO \"Alunos\"(\"ID\", \"Nome\") VALUES (%s, %s)", (ID, Nome))
        conn.commit()
    except psycopg2.Error as e:
        print(e)

def RemoverAluno(ID):
    cur.execute(f"DELETE FROM \"Alunos\" WHERE \"ID\" = {ID}")
    conn.commit()
    #isso aqui nao vai pro produto final se nao vai da so problema, so pra teste

def EditarAluno(ID, NomeNovo):
    try:
        cur.execute("UPDATE \"Alunos\" SET \"Nome\" = %s WHERE \"ID\" = %s", (NomeNovo, ID))
        conn.commit()
    except psycopg2.Error as e:
        print(e)

def AdiconarProfessor(ID, Nome, Materia):
    try:
        cur.execute("INSERT INTO \"Professores\"(\"ID\", \"Nome\", \"Materia\") VALUES (%s, %s, %s)", (ID, Nome, Materia))
        #nometabela = "sala" + str(ID)
        #cur.execute(f"CREATE TABLE {nometabela} ( \"IDPROFESSOR\" SERIAL PRIMARY KEY, \"Materia\" VARCHAR(100),\"Horario\" INT, \"Alunos\" VARCHAR)")
        #query = "INSERT INTO %s(\"IDPROFESSOR\") VALUES (%%s)" % nometabela
        #cur.execute(query, (ID,))
    except psycopg2.Error as e:
        print(e)

    conn.commit()

def CriarSala(IDProfessor, Horario):
    try:
        cur.execute(f"SELECT \"Materia\" FROM \"Professores\" WHERE \"ID\" = {IDProfessor}")
        Materia = cur.fetchone()
        cur.execute("INSERT INTO \"Salas\"(\"IDPROFESSOR\", \"Materia\", \"Horario\", \"Alunos\" ) VALUES (%s, %s, %s, %s)", (IDProfessor, Materia, Horario," 0 "))
        conn.commit()
    except psycopg2.Error as e:
        print(e)

def RemoverSala(IDProfessor):
    cur.execute(f"DELETE FROM \"Salas\" WHERE \"IDPROFESSOR\" = {IDProfessor}")
    conn.commit()

def ColocarAluno(IDAluno, IDProfessor):
    if IDAluno == 0 :
        print("Id do aluno não pode ser 0")
        return 0
    cur.execute("UPDATE \"Salas\" SET \"Alunos\" = \"Alunos\" || ' %s ' WHERE \"IDPROFESSOR\" = %s", (IDAluno, IDProfessor))
    #cur.execute("UPDATE \"Salas\" SET \"Alunos\" = \"Alunos\" || '[%s]' WHERE \"IDPROFESSOR\" = %s;", (IDALUNO, IDPROFESSOR))
    #cur.execute("INSERT INTO \"Salas\"(\"Alunos\") VALUES (%s) WHERE \"IDPROFESSOR\" = (%s)", (IDALUNO, IDPROFESSOR))
    conn.commit()

def TirarAluno(IDAluno, IDProfessor):
    if IDAluno == 0 :
        print("Id do aluno não pode ser 0")
        return 0
    cur.execute("UPDATE \"Salas\" SET \"Alunos\" = REPLACE(\"Alunos\", ' %s ', '') WHERE \"IDPROFESSOR\" = %s;", (IDAluno, IDProfessor))
    conn.commit()
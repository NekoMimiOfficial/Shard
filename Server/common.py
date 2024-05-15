import sqlite3
import pickle
import random
from socket import socket

def randomName():
    choices = 'abc123def456XYZ789Q0'
    randomID = ''
    for _ in range(0, 8):
        randomID += choices[random.randint(0, len(choices) - 1)]
    return randomID

class CrystalFracture:
    def __init__(self, id: str, shardCount: int, dust: int, shards: list[bytes]):
        self.id = id
        self.shardCount = shardCount
        self.dust = dust
        self.shards = shards

    def __str__(self):
        return str({'id' : self.id, 'size' : self.shardCount, 'remainder' : self.dust, 'content' : self.shards})

    def __repr__(self):
        return f"<CrystalFracture ID:{self.id}|Shards:{self.shardCount}|Dust:{self.dust}>"

class CrystalLab:
    def __init__(self):
        pass

    def c2s(self, crystal) -> CrystalFracture:
        """Converts raw data (Crystals) to data segments (shards)"""
        """Refer to Section 1.1 (Shard Alignment)"""

        buffer = open(crystal, 'rb')
        data = buffer.read()
        shards = int(len(data)/4096)
        residue = int(len(data) - shards*4096)

        packs: list[bytes] = []

        for step in range(0, shards+1):
            packs.append(data[step:4096])

        fracture = CrystalFracture(randomName(), shards, residue, packs)
        return fracture

class DataBase:
    def __init__(self, location: str):
        self.path = location
        self.db: sqlite3.Connection
        self.head: sqlite3.Cursor

    def connect(self):
        self.db = sqlite3.connect(self.path)
        self.head = self.db.cursor()

    def initializeDB(self):
        self.head.execute("CREATE TABLE IF NOT EXISTS shards (id INTEGER PRIMARY KEY AUTOINCREMENT, shards INTEGER, dust INTEGER, essence BLOB)")
        self.db.commit()

        self.head.execute("CREATE TABLE IF NOT EXISTS lookup (id INTEGER PRIMARY KEY AUTOINCREMENT, link TEXT)")
        self.db.commit()

    def storeShard(self, shard: CrystalFracture):
        id = shard.id
        count = shard.shardCount
        remainder = shard.dust
        data = pickle.dumps(shard.shards)

        self.head.execute("INSERT INTO shards (shards, dust, essence) VALUES (?, ?, ?)", (count, remainder, data))
        self.db.commit()

        self.head.execute(f"INSERT INTO lookup (link) VALUES (\"{id}\")")
        self.db.commit()

    def findID(self, tag: str = "ALL"):
        self.head.execute("SELECT * FROM lookup")
        rows = self.head.fetchall()
        if tag.upper() == "ALL":
            return rows
        for row in rows:
            if row[1] == tag:
                return row[0]
        return None

    def loadID(self, id: int):
        id = int(id)
        if id < 1:
            return None
        self.head.execute("SELECT * FROM shards")
        rows = self.head.fetchall()
        return rows[id-1]

class ErrorEmmiter:
    def version(self, sock: socket):
        packet = b''.join([
            int(1).to_bytes(1),
            int(1).to_bytes(1)
        ])
        pckLen = len(packet)
        payload = b''.join([
            int(70).to_bytes(1),
            int(pckLen).to_bytes(1),
            packet
        ])
        sock.send(payload)

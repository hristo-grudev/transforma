import sqlite3


class TransformaPipeline:
    conn = sqlite3.connect('transforma.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `transforma` (
                                                                                        title varchar(100),
                                                                                        description text,
                                                                                        date varchar(25)                                                                                
                                                                                        )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        date = item['date'][0]

        self.cursor.execute(
            f"""select * from transforma where title = '{title}' and date = '{date}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `transforma`
                                                (`title`, `description`, `date`)
                                                values (?, ?, ?)""", (title, description, date))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

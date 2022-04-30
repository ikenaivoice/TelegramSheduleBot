import psycopg2
import sys
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QTabWidget, QAbstractScrollArea,
                             QVBoxLayout, QHBoxLayout,
                             QTableWidget, QGroupBox,
                         QTableWidgetItem, QPushButton, QMessageBox)

class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.connect_to_db()

        self.setWindowTitle("Shedule")

        self.vbox = QVBoxLayout(self)
        self.tabs = QTabWidget(self)
        self.vbox.addWidget(self.tabs)
        self._create_shedule_tab()
        self._create_teacher_tab()
        self._create_subject_tab()

    def connect_to_db(self):
        self.conn = psycopg2.connect(database="LessonRaspis",
                        user="postgres",
                        password="426572",
                        host="localhost",
                        port="5432")
        self.cursor = self.conn.cursor()

    def _create_shedule_tab(self):
            self.shedule_tab = QWidget()
            self.tabs.addTab(self.shedule_tab, "Расписание")
            self.monday_gbox = QGroupBox("Monday")
            self.tuesday_gbox = QGroupBox("Tuesday")
            self.wednesday_gbox = QGroupBox("Wednesday")
            self.thursday_gbox = QGroupBox("Thursday")
            self.friday_gbox = QGroupBox("Friday")
            self.svbox = QVBoxLayout()
            self.shbox1 = QHBoxLayout()
            self.shbox2 = QHBoxLayout()
            self.svbox.addLayout(self.shbox1)
            self.svbox.addLayout(self.shbox2)
            self.shbox1.addWidget(self.monday_gbox)
            self.shbox1.addWidget(self.tuesday_gbox)
            self.shbox1.addWidget(self.wednesday_gbox)
            self.shbox1.addWidget(self.thursday_gbox)
            self.shbox1.addWidget(self.friday_gbox)
            self._create_monday_table()
            self._create_tuesday_table()
            self._create_wednesday_table()
            self._create_thursday_table()
            self._create_friday_table()
            self.update_shedule_button = QPushButton("Update")
            self.shbox2.addWidget(self.update_shedule_button)
            self.update_shedule_button.clicked.connect(self._update_shedule)
            self.shedule_tab.setLayout(self.svbox)

    def _create_teacher_tab(self):
        self.teacher_tab = QWidget()
        self.tabs.addTab(self.teacher_tab, "Преподаватели")
        self.teacher_gbox = QGroupBox("Teacher")
        self.svboxt = QVBoxLayout()
        self.shboxt1 = QHBoxLayout()
        self.shboxt2 = QHBoxLayout()
        self.svboxt.addLayout(self.shboxt1)
        self.svboxt.addLayout(self.shboxt2)
        self.shboxt1.addWidget(self.teacher_gbox)
        self._create_teacher_table()
        self.update_shedule_buttont = QPushButton("Update")
        self.shboxt2.addWidget(self.update_shedule_buttont)
        self.update_shedule_buttont.clicked.connect(self._update_shedule)
        self.teacher_tab.setLayout(self.svboxt)

    def _create_subject_tab(self):
        self.subject_tab = QWidget()
        self.tabs.addTab(self.subject_tab, "Предмет")
        self.subject_gbox = QGroupBox("Subject")
        self.svboxs = QVBoxLayout()
        self.shboxs1 = QHBoxLayout()
        self.shboxs2 = QHBoxLayout()
        self.svboxs.addLayout(self.shboxs1)
        self.svboxs.addLayout(self.shboxs2)
        self.shboxs1.addWidget(self.subject_gbox)
        self._create_subject_table()
        self.update_shedule_buttons = QPushButton("Update")
        self.shboxs2.addWidget(self.update_shedule_buttons)
        self.update_shedule_buttons.clicked.connect(self._update_shedule)
        self.subject_tab.setLayout(self.svboxs)

    def _create_teacher_table(self):
        self.teacher_table = QTableWidget()
        self.teacher_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.teacher_table.setColumnCount(5)
        self.teacher_table.setHorizontalHeaderLabels(["ID", "Full name", "Subject","",""])

        self._update_teacher_table()

        self.tvbox = QVBoxLayout()
        self.tvbox.addWidget(self.teacher_table)
        self.teacher_gbox.setLayout(self.tvbox)

    def _create_subject_table(self):
        self.subject_table = QTableWidget()
        self.subject_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.subject_table.setColumnCount(4)
        self.subject_table.setHorizontalHeaderLabels(["ID","Subject","",""])

        self._update_subject_table()

        self.svbox = QVBoxLayout()
        self.svbox.addWidget(self.subject_table)
        self.subject_gbox.setLayout(self.svbox)

    def _create_monday_table(self):
        self.monday_table = QTableWidget()
        self.monday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.monday_table.setColumnCount(6)
        self.monday_table.setHorizontalHeaderLabels(["ID", "Subject", "Room", "Time", "", ""])

        self._update_monday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.monday_table)
        self.monday_gbox.setLayout(self.mvbox)

    def _create_tuesday_table(self):
        self.tuesday_table = QTableWidget()
        self.tuesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.tuesday_table.setColumnCount(6)
        self.tuesday_table.setHorizontalHeaderLabels(["ID", "Subject", "Room", "Time", "", ""])

        self._update_tuesday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.tuesday_table)
        self.tuesday_gbox.setLayout(self.mvbox)

    def _create_wednesday_table(self):
            self.wednesday_table = QTableWidget()
            self.wednesday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

            self.wednesday_table.setColumnCount(6)
            self.wednesday_table.setHorizontalHeaderLabels(["ID", "Subject", "Room", "Time", "", ""])

            self._update_wednesday_table()

            self.mvbox = QVBoxLayout()
            self.mvbox.addWidget(self.wednesday_table)
            self.wednesday_gbox.setLayout(self.mvbox)
    def _create_thursday_table(self):
        self.thursday_table = QTableWidget()
        self.thursday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.thursday_table.setColumnCount(6)
        self.thursday_table.setHorizontalHeaderLabels(["ID", "Subject", "Room", "Time", "", ""])

        self._update_thursday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.thursday_table)
        self.thursday_gbox.setLayout(self.mvbox)
    def _create_friday_table(self):
        self.friday_table = QTableWidget()
        self.friday_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

        self.friday_table.setColumnCount(6)
        self.friday_table.setHorizontalHeaderLabels(["ID", "Subject", "Room", "Time", "", ""])

        self._update_friday_table()

        self.mvbox = QVBoxLayout()
        self.mvbox.addWidget(self.friday_table)
        self.friday_gbox.setLayout(self.mvbox)

    def _update_teacher_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM teacher ORDER BY id ASC")
        records = list(self.cursor.fetchall())

        self.teacher_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.teacher_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.teacher_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[1])))
            self.teacher_table.setItem(i, 2,
                                       QTableWidgetItem(str(r[2])))
            self.teacher_table.setCellWidget(i, 3, joinButton)
            self.teacher_table.setCellWidget(i, 4, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_teacher(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_teacher(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_teacher(num))
        self.teacher_table.setCellWidget(len(records), 0, joinButton2)
        self.teacher_table.resizeRowsToContents()

    def _update_subject_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM subject")
        records = list(self.cursor.fetchall())

        self.subject_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.subject_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[1])))
            self.subject_table.setItem(i, 1,
                                       QTableWidgetItem(str(r[0])))
            self.subject_table.setCellWidget(i, 2, joinButton)
            self.subject_table.setCellWidget(i, 3, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_subject(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_subject(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_subject(num))
        self.subject_table.setCellWidget(len(records), 0, joinButton2)
        self.subject_table.resizeRowsToContents()

    def _update_monday_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM timetable WHERE day='Понедельник' ORDER BY id")
        records = list(self.cursor.fetchall())

        self.monday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.monday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.monday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.monday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.monday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[4])))
            self.monday_table.setCellWidget(i, 4, joinButton)
            self.monday_table.setCellWidget(i, 5, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_monday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_monday(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_monday(num))
        self.monday_table.setCellWidget(len(records), 0, joinButton2)
        self.monday_table.resizeRowsToContents()

    def _update_tuesday_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM timetable WHERE day='Вторник' ORDER BY id ASC")
        records = list(self.cursor.fetchall())

        self.tuesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.tuesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.tuesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.tuesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.tuesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[4])))
            self.tuesday_table.setCellWidget(i, 4, joinButton)
            self.tuesday_table.setCellWidget(i, 5, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_tuesday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_tuesday(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_tuesday(num))
        self.tuesday_table.setCellWidget(len(records), 0, joinButton2)
        self.tuesday_table.resizeRowsToContents()
    def _update_wednesday_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM timetable WHERE day='Среда' ORDER BY id ASC")
        records = list(self.cursor.fetchall())

        self.wednesday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.wednesday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.wednesday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.wednesday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.wednesday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[4])))
            self.wednesday_table.setCellWidget(i, 4, joinButton)
            self.wednesday_table.setCellWidget(i, 5, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_wednesday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_wednesday(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_wednesday(num))
        self.wednesday_table.setCellWidget(len(records), 0, joinButton2)
        self.wednesday_table.resizeRowsToContents()

    def _update_thursday_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM timetable WHERE day='Четверг' ORDER BY id ASC")
        records = list(self.cursor.fetchall())

        self.thursday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.thursday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.thursday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.thursday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.thursday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[4])))
            self.thursday_table.setCellWidget(i, 4, joinButton)
            self.thursday_table.setCellWidget(i, 5, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_thursday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_thursday(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_thursday(num))
        self.thursday_table.setCellWidget(len(records), 0, joinButton2)
        self.thursday_table.resizeRowsToContents()
    def _update_friday_table(self):
        self.conn.rollback()
        self.cursor.execute("SELECT * FROM timetable WHERE day='Пятница' ORDER BY id ASC")
        records = list(self.cursor.fetchall())

        self.friday_table.setRowCount(len(records) + 1)

        for i, r in enumerate(records):
            r = list(r)
            joinButton = QPushButton("Изменить")
            joinButton1 = QPushButton("Удалить")
            self.friday_table.setItem(i, 0,
                                      QTableWidgetItem(str(r[0])))
            self.friday_table.setItem(i, 1,
                                      QTableWidgetItem(str(r[2])))
            self.friday_table.setItem(i, 2,
                                      QTableWidgetItem(str(r[3])))
            self.friday_table.setItem(i, 3,
                                      QTableWidgetItem(str(r[4])))
            self.friday_table.setCellWidget(i, 4, joinButton)
            self.friday_table.setCellWidget(i, 5, joinButton1)

            joinButton.clicked.connect(lambda ch, num=i: self._change_day_from_friday(num))
            joinButton1.clicked.connect(lambda ch, num=i: self._del_day_from_friday(num))
        joinButton2 = QPushButton("Добавить")
        joinButton2.clicked.connect(lambda ch, num=i: self._add_day_from_friday(num))
        self.friday_table.setCellWidget(len(records), 0, joinButton2)
        self.friday_table.resizeRowsToContents()

    def _add_day_from_teacher(self, rowNum):
        self.cursor.execute("insert into teacher (full_name) VALUES ('None')")
        self.conn.commit()

    def _del_day_from_teacher(self, rowNum):
        row = list()
        for column in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM teacher WHERE id = %s", (row[0],))
        self.conn.commit()

    def _add_day_from_subject(self, rowNum):
        self.cursor.execute("insert into subject (name) VALUES ('None')")
        self.conn.commit()

    def _del_day_from_subject(self, rowNum):
        row = list()
        for column in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM subject WHERE id = %s", (row[0],))
        self.conn.commit()

    def _add_day_from_monday(self, rowNum):
        self.cursor.execute("insert into timetable (day) VALUES ('Понедельник')")
        self.conn.commit()

    def _del_day_from_monday(self, rowNum):
        row = list()
        for column in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s", (row[0],))
        self.conn.commit()
    def _add_day_from_tuesday(self, rowNum):
        self.cursor.execute("insert into timetable (day) VALUES ('Вторник')")
        self.conn.commit()

    def _del_day_from_tuesday(self, rowNum):
        row = list()
        for column in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s", (row[0],))
        self.conn.commit()

    def _add_day_from_wednesday(self, rowNum):
        self.cursor.execute("insert into timetable (day) VALUES ('Среда')")
        self.conn.commit()

    def _del_day_from_wednesday(self, rowNum):
        row = list()
        for column in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s", (row[0],))
        self.conn.commit()

    def _add_day_from_thursday(self, rowNum):
        self.cursor.execute("insert into timetable (day) VALUES ('Четверг')")
        self.conn.commit()

    def _del_day_from_thursday(self, rowNum):
        row = list()
        for column in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s", (row[0],))
        self.conn.commit()

    def _add_day_from_friday(self, rowNum):
        self.cursor.execute("insert into timetable (day) VALUES ('Пятница')")
        self.conn.commit()

    def _del_day_from_friday(self, rowNum):
        row = list()
        for column in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, column).text())
            except:
                row.append(None)
        self.cursor.execute("DELETE FROM timetable WHERE id = %s", (row[0],))
        self.conn.commit()

    def _change_day_from_teacher(self, rowNum):
        row = list()
        for column in range(self.teacher_table.columnCount()):
            try:
                row.append(self.teacher_table.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE teacher SET full_name = %s, subject = %s WHERE id = %s", (row[1], row[2], row[0]))
            self.conn.commit()
        except Exception as e:
            print(e)
            QMessageBox.about(self, "Error", "Fill all")

    def _change_day_from_subject(self, rowNum):
        row = list()
        for column in range(self.subject_table.columnCount()):
            try:
                row.append(self.subject_table.item(rowNum, column).text())
            except:
                row.append(None)
        print(row)
        try:
            self.cursor.execute("UPDATE subject SET name = %s WHERE id = %s", (row[1], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Fill all")

    def _change_day_from_monday(self, rowNum):
        row = list()
        for column in range(self.monday_table.columnCount()):
            try:
                row.append(self.monday_table.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET subject = %s, room = %s, start = %s WHERE id = %s", (row[1], row[2], row[3], row[0]))
            self.conn.commit()
        except Exception as e:
            print(e)
            QMessageBox.about(self, "Error", "Fill all")

    def _change_day_from_tuesday(self, rowNum):
        row = list()
        for column in range(self.tuesday_table.columnCount()):
            try:
                row.append(self.tuesday_table.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET subject = %s, room = %s, start = %s WHERE id = %s",
                                (row[1], row[2], row[3], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Fill all")

    def _change_day_from_wednesday(self, rowNum):
        row = list()
        for column in range(self.wednesday_table.columnCount()):
            try:
                row.append(self.wednesday_table.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET subject = %s, room = %s, start = %s WHERE id = %s",
                                (row[1], row[2], row[3], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Fill all")

    def _change_day_from_thursday(self, rowNum):
        row = list()
        for column in range(self.thursday_table.columnCount()):
            try:
                row.append(self.thursday_table.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET subject = %s, room = %s, start = %s WHERE id = %s",
                                (row[1], row[2], row[3], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Fill all")
    def _change_day_from_friday(self, rowNum):
        row = list()
        for column in range(self.friday_table.columnCount()):
            try:
                row.append(self.friday_table.item(rowNum, column).text())
            except:
                row.append(None)
        try:
            self.cursor.execute("UPDATE timetable SET subject = %s, room = %s, start = %s WHERE id = %s",
                                (row[1], row[2], row[3], row[0]))
            self.conn.commit()
        except:
            QMessageBox.about(self, "Error", "Fill all ")


    def _update_shedule(self):
        self.monday_table.setRowCount(0)
        self._update_monday_table()
        self.tuesday_table.setRowCount(0)
        self._update_tuesday_table()
        self.wednesday_table.setRowCount(0)
        self._update_wednesday_table()
        self.thursday_table.setRowCount(0)
        self._update_thursday_table()
        self.friday_table.setRowCount(0)
        self._update_friday_table()
        self.teacher_table.setRowCount(0)
        self._update_teacher_table()
        self.subject_table.setRowCount(0)
        self._update_subject_table()

app = QApplication(sys.argv)
win = MainWindow()
win.show()
sys.exit(app.exec_())
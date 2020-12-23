'''
Created on Dec 9, 2020

@author: Yashas
'''
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from imutils.video import VideoStream
import MySQLdb as sql, pyzbar
from pyzbar import pyzbar
import sys, pyqrcode, time, cv2, imutils, os, datetime, webbrowser
from xlsxwriter.workbook import Workbook
from BillUi import Ui_MainWindow

class BillApp(QMainWindow, Ui_MainWindow):
    
    ##### Initialise #####
    
    def __init__(self):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.startUI()
        self.startButton()
        self.setTheme()
        self.clearBill()
        self.showItem()
        self.showBill()
        self.categoryCombobox()
        self.showCategory()
        
    ##### Handle UI #####
        
    def startUI(self):
        
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget_2.tabBar().setVisible(False)
        
    ##### Handle buttons #####
        
    def startButton(self):
        
        #LoginPage
        self.pushButton_12.clicked.connect(self.startUser)
        self.pushButton_48.clicked.connect(self.openSQLConfig)
        self.pushButton_49.clicked.connect(self.home)
        self.pushButton_47.clicked.connect(self.savePassword)
        self.pushButton_14.clicked.connect(self.closeApp)
        self.pushButton_6.clicked.connect(self.RaghavInsta)
        self.pushButton_8.clicked.connect(self.YashasInsta)
        self.pushButton_13.clicked.connect(self.RaghavLinkedIn)
        self.pushButton_16.clicked.connect(self.YashasLinkedIn)
        
        #ViewItems
        self.pushButton_43.clicked.connect(self.deleteBill)
        self.pushButton_44.clicked.connect(self.deleteItem)
        self.pushButton_17.clicked.connect(self.scanCode)
        self.pushButton_45.clicked.connect(self.createBill)
        self.pushButton_46.clicked.connect(self.clearBillArea)
        self.pushButton_22.clicked.connect(self.backUser)
        self.pushButton_24.clicked.connect(self.closeApp)
        self.pushButton_26.clicked.connect(self.viewItems)
        self.pushButton_25.clicked.connect(self.addItems)
        self.pushButton_23.clicked.connect(self.openSettings)
        
        #AddItemPage
        self.pushButton.clicked.connect(self.addItem)
        self.pushButton_28.clicked.connect(self.backUser)
        self.pushButton_29.clicked.connect(self.closeApp)
        self.pushButton_31.clicked.connect(self.viewItems)
        self.pushButton_30.clicked.connect(self.addItems)
        self.pushButton_27.clicked.connect(self.openSettings)
        
        #SettingPage
        self.pushButton_33.clicked.connect(self.backUser)
        self.pushButton_34.clicked.connect(self.closeApp)
        self.pushButton_36.clicked.connect(self.viewItems)
        self.pushButton_35.clicked.connect(self.addItems)
        self.pushButton_32.clicked.connect(self.openSettings)
        self.pushButton_2.clicked.connect(self.settingUser)
        self.pushButton_3.clicked.connect(self.settingCategory)
        self.pushButton_4.clicked.connect(self.settingTheme)
        self.pushButton_38.clicked.connect(self.settingUser)
        self.pushButton_37.clicked.connect(self.settingCategory)
        self.pushButton_39.clicked.connect(self.settingTheme)
        self.pushButton_40.clicked.connect(self.settingUser)
        self.pushButton_42.clicked.connect(self.settingCategory)
        self.pushButton_41.clicked.connect(self.settingTheme)
        self.pushButton_15.clicked.connect(self.addUser)
        self.pushButton_7.clicked.connect(self.editUser)
        self.pushButton_5.clicked.connect(self.loginUser)
        self.pushButton_10.clicked.connect(self.addCategory)
        self.pushButton_11.clicked.connect(self.deleteCategory)
        self.pushButton_9.clicked.connect(self.deleteUser)
        self.pushButton_21.clicked.connect(self.setDarkBlue)
        self.pushButton_19.clicked.connect(self.setDarkGray)
        self.pushButton_18.clicked.connect(self.setDarkOrange)
        self.pushButton_20.clicked.connect(self.setLight)
        
    ##### Handle Pages #####
        
    def settingUser(self):
        
        self.statusBar().showMessage('')
        self.tabWidget_2.setCurrentIndex(0)
    
    def settingCategory(self):
        
        self.statusBar().showMessage('')
        self.tabWidget_2.setCurrentIndex(1)
    
    def settingTheme(self):
        
        self.statusBar().showMessage('')
        self.tabWidget_2.setCurrentIndex(2)
        
    def viewItems(self):
        
        self.statusBar().showMessage('')
        self.tabWidget.setCurrentIndex(1)
    
    def addItems(self):
        
        self.statusBar().showMessage('')
        self.tabWidget.setCurrentIndex(2)
    
    def openSettings(self):
        
        self.statusBar().showMessage('')
        self.tabWidget.setCurrentIndex(3)
        
    def openSQLConfig(self):
        
        self.statusBar().showMessage('')
        self.tabWidget.setCurrentIndex(4)
        
    def home(self):
        
        self.tabWidget.setCurrentIndex(0)
        pass
        
    ##### Login Page #####
            
    def backUser(self):
        
        warn = QMessageBox.warning(self, 'Sure to log out?', 'Are you sure you want to log out?', QMessageBox.Yes|QMessageBox.No)
        if warn == QMessageBox.Yes:
            self.home()
            
    def closeApp(self):
        
        warn = QMessageBox.warning(self, 'Sure to quit?', "Are you sure you want to quit?", QMessageBox.Yes|QMessageBox.No)
        
        if warn == QMessageBox.Yes:
            
            sys.exit()
            
    def savePassword(self):
        
        f = open('SQL Dump/db.txt','w')
        password = self.lineEdit.text()
        f.write(password)
        f.close()   
    
    def returnPassword(self):
        
        f = open('SQL Dump/db.txt','r')
        x = f.read()
        return x
    
    def startUser(self):
        
        uName = self.lineEdit_11.text()
        uPass = self.lineEdit_10.text()
        pwd = self.returnPassword()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''select uName, uPass, uMail from users''')
            uData = self.cur.fetchall()
            
            for i in uData:
                
                if uName == i[0] and uPass == i[1]:
                    
                    self.label_17.setText('')
                    
                    self.lineEdit_10.setText('')
                    self.lineEdit_11.setText('')
                    
                    self.tabWidget.setCurrentIndex(1)
                    self.label_18.setText(uName)
                    
                    break
                
                else:
                
                    self.label_17.setText('Incorrect credentials')
                     
        except:
            self.statusBar().showMessage('Unable to fetch user data')
            
    ##### View Items #####
    
    def clearBillArea(self):
        
        self.clearBill()
        self.tableWidget_3.clear()
        self.label_21.setText('')
    
    def deleteBill(self):
        
        iName = self.lineEdit_15.text()
        pwd = self.returnPassword()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        self.cur1 = self.con.cursor()
        
        try:
            self.cur.execute('''delete from purchase where pName=%s''',[iName])
            self.con.commit()
            self.cur1.execute('''select sum(pPrice) from purchase''')
            total = self.cur1.fetchone()
            self.label_21.setText('Total amount: ' + str(total[0]))
            self.showBill()
            self.statusBar().showMessage('Item discarded')
        except:
            self.statusBar().showMessage('Unable to delete item from bill')
    
    def deleteItem(self):
        
        iName = self.lineEdit_16.text()
        pwd = self.returnPassword()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''delete from items where iName=%s''',[iName])
            self.con.commit()
            self.showItem()
            self.statusBar().showMessage('Item deleted')
        except:
            self.statusBar().showMessage('Unable to delete item')
    
    def showBill(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''select pName, pPrice from purchase''')
            pData = self.cur.fetchall()
            
            if pData:
                self.tableWidget_3.setRowCount(0)
                self.tableWidget_3.insertRow(0)
                for row, form in enumerate(pData):
                    for col, item in enumerate(form):
                        self.tableWidget_3.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    rowPos = self.tableWidget_3.rowCount()
                    self.tableWidget_3.insertRow(rowPos)
                    
            
        except:
            self.statusBar().showMessage('Error loading bill table')
        
    def scanCode(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        self.cur1 = self.con.cursor()
        
        vs = VideoStream(src=0).start()
        time.sleep(2.0)
        
        while True:
            
            frame = vs.read()
            frame = imutils.resize(frame, width=400)
            QRcodes = pyzbar.decode(frame)
            
            for QRcode in QRcodes:
                
                    (x, y, w, h) = QRcode.rect
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    QRcodeData = QRcode.data.decode("utf-8")
                    
                    text = "{}".format(QRcodeData)
                    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 200), 2)
                    
                    text = text.split(',')
                    pName =  text[0]
                    pPrice = text[1]

            cv2.imshow("Press 'Q' to exit", frame)
            key = cv2.waitKey(1) & 0xFF
            
            if key == ord("q"):
                break
            
        cv2.destroyAllWindows()
        vs.stop()
        
        try:
            self.cur.execute('''insert into purchase (pName, pPrice) values (%s,%s)''',(pName, pPrice))
            self.con.commit()
            self.cur1.execute('''select sum(pPrice) from purchase''')
            total = self.cur1.fetchone()
            self.label_21.setText('Total amount: ' + str(total[0]))
            self.statusBar().showMessage('Item added to cart')
            self.showBill()
        except:
            self.statusBar().showMessage('Unable to add item to bill')
            
    def createBill(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''select pName, pPrice from purchase''')
            bill = self.cur.fetchall()
            x = datetime.datetime.now()
            xlName = 'Bill-' + str(x.day) + '-' + str(x.month) + '-' + str(x.year) + '-' + str(x.hour) + '-' + str(x.minute) + '-' + str(x.second) + '-' + self.label_18.text()
            xlDate = str(x.day) + '-' + str(x.month) + '-' + str(x.year)
            XL = Workbook('Bills/' + xlName + '.xlsx')
            S1 = XL.add_worksheet()
            
            S1.write(1,0,'INVOICE' + xlDate)
            S1.write(3,0,'Item Name')
            S1.write(3,1,'Item Price')

            rowPos = 5
            for row in bill:
                colPos = 0
                for i in row:
                    S1.write(rowPos,colPos,str(i))
                    colPos += 1
                rowPos += 1
                
            total = self.label_21.text()
            total = total.split(' ')
            S1.write(rowPos+2,0,'Total: ')
            S1.write(rowPos+2,1,str(total[2]))
            S1.write(rowPos+4,0,'User: ' + self.label_18.text())
            S1.write(rowPos+6,0,'BillGen')
            S1.write(rowPos+6,1,'V1.0')
                
            self.statusBar().showMessage('Bill exported')
            XL.close()
            
        except:
            self.statusBar().showMessage('Unable to export to excel')
            
    ##### Add Items #####
    
    def clearBill(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''delete from purchase''')
            self.con.commit()
            self.showBill()
        except:
            self.statusBar().showMessage('Unable to clear bill')
            
    def addItem(self):
        
        pwd = self.returnPassword()
        iName = self.lineEdit_2.text()
        iPrice = self.lineEdit_3.text()
        iCategory = self.comboBox.currentText()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''insert into items (iName, iPrice, iCategory) values (%s,%s,%s)''',(iName, iPrice, iCategory))
            self.lineEdit_2.setText('')
            self.lineEdit_3.setText('')
            self.comboBox.setCurrentIndex(0)
            self.con.commit()
            
            x = [iName, iPrice, iCategory]
            newQr = pyqrcode.create(f'{x[0]}, {x[1]}, {x[2]}')
            newQr.png(f'QRCodes/{iName}.png', 10)
            self.label_19.setStyleSheet(f"background-image: url(QRCodes/{iName}.png);")
            
            self.statusBar().showMessage('Item added successfully')
            self.showItem()
        except:
            self.statusBar().showMessage('Unable to add item')
            
    def showItem(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        self.cur1 = self.con.cursor()
        
        try:
            self.cur.execute('''select iName, iPrice, iCategory from items''')
            iData = self.cur.fetchall()
            
            if iData:
                self.tableWidget.setRowCount(0)
                self.tableWidget.insertRow(0)
                for row, form in enumerate(iData):
                    for col, item in enumerate(form):
                        self.tableWidget.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    rowPos = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPos)
                    
            self.cur1.execute('''select count(id) from items''')
            count = self.cur1.fetchone()
            self.label_23.setText('Total items: ' + str(count[0]))
        except:
            self.statusBar().showMessage('Error loading item table')
    
    ##### Users #####
            
    def loginUser(self):
        
        pwd = self.returnPassword()
        uName = self.label_18.text()
        uPass = self.lineEdit_5.text()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''select uName, uPass, uMail from users''')
            uData = self.cur.fetchall()
            
            for i in uData:
                
                if uName == i[0] and uPass == i[1]:
                    
                    self.label_16.setText('')
                    
                    self.lineEdit_7.setText(self.label_18.text())
                    self.lineEdit_6.setText(self.lineEdit_5.text())
                    self.lineEdit_8.setText(i[2])
                    
                    self.lineEdit_5.setText('')
                    
                    break
                
                else:
                
                    self.label_16.setText('Incorrect credentials')
                     
        except:
            self.statusBar().showMessage('Unable to fetch user data')
        
    def addUser(self):
        
        pwd = self.returnPassword()
        uName = self.lineEdit_12.text()
        uPass = self.lineEdit_13.text()
        uMail = self.lineEdit_14.text()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''insert into users (uName, uPass, uMail) values (%s,%s,%s)''',(uName, uPass, uMail))
            self.con.commit()
            self.statusBar().showMessage('User added successfully')
            self.lineEdit_12.setText('')
            self.lineEdit_13.setText('')
            self.lineEdit_14.setText('')
        except:
            self.statusBar().showMessage('Failed to add user')
    
    def editUser(self):
        
        pwd = self.returnPassword()
        OriginaluName = self.label_18.text()
        uName = self.lineEdit_7.text()
        uPass = self.lineEdit_6.text()
        uMail = self.lineEdit_8.text()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''update users set uName=%s, uPass=%s, uMail=%s where uName=%s''',(uName,uPass,uMail,OriginaluName))
            self.con.commit()
            self.label_18.setText(uName)
            self.lineEdit_7.setText('')
            self.lineEdit_6.setText('')
            self.lineEdit_8.setText('')
            self.statusBar().showMessage('User details updated')
        except:
            self.statusBar().showMessage('Unable to update user details')
    
    def deleteUser(self):
        
        pwd = self.returnPassword()
        uName = self.label_18.text()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            warn = QMessageBox.warning(self, 'Sure to delete user?', 'Are you sure you want to delete this user?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                self.cur.execute('''delete from users where uName = %s''',[uName])
                self.con.commit()
                self.statusBar().showMessage('User deleted successfully')
                self.lineEdit_6.setText('')
                self.lineEdit_7.setText('')
                self.lineEdit_8.setText('')
                self.tabWidget.setCurrentIndex(0)
        except:
            self.statusBar().showMessage('Unable to delete user')
            
    ##### Categories #####
    
    def addCategory(self):
        
        pwd = self.returnPassword()
        cName = self.lineEdit_9.text()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''insert into categories (cName) values (%s)''',[cName])
            self.con.commit()
            self.statusBar().showMessage('Category added successfully')
            self.lineEdit_9.setText('')
            self.categoryCombobox()
            self.showCategory()
        except:
            self.statusBar().showMessage('Unable to add category')
            
    def deleteCategory(self):
        
        pwd = self.returnPassword()
        cName = self.lineEdit_9.text()
        
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            warn = QMessageBox.warning(self, 'Sure to delete category?', 'Are you sure you want to delete this category?', QMessageBox.Yes|QMessageBox.No)
            
            if warn == QMessageBox.Yes:
                self.cur.execute('''delete from categories where cName = %s''',[cName])
                self.con.commit()
                self.statusBar().showMessage('Category deleted successfully')
                self.lineEdit_9.setText('')
                self.categoryCombobox()
                self.showCategory()
        except:
            self.statusBar().showMessage('Unable to delete category')
    
    def categoryCombobox(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''select cName from categories''')
            cData = self.cur.fetchall()
            
            self.comboBox.clear()
            self.comboBox.addItem('---Select category---')
            
            for i in cData:
                self.comboBox.addItem(i[0])
                
        except:
            self.statusBar().showMessage('Error loading category combobox')
                
    def showCategory(self):
        
        pwd = self.returnPassword()
        self.con = sql.connect('localhost', 'root', pwd, 'bill')
        self.cur = self.con.cursor()
        
        try:
            self.cur.execute('''select cName from categories''')
            cData = self.cur.fetchall()
            
            if cData:
                self.tableWidget_2.setRowCount(0)
                self.tableWidget_2.insertRow(0)
                for row, form in enumerate(cData):
                    for col, item in enumerate(form):
                        self.tableWidget_2.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1
                    rowPos = self.tableWidget_2.rowCount()
                    self.tableWidget_2.insertRow(rowPos)
        except:
            self.statusBar().showMessage('Error loading category table')
            
    ##### Themes #####
    
    def setTheme(self):

        file = open('Themes/ThemeConfig.txt','r')
        x = file.read()
        x = x.split(' ')
        ThemeVariable = 'Themes/' + x[-1]
              
        style = open(ThemeVariable)
        style = style.read()
        self.setStyleSheet(style)
            
    def setDarkBlue(self):
        
        file = open('Themes/ThemeConfig.txt','w')
        file.write('Default theme: darkstyle.css')
        file.close()
        self.setTheme()
        
    def setDarkOrange(self):
        
        file = open('Themes/ThemeConfig.txt','w')
        file.write('Default theme: darkorange.css')
        file.close()
        self.setTheme()
        
    def setDarkGray(self):
        
        file = open('Themes/ThemeConfig.txt','w')
        file.write('Default theme: darkgray.css')
        file.close()
        self.setTheme()
        
    def setLight(self):
        
        file = open('Themes/ThemeConfig.txt','w')
        file.write('Default theme: light.css')
        file.close()
        self.setTheme()
        
    ##### Web operations
    
    def YashasInsta(self):
        
        webbrowser.open('https://www.instagram.com/yashas1145/')
    
    def RaghavInsta(self):
        
        webbrowser.open('https://www.instagram.com/raghav_vasishta/')
    
    def YashasLinkedIn(self):
        
        webbrowser.open('https://www.linkedin.com/in/yashas-bn-485b6816b/')
    
    def RaghavLinkedIn(self):
        
        webbrowser.open('https://www.linkedin.com/in/raghavendra-vasista-l-a6384b27')
                
def main():
    
    Final = QApplication(sys.argv)
    NewApp = BillApp()
    NewApp.show()
    Final.exec_()
    
if __name__ == '__main__':
    
    main()

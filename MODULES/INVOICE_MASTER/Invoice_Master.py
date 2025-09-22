from PyQt5.QtCore import QDate

from Env import *

@Exception_Handle
def Invoice_Master_FN(ui):
    print("------------Invoice Master Started-------------")
    PrdTbl = ui.IQTB_ProductList
    BilTbl = ui.IQTB_BillList

    @Exception_Handle
    def BilTblFilter(row, column, text):
        if column == 0:
            Product_Push(text)
            row, col = 0, 0
            index = models['Product_Model'].index(row, col)

    @Exception_Handle
    def setup_table_with_text_changes(table):
        class LetterEditDelegate(QStyledItemDelegate):
            textChanged = pyqtSignal(int, int, str)  # row, column, text

            def createEditor(self, parent, option, index):
                editor = super().createEditor(parent, option, index)
                if editor:  # Typically a QLineEdit
                    editor.textChanged.connect(
                        lambda text: self.textChanged.emit(
                            index.row(),
                            index.column(),
                            text
                        )
                    )
                return editor

        delegate = LetterEditDelegate(table)
        table.setItemDelegate(delegate)
        return delegate
    delegate = setup_table_with_text_changes(BilTbl)
    delegate.textChanged.connect(BilTblFilter)

    @Exception_Handle
    def Prd_Bil_Add(index):
        data = get_row_values(PrdTbl, index.row())
        BilTbl.setItem(BilTbl.rowCount() - 1, 0, QTableWidgetItem(str(data[2])))
        BilTbl.setItem(BilTbl.rowCount() - 1, 2, QTableWidgetItem(str(data[6])))
        BilTbl.setFocus(True)
        BilTbl.setCurrentCell(BilTbl.rowCount() - 1, 1)

    @Exception_Handle
    def Product_Push(filter):
        SQL_Product = fr'SELECT EPN, IPN, Product_Name, HSN, GST_Slab, UOM, Price, Misc FROM product_info '\
                        fr'WHERE Active = "Y" and Product_name like "{filter}%" order by Product_Name'
        # print(SQL_Product)
        Push_TableView_SqlData('Product_Model', PrdTbl, SQL_Product)
        for col in [0]+list(range(3, 6))+[7]:
            ui.IQTB_ProductList.hideColumn(col)

    @Exception_Handle
    def Calc_Amount(row,col):
        if col == 1:
            try:
                BilTbl.setItem(row,3,QTableWidgetItem(str( round(float(BilTbl.item(row,1).text()) * float(BilTbl.item(row,2).text()),2))))
            except:
                pass

        try:
            temp = Fetch_Table_Values(BilTbl)
            ui.IQTE_NetQuantity.setText(str(sum(float(x[1]) for x in temp)))
            ui.IQTE_UniqueQuantity.setText(str(len(temp)))
            ui.IQLE_SubTotal.setText(str(sum(float(x[3]) for x in temp)))


        except Exception as e:
            print(e)
            pass

    @Exception_Handle
    def Bil_Tbl_Add():
        if None not in get_row_values(BilTbl,BilTbl.rowCount()-1):
            BilTbl.setRowCount(BilTbl.rowCount() + 1)
            BilTbl.setFocus(True)
            BilTbl.setCurrentCell(BilTbl.rowCount()-1, 0)
            Product_Push("")

    @Exception_Handle
    def Update_customerDetails():
        try:
            temp = DB_Fetch(fr'''select customer_name, concat(Address," ",District) from customer_info 
            where Mobile ='{ui.IQCB_PhoneNumber.currentText()}' ''',True,"LOE")
            ui.IQLE_CustomerName.setReadOnly(True)
            ui.IQLE_Address.setReadOnly(True)
            ui.IQLE_CustomerName.setText(temp[0])
            ui.IQLE_Address.setText(temp[1])
            ui.IQCB_PhoneNumber.setStyleSheet("QComboBox { background-color: lightgreen; }")
            ui.IQPB_LoadCustomer.setEnabled(False)

        except Exception as e:
            ui.IQLE_CustomerName.setReadOnly(False)
            ui.IQLE_Address.setReadOnly(False)
            ui.IQLE_CustomerName.setText("")
            ui.IQLE_Address.setText("")
            ui.IQCB_PhoneNumber.setStyleSheet("QComboBox { background-color: white; }")
            ui.IQPB_LoadCustomer.setEnabled(True)
            pass


    Product_Push("")

    PrdTbl.setTabKeyNavigation(False)
    BilTbl.setTabKeyNavigation(False)
    BilTbl.setRowCount(1)
    BilTbl.setFocus(True)
    PrdTbl.activated.connect(Prd_Bil_Add)
    BilTbl.activated.connect(lambda : Bil_Tbl_Add())
    BilTbl.cellChanged.connect(Calc_Amount)

    CustomerMobileFetch = lambda X : DB_Fetch(fr''' select Mobile from customer_info where active = 'Y' and 
                                                        mobile like '{X}%' order by Mobile ''',False,"LOE")
    ui.IQCB_PhoneNumber.addItems(CustomerMobileFetch(""))
    Dynamic_Filter_ComboBox(ui.IQCB_PhoneNumber)
    ui.IQCB_PhoneNumber.currentIndexChanged.connect(lambda : Update_customerDetails())
    ui.IQDE_InvDate.setDate(QDate.currentDate())



if __name__ == "__main__":
    Invoice_Master_FN(Inv_Mtr)
    Inv_Mtr.showMaximized()
    sys.exit(app.exec_())
# ldir = fr"G:\GIt Workspsce\Twink_ERP"
# Itm_Mtr = uic.loadUi(fr'{ldir}\MODULES\ITEM_MASTER\UI-ItemMaster.ui')
from Env import *

@Exception_Handle
def Item_Master_FN(Itm_Mtr):
    Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQLE", True)
    Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQTE", True)

    Units_List = ["Kg", "Nos", "Ton",'Piece','Gram']
    Active_Status = ["Yes","No"]

    Itm_Mtr.IQCB_UOM.addItems(Units_List)

    print("------------Item Master Started-------------")

    @Exception_Handle
    def On_Clicked_Product_TblView():
        print("hello on chick")
        selected_rows = Itm_Mtr.OQTB_Product.selectionModel().selectedRows()
        index = selected_rows[-1]
        Product_IPN = Itm_Mtr.OQTB_Product.model().index(index.row(), 0).data()

        print(Product_IPN)

        Itm_Mtr.IQLE_ProductID.setText(str(Product_IPN))
        Itm_Mtr.IQLE_BarcodeInput.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 1).data()))
        Itm_Mtr.IQLE_ProductName.setText(Itm_Mtr.OQTB_Product.model().index(index.row(), 2).data())
        Itm_Mtr.IQLE_TamilName.setText(Itm_Mtr.OQTB_Product.model().index(index.row(), 3).data())
        Itm_Mtr.IQLE_PurchaseRate.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 4).data()))
        Itm_Mtr.IQLE_MRP.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 5).data()))
        Itm_Mtr.IQLE_SalesPrice_W.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 6).data()))
        Itm_Mtr.IQLE_SalesPrice_R.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 7).data()))
        Itm_Mtr.IQLE_GST.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 8).data()))


        Itm_Mtr.IQCB_UOM.clear()
        Itm_Mtr.IQCB_UOM.addItems(Units_List)
        Itm_Mtr.IQCB_UOM.setCurrentIndex(
            Units_List.index(Itm_Mtr.OQTB_Product.model().index(index.row(), 9).data()))
        Itm_Mtr.IQCB_UOM.setEnabled(False)

        Itm_Mtr.IQLE_Stock.setText(str(Itm_Mtr.OQTB_Product.model().index(index.row(), 10).data()))

        Itm_Mtr.IQCB_Active.clear()
        Itm_Mtr.IQCB_Active.addItems(Active_Status)
        Itm_Mtr.IQCB_Active.setCurrentIndex(
            Active_Status.index("Yes" if Itm_Mtr.OQTB_Product.model().index(index.row(), 11).data() == "Y" else "No"))
        Itm_Mtr.IQCB_Active.setEnabled(False)


        Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQLE", True)
        Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQTE", True)

    @Exception_Handle
    def Filter_Product_ViewTbl():
        if len(Itm_Mtr.OQLE_ProductFilter.text()) >0:
            # print(Itm_Mtr.IQLE_CustomerSearch.text())
            filter_SQL_Customer = fr'select product_id,barcode_code,product_name,tamil_name,cost_price,mrp,wholesale,retail,gst,uom,stock,active_status from product_info WHERE product_name LIKE "%{Itm_Mtr.OQLE_ProductFilter.text()}%" ORDER BY product_name'
            # print(filter_SQL_Customer)
            Push_TableView_SqlData('Product_Model', Itm_Mtr.OQTB_Product, filter_SQL_Customer)
        else:
            Product_Viewtbl_SQlData()

    @Exception_Handle
    def Enable_Add_Item(state):

        if state == Qt.Checked:
            print("yes")
            Itm_Mtr.IQPB_AddProduct.setEnabled(True)

            Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQLE", False)
            Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQTE", False)

        else:
            print("No")
            Itm_Mtr.IQPB_AddProduct.setEnabled(False)
            Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQLE", True)
            Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQTE", True)

        Update_Property(Itm_Mtr.Item_Frame, "Clear", "IQLE", True)
        Update_Property(Itm_Mtr.Item_Frame, "Clear", "IQTE", True)
        Itm_Mtr.IQLE_ProductID.setReadOnly(True)
        Itm_Mtr.IQLE_ProductID.setText(str(Maximum_Product_ID()))

        Itm_Mtr.IQCB_Active.clear()
        Itm_Mtr.IQCB_UOM.clear()

        Itm_Mtr.IQCB_Active.setEnabled(True)
        Itm_Mtr.IQCB_UOM.setEnabled(True)


        Itm_Mtr.IQCB_Active.addItems(Active_Status)
        Itm_Mtr.IQCB_UOM.addItems(Units_List)
        Itm_Mtr.OQTB_Product.selectionModel().clearSelection()

    @Exception_Handle
    def Enable_Update_Item(state):

        # selected_rows = Itm_Mtr.OQTB_Product.selectionModel().selectedRows()
        # index = selected_rows[-1]
        # Product_IPN = Itm_Mtr.OQTB_Product.model().index(index.row(), 0).data()
        # print(Product_IPN)


        if Itm_Mtr.IQLE_ProductName.text() != "":

            if state == Qt.Checked:
                print("Yes")
                Itm_Mtr.IQPB_UpdateProduct.setEnabled(True)

                Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQLE", False)
                Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQTE", False)


                Itm_Mtr.IQCB_Active.setEnabled(True)
                Itm_Mtr.IQCB_UOM.setEnabled(True)

                Index_Status = Active_Status.index(Itm_Mtr.IQCB_Active.currentText())
                Index_Unit = Units_List.index(Itm_Mtr.IQCB_UOM.currentText())

                Itm_Mtr.IQCB_Active.clear()
                Itm_Mtr.IQCB_UOM.clear()

                Itm_Mtr.IQCB_Active.addItems(Active_Status)
                Itm_Mtr.IQCB_UOM.addItems(Units_List)

                Itm_Mtr.IQCB_Active.setCurrentIndex(Index_Status)
                Itm_Mtr.IQCB_UOM.setCurrentIndex(Index_Unit)

            else:
                print("No")
                Itm_Mtr.IQPB_UpdateProduct.setEnabled(False)

                Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQLE", True)
                Update_Property(Itm_Mtr.Item_Frame, "Readonly", "IQTE", True)

                action = Itm_Mtr.IQCB_Active.currentText()
                uom = Itm_Mtr.IQCB_UOM.currentText()

                Itm_Mtr.IQCB_Active.clear()
                Itm_Mtr.IQCB_UOM.clear()

                Itm_Mtr.IQCB_Active.addItem(action)
                Itm_Mtr.IQCB_UOM.addItem(uom)

        else:
            Show_Msg_Infomation("Select The Product","Please Select the Product to be Updated........")
            # Itm_Mtr.IQCB_Update.setChecked(False)

        Itm_Mtr.IQLE_ProductID.setReadOnly(True)

    @Exception_Handle
    def Add_Product_Item():
        print("Add")
        dict = {
            'barcode_code' :  int(Itm_Mtr.IQLE_ProductID.text()) if Itm_Mtr.IQLE_BarcodeInput.text() == "" else int(Itm_Mtr.IQLE_BarcodeInput.text()),
            'product_name' : Itm_Mtr.IQLE_ProductName.text(),
            'tamil_name' : Itm_Mtr.IQLE_TamilName.text(),
            'cost_price' : float(Itm_Mtr.IQLE_PurchaseRate.text()),
            'mrp' : float(Itm_Mtr.IQLE_MRP.text()),
            'wholesale' : float(Itm_Mtr.IQLE_SalesPrice_W.text()),
            'retail' : float(Itm_Mtr.IQLE_SalesPrice_R.text()),
            'uom' : Itm_Mtr.IQCB_UOM.currentText(),
            'active_status' : "Y" if Itm_Mtr.IQCB_Active.currentText() == "Yes" else "N",
            'gst' : 0 if Itm_Mtr.IQLE_GST.text() == "" else float(Itm_Mtr.IQLE_GST.text()),
            'stock' : int(Itm_Mtr.IQLE_Stock.text())
        }
        tbl_nm = 'product_info'

        print(dict.values())

        if "" not in list(dict.values()):
            print("Yes")
            dbc = db.cursor()

            # Build dynamic SQL query
            columns = ', '.join(dict.keys())
            placeholders = ', '.join(['%s'] * len(dict))
            values = tuple(dict.values())

            sql = f"INSERT INTO {tbl_nm} ({columns}) VALUES {values}"
            dbc.execute(sql)

            print(sql)

            db.commit()

            Product_Viewtbl_SQlData()
            # Itm_Mtr.IQLE_ProductID.setText(str(Maximum_Product_ID()))


            Show_Msg_Infomation("Adding Product", "Product Has Been Added Successfully")
        else:
            Show_Msg_Infomation("Information", "Please Enter the nessessary Details ")

    @Exception_Handle
    def Update_Product_Item():
        print("Update")
        dict = {
            'barcode_code': int(Itm_Mtr.IQLE_ProductID.text()) if Itm_Mtr.IQLE_BarcodeInput.text() == "" else int(
                Itm_Mtr.IQLE_BarcodeInput.text()),
            'product_name': Itm_Mtr.IQLE_ProductName.text(),
            'tamil_name': Itm_Mtr.IQLE_TamilName.text(),
            'cost_price': float(Itm_Mtr.IQLE_PurchaseRate.text()),
            'mrp': float(Itm_Mtr.IQLE_MRP.text()),
            'wholesale': float(Itm_Mtr.IQLE_SalesPrice_W.text()),
            'retail': float(Itm_Mtr.IQLE_SalesPrice_R.text()),
            'uom': Itm_Mtr.IQCB_UOM.currentText(),
            'active_status': "Y" if Itm_Mtr.IQCB_Active.currentText() == "Yes" else "N",
            'gst': 0 if Itm_Mtr.IQLE_GST.text() == "" else float(Itm_Mtr.IQLE_GST.text()),
            'stock': int(Itm_Mtr.IQLE_Stock.text())
        }
        c_dict = {
            'product_id': int(Itm_Mtr.IQLE_ProductID.text()),
        }
        tbl_nm = 'product_info'

        print(dict.keys())
        print(dict.values())

        print(list(c_dict.values()))

        dbc = db.cursor()
        for key, value in dict.items():
            sql = f"UPDATE {tbl_nm} SET {key} = '{value}' WHERE {list(c_dict.keys())[0]} = {list(c_dict.values())[0]}"
            print(sql)
            dbc.execute(sql)
            db.commit()

        Product_Viewtbl_SQlData()
        Show_Msg_Infomation("Updating Product", "Product Has Been Updated Successfully")


    @Exception_Handle
    def Delete_Product_Data():
        selected_rows = Itm_Mtr.OQTB_Product.selectionModel().selectedRows()

        if len(selected_rows) >0:

            index = selected_rows[-1]
            Product_IPN = Itm_Mtr.OQTB_Product.model().index(index.row(), 0).data()

            dbc = db.cursor()
            sql = fr"DELETE FROM product_info WHERE product_id = {Product_IPN} "
            dbc.execute(sql)
            db.commit()

            Show_Msg_Infomation("Deleted Information", fr"The selected Product ID : {Product_IPN}\n"
                                                       fr"Product Name : {Itm_Mtr.OQTB_Product.model().index(index.row(), 1).data()}\n"
                                                       fr"Has Been Deleted Successfully...........")

            Update_Property(Itm_Mtr.Item_Frame, "Clear", "IQLE", True)
            Update_Property(Itm_Mtr.Item_Frame, "Clear", "IQTE", True)

            Itm_Mtr.IQCB_Active.clear()
            Itm_Mtr.IQCB_UOM.clear()

            Itm_Mtr.IQCB_Active.setEnabled(True)
            Itm_Mtr.IQCB_UOM.setEnabled(True)

            Itm_Mtr.IQCB_Active.addItems(Active_Status)
            Itm_Mtr.IQCB_UOM.addItems(Units_List)

            Product_Viewtbl_SQlData()

            Itm_Mtr.IQLE_ProductID.setReadOnly(True)
            Itm_Mtr.IQLE_ProductID.setText(str(Maximum_Product_ID()))



        else:
            Show_Msg_Infomation("Select The Product","........Please Select the Product to be Deleted........")



        Itm_Mtr.OQTB_Product.selectionModel().clearSelection()



    #------------ Generic/Supporting Definitions ----------------------
    @Exception_Handle
    def Product_Viewtbl_SQlData():
        SQL_Product = 'select product_id,barcode_code,product_name,tamil_name,cost_price,mrp,wholesale,retail,gst,uom,stock,active_status from product_info order by product_name'
        Push_TableView_SqlData('Product_Model', Itm_Mtr.OQTB_Product, SQL_Product)

    @Exception_Handle
    def Maximum_Product_ID():
        sql = fr"select max(product_id)+1 from product_info"
        Maxi_Prod_ID = DB_Fetch(sql, False, "LOE")
        return fr"{Maxi_Prod_ID[-1]}"






    ### General Code Running
    Product_Viewtbl_SQlData()
    Itm_Mtr.IQLE_ProductID.setText(str(Maximum_Product_ID()))




    #------------------Function & Connection ------------------------
    Itm_Mtr.OQTB_Product.clicked.connect(lambda: On_Clicked_Product_TblView())

    Itm_Mtr.OQLE_ProductFilter.textChanged.connect(lambda :Filter_Product_ViewTbl())

    Itm_Mtr.IQCB_Add.stateChanged.connect(Enable_Add_Item)

    Itm_Mtr.IQCB_Update.stateChanged.connect(Enable_Update_Item)

    Itm_Mtr.IQPB_AddProduct.clicked.connect(lambda: Add_Product_Item())

    Itm_Mtr.IQPB_UpdateProduct.clicked.connect(lambda: Update_Product_Item())

    Itm_Mtr.IQPB_DeleteProduct.clicked.connect(lambda: Delete_Product_Data())


if __name__ == "__main__":
    print("XX")
    Item_Master_FN(Itm_Mtr)
    Itm_Mtr.showMaximized()
    sys.exit(app.exec_())
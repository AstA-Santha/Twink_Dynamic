# ldir = fr"G:\GIt Workspsce\Twink_ERP"
# Itm_Mtr = uic.loadUi(fr'{ldir}\MODULES\ITEM_MASTER\UI-ItemMaster.ui')
from Env import *

@Exception_Handle
def Item_Master_FN(Itm_Mtr):
    Units_List = ["Kg", "Nos", "Ton"]

    print("------------Item Master Started-------------")
    
    ## ------- Customer/Supplier Definition Starts Here ---------
    @Exception_Handle
    def Add_Customer():

        print("Add Customer")

        print(Itm_Mtr.IQLE_CustomerName.text())
        print(Itm_Mtr.IQLE_MobileNo.text())
        print(Itm_Mtr.IQLE_CustomerGST.text())
        print(Itm_Mtr.IQLE_CustomerEmail.text())
        print(Itm_Mtr.IQTE_Street.toPlainText())
        print(Itm_Mtr.IQLE_District.text())
        print(Itm_Mtr.IQLE_Pincode.text())
        print(Itm_Mtr.IQLE_State.text())

        print(Itm_Mtr.IQLE_SPOCName.text())
        print(Itm_Mtr.IQLE_SPOCPhoneNo.text())
        print(Itm_Mtr.IQLE_CustomerTag.text())
        print(Itm_Mtr.IQLE_CustomerRemarks.text())
        print(Itm_Mtr.IQCB_Supplier.currentText())

        misc_dict = {}
        if Itm_Mtr.IQLE_SPOCName.text() != "" :
            misc_dict['Name'] = Itm_Mtr.IQLE_SPOCName.text()
        if Itm_Mtr.IQLE_SPOCPhoneNo.text() != "" :
            misc_dict['Number'] = Itm_Mtr.IQLE_SPOCPhoneNo.text()
        if Itm_Mtr.IQLE_CustomerTag.text() != "" :
            misc_dict['Tag'] = Itm_Mtr.IQLE_CustomerTag.text()


        # misc_json = json.dumps({"Name":Itm_Mtr.IQLE_SPOCName.text(),
        #     "Number":Itm_Mtr.IQLE_SPOCPhoneNo.text(),
        #     "Tag":Itm_Mtr.IQLE_CustomerTag.text()})

        # misc_json = json.dumps(misc_dict)

        supplier = "N" if Itm_Mtr.IQCB_Supplier.currentText() == "Opt-Out" else ("Y" if Itm_Mtr.IQCB_Supplier.currentText() == "Opt-In" else "B")

        dict = {
            'Customer_Name': Itm_Mtr.IQLE_CustomerName.text(),
            'GST': Itm_Mtr.IQLE_CustomerGST.text(),
            'Mobile': Itm_Mtr.IQLE_MobileNo.text(),
            'Email': Itm_Mtr.IQLE_CustomerEmail.text(),
            'Address': Itm_Mtr.IQTE_Street.toPlainText(),
            'District': Itm_Mtr.IQLE_District.text(),
            'State': Itm_Mtr.IQLE_State.text(),
            'Pincode': Itm_Mtr.IQLE_Pincode.text(),

            'Misc': json.dumps(misc_dict),

            'Remarks': Itm_Mtr.IQLE_CustomerRemarks.text(),
            'active': 'Y',
            'Supplier': supplier
        }
        tbl_nm = 'customer_info'

        dbc = db.cursor()

        # Build dynamic SQL query
        columns = ', '.join(dict.keys())
        placeholders = ', '.join(['%s'] * len(dict))
        values = tuple(dict.values())

        sql = f"INSERT INTO {tbl_nm} ({columns}) VALUES ({placeholders})"
        dbc.execute(sql, values)
        # print(sql)
        # print(values)
        db.commit()

        Customer_Viewtbl_SQlData()
        Product_Window_Customer_Lst()
        Show_Msg_Infomation("Adding Customer", "Customer Has Been Added Successfully")

    @Exception_Handle
    def Update_Customer():
        print("Update Customer")
        selected_rows = Itm_Mtr.OQTB_CustomerDetails.selectionModel().selectedRows()
        index = selected_rows[-1]
        customer_uid = Itm_Mtr.OQTB_CustomerDetails.model().index(index.row(), 0).data()
        print(customer_uid)

        misc_dict = {}
        if Itm_Mtr.IQLE_SPOCName.text() != "" and Itm_Mtr.IQLE_SPOCName.text() != "No Data" :
            misc_dict['Name'] = Itm_Mtr.IQLE_SPOCName.text()
        if Itm_Mtr.IQLE_SPOCPhoneNo.text() != "" and Itm_Mtr.IQLE_SPOCPhoneNo.text() != "No Data":
            misc_dict['Number'] = Itm_Mtr.IQLE_SPOCPhoneNo.text()
        if Itm_Mtr.IQLE_CustomerTag.text() != "" and Itm_Mtr.IQLE_CustomerTag.text() != "No Data":
            misc_dict['Tag'] = Itm_Mtr.IQLE_CustomerTag.text()

        supplier = "N" if Itm_Mtr.IQCB_Supplier.currentText() == "Opt-Out" else ("Y" if Itm_Mtr.IQCB_Supplier.currentText() == "Opt-In" else "B")

        dict = {
            'Customer_Name': Itm_Mtr.IQLE_CustomerName.text(),
            'GST': Itm_Mtr.IQLE_CustomerGST.text(),
            'Mobile': Itm_Mtr.IQLE_MobileNo.text(),
            'Email': Itm_Mtr.IQLE_CustomerEmail.text(),
            'Address': Itm_Mtr.IQTE_Street.toPlainText(),
            'District': Itm_Mtr.IQLE_District.text(),
            'State': Itm_Mtr.IQLE_State.text(),
            'Pincode': Itm_Mtr.IQLE_Pincode.text(),

            'Misc': json.dumps(misc_dict),

            'Remarks': Itm_Mtr.IQLE_CustomerRemarks.text(),
            'active': 'Y',
            'Supplier': supplier
        }
        c_dict = {
            'UID': customer_uid,
        }

        dbc = db.cursor()
        for key, value in dict.items():
            # sql = f"UPDATE customer_info SET {key} = %s WHERE UID = %s"
            sql = f"UPDATE customer_info SET {key} = '{value}' WHERE UID = {c_dict['UID']}"
            print(sql)
            dbc.execute(sql)
            # dbc.execute(sql, (value, c_dict['UID']))
            db.commit()


        Customer_Viewtbl_SQlData()
        Product_Window_Customer_Lst()

        Itm_Mtr.IQCB_CustomerProduct.setCurrentIndex(Customer_List.index(Itm_Mtr.IQLE_CustomerName.text()))

        Show_Msg_Infomation("Update Customer","Customer Data Has been Uodated ")

        Itm_Mtr.IQPB_UpdateCustomer.setEnabled(False)

        Itm_Mtr.OQTB_CustomerDetails.selectionModel().select(Itm_Mtr.OQTB_CustomerDetails.model().index(index.row(), 0),
                                     QItemSelectionModel.Select | QItemSelectionModel.Rows)

    @Exception_Handle
    def On_Clicked_Customer_TblView(index):

        Customer_uid = models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 0))

        Itm_Mtr.IQCB_CustomerProduct.setCurrentIndex(Customer_List.index(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 1))))

        print(Customer_List.index(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 1))),"Customer")

        Itm_Mtr.IQLE_CustomerName.setText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 1)))
        Itm_Mtr.IQLE_MobileNo.setText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 3)))
        Itm_Mtr.IQLE_CustomerGST.setText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 2)))
        Itm_Mtr.IQLE_CustomerEmail.setText(
            models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 5)))
        Itm_Mtr.IQTE_Street.setPlainText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 6)))
        Itm_Mtr.IQLE_District.setText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 4)))
        Itm_Mtr.IQLE_Pincode.setText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 8)))
        Itm_Mtr.IQLE_State.setText(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 7)))
        Itm_Mtr.IQLE_CustomerRemarks.setText(
            models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 9)))
        # ["Opt-Out", "Opt-In", "Both"]

        Supplier_Data = models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 12))
        Itm_Mtr.IQCB_Supplier.clear()
        Itm_Mtr.IQCB_Supplier.addItem("Opt-Out") if Supplier_Data == "N" else (
            Itm_Mtr.IQCB_Supplier.addItem("Opt-In") if Supplier_Data == "Y" else Itm_Mtr.IQCB_Supplier.addItem("Both"))

        Misc_Dict = json.loads(
            "{}" if len(models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 10))) == 0 else
            models['Customer_Model'].data(models['Customer_Model'].index(index.row(), 10)))

        Itm_Mtr.IQLE_SPOCName.setText(Misc_Dict.get('Name', "No Data"))
        Itm_Mtr.IQLE_SPOCPhoneNo.setText(Misc_Dict.get('Number', "No Data"))
        Itm_Mtr.IQLE_CustomerTag.setText(Misc_Dict.get('Tag', "No Data"))

        Product_Viewtbl_Update()

        if Itm_Mtr.IQC_UpdateCustomer.isChecked():
            Itm_Mtr.IQPB_UpdateCustomer.setEnabled(True)
            Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQLE", False)
            Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQTE", False)

        else:
            Itm_Mtr.IQPB_UpdateCustomer.setEnabled(False)

    @Exception_Handle
    def On_Add_Customer_CheckBox_Changed(state):
        if state == Qt.Checked:
            Itm_Mtr.IQPB_AddCustomer.setEnabled(True)

            Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQLE", False)
            Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQTE", False)
            Update_Property(Itm_Mtr.Customer_Frame, "Clear", "IQLE", False)
            Update_Property(Itm_Mtr.Customer_Frame, "Clear", "IQTE", False)

            Itm_Mtr.IQCB_Supplier.setEnabled(True)
            Itm_Mtr.IQCB_Supplier.clear()
            Itm_Mtr.IQCB_Supplier.addItems(["Opt-Out", "Opt-In", "Both"])

        else:
            Itm_Mtr.IQPB_AddCustomer.setEnabled(False)

            Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQLE", True)
            Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQTE", True)
            Update_Property(Itm_Mtr.Customer_Frame, "Clear", "IQLE", True)
            Update_Property(Itm_Mtr.Customer_Frame, "Clear", "IQTE", True)

            Itm_Mtr.IQCB_Supplier.setEnabled(True)  # You may want to disable it?
            Itm_Mtr.IQCB_Supplier.clear()
            Itm_Mtr.IQCB_Supplier.addItems(["Opt-Out", "Opt-In", "Both"])

    @Exception_Handle
    def On_Update_Customer_CheckBox_Changed(state):
        print("hi")
        if state == Qt.Checked:
            if Itm_Mtr.IQLE_CustomerName.text() == "":
                print("Select the Item")
                Show_Msg_Infomation("Select the Customer","Please Select the Customer To Be Updated")
                # Itm_Mtr.IQC_UpdateCustomer.setChecked(False)
                Itm_Mtr.IQPB_UpdateCustomer.setEnabled(False)

            else:
                print("selecte 1")
                Itm_Mtr.IQPB_UpdateCustomer.setEnabled(True)
                Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQLE", False)
                Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQTE", False)

                Itm_Mtr.IQCB_Supplier.setEnabled(True)
                Itm_Mtr.IQCB_Supplier.clear()
                Itm_Mtr.IQCB_Supplier.addItems(["Opt-Out", "Opt-In", "Both"])

        else:
            if Itm_Mtr.IQLE_CustomerName.text() == "":
                print("please selecte 2")
                Show_Msg_Infomation("Select the Customer", "Please Select the Customer To Be Updated")
                # Itm_Mtr.IQC_UpdateCustomer.setChecked(False)
                Itm_Mtr.IQPB_UpdateCustomer.setEnabled(False)

            else:
                print("selecte 2")

                Itm_Mtr.IQPB_UpdateCustomer.setEnabled(False)

                Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQLE", True)
                Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQTE", True)

                Itm_Mtr.IQCB_Supplier.setEnabled(True)
                Itm_Mtr.IQCB_Supplier.clear()
                Itm_Mtr.IQCB_Supplier.addItems(["Opt-Out", "Opt-In", "Both"])

    @Exception_Handle
    def Filter_Customer_ViewTbl():
        if len(Itm_Mtr.IQLE_CustomerSearch.text()) >0:
            # print(Itm_Mtr.IQLE_CustomerSearch.text())
            filter_SQL_Customer = fr'SELECT UID, Customer_Name, GST, Mobile, District, Email, Address, State, Pincode, Remarks, Misc, active, Supplier FROM customer_info WHERE active = "Y" AND Customer_Name LIKE "%{Itm_Mtr.IQLE_CustomerSearch.text()}%" ORDER BY Customer_Name'
            # print(filter_SQL_Customer)
            Push_TableView_SqlData('Customer_Model', Itm_Mtr.OQTB_CustomerDetails, filter_SQL_Customer)
        else:
            Customer_Viewtbl_SQlData()


    ## ============== Product Definition Starts Here ============
    @Exception_Handle
    def Add_Product():
        print("Add Customer")
        print(Itm_Mtr.IQLE_ProductName.text())
        print(Itm_Mtr.IQLE_IPN.text())
        print(Itm_Mtr.IQLE_EPN.text())
        print(Itm_Mtr.IQLE_Price.text())
        print(Itm_Mtr.IQLE_SGST.text())
        print(Itm_Mtr.IQLE_CGST.text())
        print(Itm_Mtr.IQLE_HSN.text())

        Misc_Product_Dict = {}
        if Itm_Mtr.IQC_ToPrint.isChecked():
            Misc_Product_Dict['To_Print'] = 1
        else:
            Misc_Product_Dict['To_Print'] = 0

        if Itm_Mtr.IQTE_ProductRemarks.toPlainText() == "":
            Misc_Product_Dict['Remarks'] = "NA"
        else:
            Misc_Product_Dict['Remarks'] = Itm_Mtr.IQTE_ProductRemarks.toPlainText()

        dict = {
            'IPN' : Itm_Mtr.IQLE_IPN.text(),
            'EPN' : Itm_Mtr.IQLE_EPN.text(),
            'Product_Name' : Itm_Mtr.IQLE_ProductName.text(),
            'HSN' : Itm_Mtr.IQLE_HSN.text(),
            'GST_Slab' : fr"{Itm_Mtr.IQLE_SGST.text()},{Itm_Mtr.IQLE_CGST.text()}",
            'UOM' : Itm_Mtr.IQCB_UOM.currentText(),
            'Price' :Itm_Mtr.IQLE_Price.text(),
            'Misc' : json.dumps(Misc_Product_Dict),
            'Active' :"Y",
        }
        tbl_nm = 'product_info'

        dbc = db.cursor()
        # # Build dynamic SQL query
        columns = ', '.join(dict.keys())
        placeholders = ', '.join(['%s'] * len(dict))
        values = tuple(dict.values())
        # sql = f"INSERT INTO {tbl_nm} ({columns}) VALUES ({placeholders})"
        # dbc.execute(sql, values)
        sql = f"INSERT INTO {tbl_nm} ({columns}) VALUES {values}"
        print(sql)
        dbc.execute(sql)
        db.commit()

        customer_id = DB_Fetch(fr"select UID from customer_info where Customer_Name = '{Itm_Mtr.IQCB_CustomerProduct.currentText()}'",True,"LOE")

        dict = {
            'customer_id': customer_id[-1],
            'product_id': Itm_Mtr.IQLE_IPN.text(),
        }
        tbl_nm = "customer_product"

        dbc = db.cursor()
        # # Build dynamic SQL query
        columns = ', '.join(dict.keys())
        values = tuple(dict.values())
        sql = f"INSERT INTO {tbl_nm} ({columns}) VALUES {values}"
        print(sql)
        dbc.execute(sql)
        db.commit()

        Product_Viewtbl_Update()

        Show_Msg_Infomation("Add Product", "Product Has Been Added Successfully")

    @Exception_Handle
    def Update_Product():
        print("Update Customer")

        Misc_Product_Dict = {}
        if Itm_Mtr.IQC_ToPrint.isChecked():
            Misc_Product_Dict['To_Print'] = 1
        else:
            Misc_Product_Dict['To_Print'] = 0

        if Itm_Mtr.IQTE_ProductRemarks.toPlainText() == "":
            Misc_Product_Dict['Remarks'] = "NA"
        else:
            Misc_Product_Dict['Remarks'] = Itm_Mtr.IQTE_ProductRemarks.toPlainText()

        print(Misc_Product_Dict)

        dict = {
            'EPN': Itm_Mtr.IQLE_EPN.text(),
            'Product_Name': Itm_Mtr.IQLE_ProductName.text(),
            'HSN': Itm_Mtr.IQLE_HSN.text(),
            'GST_Slab': fr"{Itm_Mtr.IQLE_SGST.text()},{Itm_Mtr.IQLE_CGST.text()}",
            'UOM': Itm_Mtr.IQCB_UOM.currentText(),
            'Price': Itm_Mtr.IQLE_Price.text(),
            'Misc': json.dumps(Misc_Product_Dict),

        }
        #
        c_dict = {
            'IPN': Itm_Mtr.IQLE_IPN.text(),
        }
        tbl_nm = "product_info"

        dbc = db.cursor()
        for key, value in dict.items():
            # sql = f"UPDATE customer_info SET {key} = %s WHERE UID = %s"

            sql = f"UPDATE {tbl_nm} SET {key} = '{value}' WHERE {list(c_dict.keys())[0]} = '{list(c_dict.values())[0]}'"
            print(sql)
            dbc.execute(sql)
            # dbc.execute(sql, (value, c_dict['UID']))
            db.commit()

        Product_Viewtbl_Update()
        Show_Msg_Infomation("Update Product", "Product Data Has been Uodated ")

        Itm_Mtr.IQPB_UpdateProduct.setEnabled(False)

    @Exception_Handle
    def Fetch_Product_Customer_ComboBox():

        Itm_Mtr.OQTB_CustomerDetails.selectionModel().clearSelection()


        # print(Itm_Mtr.IQCB_CustomerProduct.currentText())
        SQL_Product_ComboBox = fr"select IPN,EPN,Product_Name,HSN,GST_Slab,UOM,Price,Misc from product_info where IPN in (select product_id from customer_product where customer_id = (select UID from customer_info where Customer_Name = '{Itm_Mtr.IQCB_CustomerProduct.currentText()}'))"
        Push_TableView_SqlData('Product_Model', Itm_Mtr.OQTB_ProductDetails, SQL_Product_ComboBox)

        Update_Property(Itm_Mtr.Product_Frame, "Clear", "IQLE", False)
        Update_Property(Itm_Mtr.Product_Frame, "Clear", "IQTE", False)
        Itm_Mtr.IQCB_UOM.setEnabled(True)
        Itm_Mtr.IQCB_UOM.clear()
        Itm_Mtr.IQCB_UOM.addItems(["Kg", "Nos", "Ton"])

    @Exception_Handle
    def On_Clicked_Product_TblView():

        selected_rows = Itm_Mtr.OQTB_ProductDetails.selectionModel().selectedRows()
        index = selected_rows[-1]
        Product_IPN = Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 0).data()
        # print(Product_IPN)

        # IPN 0, EPN 1, Product_Name 2, HSN 3, GST_Slab 4, UOM 5, Price 6, Remarks 7

        Itm_Mtr.IQLE_ProductName.setText(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 2).data())
        Itm_Mtr.IQLE_IPN.setText(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 0).data())
        Itm_Mtr.IQLE_EPN.setText(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 1).data())
        Itm_Mtr.IQLE_Price.setText(str(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 6).data()))
        Itm_Mtr.IQLE_SGST.setText(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 4).data().split(",")[0])
        Itm_Mtr.IQLE_CGST.setText(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 4).data().split(",")[1])
        Itm_Mtr.IQLE_HSN.setText(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 3).data())

        misc_dict = json.loads(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 7).data())
        Itm_Mtr.IQC_ToPrint.setChecked(True) if misc_dict['To_Print'] == 1 else Itm_Mtr.IQC_ToPrint.setChecked(False)
        Itm_Mtr.IQTE_ProductRemarks.setText(misc_dict['Remarks'])



        Itm_Mtr.IQCB_UOM.setCurrentIndex(Units_List.index(Itm_Mtr.OQTB_ProductDetails.model().index(index.row(), 5).data()))


        if Itm_Mtr.IQC_UpdateProduct.isChecked():
            Itm_Mtr.IQPB_UpdateProduct.setEnabled(True)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQLE", False)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQTE", False)

        else:
            Itm_Mtr.IQPB_UpdateProduct.setEnabled(False)

        Itm_Mtr.IQLE_IPN.setReadOnly(True)

    @Exception_Handle
    def On_Add_Product_CheckBox_Changed(state):

        if state == Qt.Checked:
            # print("hello clicked")

            Itm_Mtr.IQCB_CustomerProduct.setEnabled(False)
            Itm_Mtr.IQPB_AddProduct.setEnabled(True)

            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQLE", False)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQTE", False)

        else:
            Itm_Mtr.IQCB_CustomerProduct.setEnabled(True)
            # print("Not  clicked")
            Itm_Mtr.IQPB_AddProduct.setEnabled(False)

            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQLE", True)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQTE", True)

        Update_Property(Itm_Mtr.Product_Frame, "Clear", "IQLE", False)
        Update_Property(Itm_Mtr.Product_Frame, "Clear", "IQTE", False)
        Itm_Mtr.IQCB_UOM.setEnabled(True)
        Itm_Mtr.IQCB_UOM.clear()
        Itm_Mtr.IQCB_UOM.addItems(Units_List)

        Itm_Mtr.IQLE_IPN.setReadOnly(True)
        Itm_Mtr.IQLE_IPN.setText(Maximum_IPN())

    @Exception_Handle
    def On_Update_Product_CheckBox_Changed(state):

        if state == Qt.Checked and Itm_Mtr.IQLE_ProductName.text() != "":
            Itm_Mtr.IQCB_CustomerProduct.setEnabled(False)
            Itm_Mtr.IQPB_UpdateProduct.setEnabled(True)

            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQLE", False)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQTE", False)

            print("Clicked")
        elif state != Qt.Checked :
            Itm_Mtr.IQCB_CustomerProduct.setEnabled(True)
            Itm_Mtr.IQPB_UpdateProduct.setEnabled(False)
            print("Nont Clicked")
            Update_Property(Itm_Mtr.Product_Frame, "Clear", "IQLE", True)
            Update_Property(Itm_Mtr.Product_Frame, "Clear", "IQTE", True)
            Itm_Mtr.IQCB_UOM.setEnabled(True)
            Itm_Mtr.IQCB_UOM.clear()
            Itm_Mtr.IQCB_UOM.addItems(Units_List)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQLE", True)
            Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQTE", True)
            Itm_Mtr.IQC_ToPrint.setChecked(False)
        else:
            Itm_Mtr.IQCB_CustomerProduct.setEnabled(False)
        Itm_Mtr.IQLE_IPN.setReadOnly(True)



    #------------ Generic/Supporting Definitions ----------------------
    @Exception_Handle
    def Customer_Viewtbl_SQlData():
        SQL_Customer = 'select UID, Customer_Name, GST, Mobile, District, Email, Address, State,Pincode, Remarks, Misc, active, Supplier from customer_info where active = "Y" order by Customer_Name'
        Push_TableView_SqlData('Customer_Model',Itm_Mtr.OQTB_CustomerDetails, SQL_Customer)

        # for col in [0, 5, 6, 7, 8, 9, 10, 11, 12]:
        #     Itm_Mtr.OQTB_CustomerDetails.hideColumn(col)

    @Exception_Handle
    def Product_Window_Customer_Lst():
        global Customer_List
        sql = "select Customer_Name from customer_info order by Customer_Name asc"
        Customer_List = DB_Fetch(sql, False, "LOE")
        # globals()['Customer_List'] = "select Customer_Name from customer_info order by Customer_Name asc"
        # print(DB_Fetch(Customer_List, False, "LOE"))
        Itm_Mtr.IQCB_CustomerProduct.setEnabled(True)
        Itm_Mtr.IQCB_CustomerProduct.clear()
        Itm_Mtr.IQCB_CustomerProduct.addItems(Customer_List)

    @Exception_Handle
    def Maximum_IPN():
        sql = 'SELECT MAX(CAST(RIGHT(IPN, LENGTH(IPN) - 2) AS UNSIGNED))+1 FROM product_info'
        Max_Ipn = DB_Fetch(sql, False, "LOE")

        return fr"AT{Max_Ipn[-1]}"

    @Exception_Handle
    def Product_Viewtbl_Update():
        SQL_Product_ComboBox = fr"select IPN,EPN,Product_Name,HSN,GST_Slab,UOM,Price,Misc from product_info where IPN in (select product_id from customer_product where customer_id = (select UID from customer_info where Customer_Name = '{Itm_Mtr.IQCB_CustomerProduct.currentText()}'))"
        Push_TableView_SqlData('Product_Model', Itm_Mtr.OQTB_ProductDetails, SQL_Product_ComboBox)




    # ---------------- Generic Finctionality --------------

    Customer_Viewtbl_SQlData()
    Product_Window_Customer_Lst()
    Product_Viewtbl_Update()

    Update_Property(Itm_Mtr.Customer_Frame,"Readonly","IQLE",True)
    Update_Property(Itm_Mtr.Customer_Frame, "Readonly", "IQTE", True)

    Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQLE", True)
    Update_Property(Itm_Mtr.Product_Frame, "Readonly", "IQTE", True)


    # # sql = 'select Customer_Name,gst from customer_info'
    # model.setQuery(sql, db)
    # Itm_Mtr.OQTB_CustomerDetails.setModel(model)


    # ------- UI Signal Connection Functionality Starts Here ----------

    #---------- Customer --------------
    Itm_Mtr.IQPB_AddCustomer.clicked.connect(lambda : Add_Customer())
    Itm_Mtr.IQPB_UpdateCustomer.clicked.connect(lambda : Update_Customer())

    Itm_Mtr.OQTB_CustomerDetails.clicked.connect(On_Clicked_Customer_TblView)

    Itm_Mtr.IQC_AddCustomer.stateChanged.connect(On_Add_Customer_CheckBox_Changed)

    Itm_Mtr.IQC_UpdateCustomer.stateChanged.connect(On_Update_Customer_CheckBox_Changed)

    Itm_Mtr.IQLE_CustomerSearch.textChanged.connect(lambda :Filter_Customer_ViewTbl())



    #--------- Product ---------------

    Itm_Mtr.IQCB_CustomerProduct.activated.connect(lambda : Fetch_Product_Customer_ComboBox())

    Itm_Mtr.OQTB_ProductDetails.clicked.connect(lambda: On_Clicked_Product_TblView())

    Itm_Mtr.IQC_AddProduct.stateChanged.connect(On_Add_Product_CheckBox_Changed)
    Itm_Mtr.IQC_UpdateProduct.stateChanged.connect(On_Update_Product_CheckBox_Changed)


    Itm_Mtr.IQPB_AddProduct.clicked.connect(lambda: Add_Product())
    Itm_Mtr.IQPB_UpdateProduct.clicked.connect(lambda: Update_Product())

    # Itm_Mtr.IQC_AddProduct.stateChanged.connect(
    #     lambda state: Itm_Mtr.IQPB_AddProduct.setEnabled(True) if state == Qt.Checked else Itm_Mtr.IQPB_AddProduct.setEnabled(False))
    #
    # Itm_Mtr.IQC_UpdateProduct.stateChanged.connect(
    #     lambda state: Itm_Mtr.IQPB_UpdateProduct.setEnabled(True) if state == Qt.Checked else Itm_Mtr.IQPB_UpdateProduct.setEnabled(False))




if __name__ == "__main__":
    print("XX")
    Item_Master_FN(Itm_Mtr)
    Itm_Mtr.showMaximized()
    sys.exit(app.exec_())
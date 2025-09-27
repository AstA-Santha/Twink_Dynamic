from BENV import *
from ICONS import ICONS_rc
from PyQt5.QtCore import QObject, QEvent
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
#--- UI Imports ---
Itm_Mtr = uic.loadUi(fr'{os.path.dirname(os.path.abspath(__file__))}\MODULES\ITEM_MASTER\UI-ItemMaster-.ui')
Inv_Mtr = uic.loadUi(fr'{os.path.dirname(os.path.abspath(__file__))}\MODULES\INVOICE_MASTER\UI_InvoiceMaster.ui')

#--- Keyboard Event Functions ---
class KeyFilter(QObject):
    @Exception_Handle
    def eventFilter(self, obj, event):
        if event.type() == QEvent.KeyPress:
            # print("Key pressed:", event.text(), "Code:", event.key())
            focused = QApplication.focusWidget()
            chain = []
            w = focused
            while w is not None:
                # name = w.objectName() if w.objectName() else w.__class__.__name__
                # chain.append(name)
                chain.append(w)
                w = w.parentWidget()
            print()
            if Inv_Mtr.IQTB_BillList in chain and Inv_Mtr.IQTB_BillList.currentColumn() == 0 and (event.key() == Qt.Key_Up or event.key() == Qt.Key_Down):
                Inv_Mtr.IQTB_ProductList.setFocus(True)

        return super().eventFilter(obj, event)

filter = KeyFilter()
app.installEventFilter(filter)


#--- Fetch Row_TableView  ---
def get_row_values(tableView, row):
    model = tableView.model()
    return [model.data(model.index(row, col)) for col in range(model.columnCount())]
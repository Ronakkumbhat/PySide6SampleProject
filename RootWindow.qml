import QtQuick
import QtQuick.Controls


ApplicationWindow{

    id:root
    title: "PySide6 QML Bridge"
    visible: true
    height: 800
    width: 800

    property var pr_var: bridge.a
    Component.onCompleted: {
        console.log("from qml", bridge.getText())
        console.log("from qml1", bridge.getColor("red"))

        bridge.textChanged()
       // console.log("from qml2", pr_var)
        bridge.a = [1,2,3]
        bridge.appendValue(7)
    }

    onPr_varChanged: {
        console.log("from qml3", pr_var)
    }

}

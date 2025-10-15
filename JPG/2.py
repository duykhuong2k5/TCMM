#!/usr/bin/env python3
"""
LAB: Cơ chế trích xuất và kích hoạt mã độc từ file JPG
"""
import base64
import os
import struct
import subprocess
import tempfile

class MalwareExtractor:
    def __init__(self):
        self.extracted_data = []
    
    def extract_from_metadata(self, jpg_path):
        """Trích xuất mã độc từ metadata"""
        print("🔍 Đang trích xuất mã độc từ metadata...")
        
        with open(jpg_path, 'rb') as f:
            data = f.read()
        
        # Tìm và trích xuất comment sections
        pos = 0
        while pos < len(data) - 1:
            if data[pos:pos+2] == b'\xff\xfe':  # Comment marker
                if pos + 4 < len(data):
                    length = struct.unpack('>H', data[pos+2:pos+4])[0]
                    comment_data = data[pos+4:pos+2+length]
                    
                    # Kiểm tra nếu là base64
                    try:
                        text = comment_data.decode('utf-8', errors='ignore')
                        if len(text) > 10:
                            # Thử decode base64
                            try:
                                decoded = base64.b64decode(text)
                                decoded_str = decoded.decode('utf-8', errors='ignore')
                                if 'function' in decoded_str or 'fetch' in decoded_str:
                                    print("✅ Phát hiện JavaScript mã độc trong metadata")
                                    self.extracted_data.append(('metadata_js', decoded_str))
                            except:
                                pass
                    except:
                        pass
                    
                    pos += 2 + length
                else:
                    break
            pos += 1
    
    def extract_from_appended_data(self, jpg_path):
        """Trích xuất từ data sau EOI marker"""
        print("🔍 Đang trích xuất từ appended data...")
        
        with open(jpg_path, 'rb') as f:
            data = f.read()
        
        # Tìm EOI marker
        eoi_pos = data.find(b'\xff\xd9')
        if eoi_pos != -1 and len(data) > eoi_pos + 2:
            appended_data = data[eoi_pos+2:]
            
            # Kiểm tra executable signatures
            if b'MZ' in appended_data or b'PE' in appended_data:
                print("✅ Phát hiện executable data appended")
                self.extracted_data.append(('executable', appended_data))
            
            # Kiểm tra base64 data
            try:
                text = appended_data.decode('utf-8', errors='ignore')
                if 'base64' in text.lower():
                    print("✅ Phát hiện base64 encoded data")
            except:
                pass
    
    def simulate_malware_execution(self):
        """Mô phỏng thực thi mã độc"""
        print("\n⚡ MÔ PHỎNG KÍCH HOẠT MÃ ĐỘC")
        print("=" * 50)
        
        for data_type, content in self.extracted_data:
            if data_type == 'metadata_js':
                print("🔓 Thực thi JavaScript mã độc (mô phỏng):")
                print(f"   {content[:100]}...")
                
                # Mô phỏng đánh cắp thông tin trình duyệt
                self.simulate_browser_data_theft()
                
            elif data_type == 'executable':
                print("🔓 Phát hiện file thực thi (mô phỏng chạy)")
                self.simulate_executable_execution()
    
    def simulate_browser_data_theft(self):
        """Mô phỏng đánh cắp dữ liệu trình duyệt"""
        print("🎯 MÔ PHỎNG ĐÁNH CẮP DỮ LIỆU TRÌNH DUYỆT:")
        
        # Giả lập các loại dữ liệu bị đánh cắp
        stolen_data = {
            'browser_passwords': [
                {'url': 'https://facebook.com', 'username': 'user123', 'password': 'pass123'},
                {'url': 'https://gmail.com', 'username': 'test@gmail.com', 'password': 'emailpass'}
            ],
            'cookies': [
                {'domain': '.facebook.com', 'name': 'session_id', 'value': 'fake_session_123'},
                {'domain': '.google.com', 'name': 'auth_token', 'value': 'fake_token_456'}
            ],
            'autofill_data': {
                'credit_cards': ['**** **** **** 1234'],
                'addresses': ['123 Main St, City, Country']
            }
        }
        
        print("   📧 Passwords từ trình duyệt: ĐÃ ĐÁNH CẮP")
        print("   🍪 Cookies phiên đăng nhập: ĐÃ ĐÁNH CẮP") 
        print("   💳 Thông tin thẻ tín dụng: ĐÃ ĐÁNH CẮP")
        
        return stolen_data
    
    def simulate_executable_execution(self):
        """Mô phỏng thực thi file EXE"""
        print("   💻 Downloader được kích hoạt (mô phỏng)")
        print("   📥 Đang tải payload thứ cấp...")
        
        # Giả lập download các malware khác
        secondary_payloads = [
            "Vidar Stealer - Thu thập credential",
            "Raccoon Stealer - Đánh cắp thông tin",
            "Redline Stealer - Thu thập system info"
        ]
        
        for payload in secondary_payloads:
            print(f"      ⬇️  {payload}")
        
        print("   🔧 Cài đặt persistence...")
        print("   📡 Thiết lập kết nối C2...")

# Sử dụng extractor
extractor = MalwareExtractor()
extractor.extract_from_metadata(malicious_file)
extractor.extract_from_appended_data(malicious_file)
extractor.simulate_malware_execution()
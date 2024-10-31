# đây là đoạn code để lấy lần lượt giá trị ở sheet DataSep ở Tab2 với api google credentials
import gspread
import pandas as pd
# nhớ lấy api của G.s vào đây trước mới làm được
credentials = {...}
gc = gspread.service_account_from_dict(credentials)

# Mở bảng tính Google Sheets
def get_sheet_data(credentials,ggsheet_name,tab_name):
    gc = gspread.service_account_from_dict(credentials)
    sh = gc.open(ggsheet_name)
    worksheet = sh.worksheet(tab_name)
    df = pd.DataFrame(worksheet.get_all_records())
    # print(df)
    return df

# # Gọi hàm với tên bảng tính và tab cụ thể
data = get_sheet_data(credentials,"DataSep","Tab2")


# cách lấy pass và email trong data lấy hết xuất hiện cùng lúc chứ không phải lần lượt 
for index, row in data.iterrows():
    email = row['email']
    password = row['pass']
    # print(f"Email: {email}, Password: {password}")


# cách lấy email và pass ở dòng thứ 5 dòng thứ 5 tương ứng với index = 4 do index bắt đầu từ 0 chú ý là chỉ lấy dòng 5 chứ không lấy đc lần lượt
row_index = 1000 # Chỉ số của dòng thứ 5 là 4
if row_index < len(data):  # Kiểm tra xem chỉ số có hợp lệ không
    email = data.iloc[row_index]['email']
    password = data.iloc[row_index]['pass']
    # print(f"Email: {email}, Password: {password}")
else:
    print("Dòng thứ 5 không tồn tại.")



# cách lấy email và pass từ số hàng đầu tiên đến hết hàng. lấy lần lượt đến hết chứ không chọn được hàng bắt đầu như code dưới
num_rows = data.shape[0]
for row_index in range(num_rows):# Vòng lặp từ 0 đến số hàng
    email = data.iloc[row_index]['email']
    password = data.iloc[row_index]['pass']
    tai_khoan = email
    # print(f"Email: {email}, Password: {password}")
    row_index = row_index + 1
    print(tai_khoan)


# cách lấy lần lượt từng email và pass lấy xong rồi lấy tiếp dòng tiếp theo nhưng bắt đầu từ dòng thứ 5 lần lượt

# Lấy email và mật khẩu bắt đầu từ dòng thứ 5 (index 4)
start_row_index = 1000  # Dòng thứ 5 tương ứng với chỉ số 4
num_rows = data.shape[0]  # Số lượng hàng trong DataFrame

# Kiểm tra chỉ số bắt đầu có hợp lệ không
if start_row_index < num_rows:
    for row_index in range(start_row_index, num_rows):
        email = data.iloc[row_index]['email']
        password = data.iloc[row_index]['pass']
        # print(f"Email: {email}, Password: {password}")
        tai_khoan = email
        # print(tai_khoan)
else:
    print("Dòng thứ 5 không tồn tại.")

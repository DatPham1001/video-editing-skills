# Chia khung: nền mờ, người tách nền rõ nét

Áp dụng cho mọi đoạn chia hai có người nói. Đây là mặc định đã được người dùng yêu cầu; không cần hỏi lại cho từng job. Giữ cách xen kẽ popup/split và timing đã duyệt.

## Lớp hình bắt buộc

1. Video A-roll gốc chạy liên tục, muted, làm nền toàn khung. Khi split vào, nội suy blur mạnh và dim nhẹ; tham chiếu blur khoảng 50–65px trên canvas 1080×1920, brightness khoảng 0.85–0.92 so với grade hiện tại. Chọn theo source để hậu cảnh không cạnh tranh với người nói. Không blur bài báo, phụ đề hoặc lớp người đã tách nền.
2. Người nói được tách nền bằng **alpha matte đúng từng frame**, đặt rõ nét phía trước nền mờ. Crop/scale người đồng đều, full ngang phía dưới, nâng đủ cao và giữ tóc, kính, bàn tay/micro khi có. Không dùng crop chữ nhật của video còn nguyên hậu cảnh hoặc mask hình học giả đầu thay cho tách nền. Áp cùng grade hiện tại cho RGB người; không nhân gain/rate tiếng.
3. Tư liệu phía trên, gọn trong safe zone. Phụ đề split giữ tâm x≈540/y≈960, chuyển mượt về y≈1290 khi ra. Không sửa layout của tư liệu/caption để che lỗi matte.

Khung tham chiếu trước đây: video nền phủ canvas, lớp người nguồn 1080×1920 ở global top khoảng 550–570 hoặc vị trí tương đương theo crop; vẫn phải cân theo source thực. Một lựa chọn khác là panel dưới y≈920 có image alpha dịch lên bên trong. Kích thước/lớp crop không được làm cắt tóc hoặc méo người.

## Chuẩn bị và ánh xạ matte

- Tách từ đúng source/proxy và cut map hiện tại. Lưu model/hash, source/hash, fps và khoảng frame. Với model có recurrent state, xử lý tuần tự và warm-up trước cảnh; không suy alpha bằng một still cho cả đoạn.
- Chuẩn bị đủ frame cho cả entry, hold, exit và handles; RGB/alpha cùng frame, cùng tốc độ và cùng crop. Nếu có retime, ghi rõ master/local mapping, không áp offset hoặc tốc độ hai lần.
- PNG RGBA sequence hoặc video alpha đều được nếu preview và renderer đọc đúng. Kiểm alpha thực sự trong suốt ở hậu cảnh; file có kênh alpha nhưng alpha trắng toàn ảnh chưa phải tách nền.
- Trong preview/export, giữ một video nền liên tục, một track tiếng liên tục; lớp người tách nền không phát thêm tiếng. Fade/chuyển vị trí alpha theo cùng layout progress để không có khung chữ nhật bật lên ở đầu/cuối. Tránh để hai bóng người chồng lên nhau lúc chuyển vị trí: làm mờ nền sớm và đưa lớp người tách nền lên đủ rõ trước khi chuyển khung; kiểm thực tế rồi tinh envelope thay vì buộc mọi lớp có cùng opacity.

## Điều kiện giao

Kiểm đủ file/frame và xem composed frames đầu/giữa/cuối của **từng đoạn split**, gồm chuyển vào/ra; kiểm tóc, rìa kính, vai, tay/micro, lỗ thủng và bóng viền. Hậu cảnh phải mờ, người rõ nét và đã mất nền thật. Thử playback để phát hiện matte lệch frame/nhấp nháy; không gọi hoàn tất khi chỉ sửa code blur hoặc mới tách một frame mẫu.

Nếu matte chưa đủ hoặc chất lượng chưa đạt, tiếp tục sửa tách nền trước khi giao. Khi công cụ không thể xử lý được, báo rõ phần chưa xong, không tự thay bằng crop nền rõ rồi báo hoàn tất.


Quy tắc phạm vi tách nền: **chỉ bật lớp người tách nền khi layout hiện hành là chia hai/split và split progress > 0**. A-roll, highlight chữ, popup và countdown không bật matte. Không dùng điều kiện `split || highlight`; đây là mặc định hiện hành thay các preset lồng chữ sau đầu cũ.

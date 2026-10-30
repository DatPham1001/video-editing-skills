# Pop-up highlight giữa màn hình

Quy tắc người dùng hiện hành ưu tiên: capture thiếu chú thích/ngày/nguồn thì bỏ trường đó, ẩn hàng/footer trống; không tự thêm giải thích “chưa xác minh/chưa xác thực” hoặc caveat vào popup. Ghi chú nghiên cứu ở hồ sơ job. Áp cả khi tái dùng preset cũ.

Đây là preset v1 tùy chọn. Phong cách mặc định hiện tại ở [dark-tech-v2](dark-tech-v2.md), dùng Remotion trực tiếp, caption 10–12 từ và xen kẽ popup/split. Không ép thêm tag/caveat cho ý kiến riêng, không áp hướng dẫn import ChatCut trừ khi người dùng chọn surface đó.

Dùng khi người dùng yêu cầu chữ nhấn pop-up ở giữa, làm mờ talking head phía sau, hoặc ở bước2 đã được phép sau duyệt cắt thô. Job mới phải hoàn thành bước1 và dừng duyệt bản thô trước; không có checkpoint draft transcript/draft hiệu ứng. Giữ phong cách teal/navy của video; đọc [preset](../assets/highlight-popup-v1/preset.json) và dùng nguyên [component](../assets/highlight-popup-v1/HighlightPopV1.tsx).

Tìm câu nhấn trong transcript hiện tại và kiểm tra caption đã sửa; dùng find_transcript để canh từ khóa, đọc lại timeline để lấy clip/range thật. Chọn các khoảng trống giữa evidence và hình minh họa; không chồng lên chúng. Không tự nhấn số liệu đang HOLD như dữ kiện đã xác nhận. Chữ nhấn được rút gọn sát câu nói, không thêm luận điểm mới. Có thể giữ tag bối cảnh như “THỬ TƯỞNG TƯỢNG” khi câu nằm trong tình huống giả định.

HighlightPopV1 dùng canvas1080×1920/30fps, panel940×460 tại(70,730), tâm đúng(540,960). Hai dòng chữ đậm, dòng cuối teal/vàng; spring19/210/.65, scale .74→1, Y64→0; mỗi dòng stagger4f; opacity vào5f, ra6f; gạch nhấn và pulse canh theo accentAt. Props: lines (thường2 dòng), fontSize (68–108 ở bản đã dựng, điều chỉnh vừa khung), accent, accentAt (frame tương đối), tag (có thể rỗng). Vùng chữ hữu dụng856px, đo glyph bằng font thật; pulse phóng thêm2.5% cũng cần vừa. Dùng font reference-bold.ttf từ assets/evidence-remotion-v1/fonts/, copy vào public/fonts/.

Caption trước ngực được giữ riêng bên dưới panel; bản tham chiếu top1414/font48px. Không repaginate hoặc thay nội dung caption khi chỉ thêm highlight. Yêu cầu center+blur là chủ ý phủ hình người nói bằng chữ trong đoạn nhấn; các đoạn thường vẫn theo quy tắc bảo vệ mặt của talking-head-guide.

Mở Studio và đăng ký Composition cho từng đoạn, hoặc đóng gói các scene vào một alpha WebM để bớt khởi động render. Nếu đóng gói, đặt guard trong suốt2f mỗi đầu scene, Sequence durationInFrames đúng độ dài để useCurrentFrame/useVideoConfig reset animation. Ghi sourceFrame từng scene, đặt sourceStartFromInSeconds=sourceFrame/30 chính xác trên mỗi instance; không dùng0 cho tất cả instance. Native instance vẫn tách riêng, không ghép phẳng A-roll.

Render VP9alpha như [workflow evidence](evidence-remotion.md), codec vp9/image-format png/pixel-format yuva420p/bitrate5M/concurrency2, không audio. Kiểm alpha và frame ra cuối để tránh nền đen/scene bên cạnh lọt vào. Chèn lên track hình phía trên, khung1080×1920 fit contain, không ripple. Gắn Gaussian Blur radius180 vào TỪNG clip A-roll giao với đoạn highlight; dùng planner evidence để tính adds, rồi thay sourceStartFromInSeconds nếu dùng library. Giữ exact range, không blur chữ/caption. validateOnly rồi commit trong phạm vi đã được yêu cầu.

Xem composed frames tất cả pop-up, kiểm các frame vào/ra và mối cắt nền; đọc lại cấu trúc và caption revision. Lưu props/range/source offsets/asset IDs trong manifest JOB, không trong skill. Muốn thay phong cách thì tạo preset mới, giữ v1 để tái dùng đúng mẫu.
